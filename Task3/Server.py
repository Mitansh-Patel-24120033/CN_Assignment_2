import socket
import argparse
import time
import json
import os

def start_server(host, port, nagle, delack):
	fl='metrics_3.json'
	if os.path.exists(fl):
		with open(fl, "r") as f:
			existing = json.load(f)
	else:
		existing=[]
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	server_socket.bind((host, port))
	server_socket.listen(1)
	print()
	print(f"Nagle: {nagle} & Delayed ACK: {delack}")
	print(f"Server listening on {host}:{port}")

	conn, addr = server_socket.accept()
	# Apply Nagle and Delayed-ACK settings
	if not nagle:
		conn.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
	if not delack:
		conn.setsockopt(socket.IPPROTO_TCP, socket.TCP_QUICKACK, 1)

	start_time = None
	total_bytes = 0
	max_chunk = 0
	tpt=0
	gpt=0
	
	try:
		while True:
			data = conn.recv(1024)
			if not data:
				break
			if start_time is None:
				start_time = time.time()
			total_bytes += len(data)
			print(f"Got {total_bytes}B")
			max_chunk = max(max_chunk, len(data))
	except Exception as e:
		print(e)
		exit()
	duration = time.time() - start_time if start_time else 0
	tpt=total_bytes/duration
	gpt=4096/duration
	print("\n--- Metrics ---")
	print(f"Throughput: {tpt:.3f} B/s")
	print(f"Goodput: {gpt:.3f} B/s")
	print(f"Max Packet Size: {max_chunk} B")
	print("Packet Loss: 0.00% (TCP guarantees delivery)")
	
	mtr={"nagle":nagle, 'delayed_ack':delack, 'throughput':round(tpt,3), 'goodput':round(gpt,3), 'max_pac':max_chunk}
	existing.append(mtr)
	with open(fl, "w") as f:
		json.dump(existing, f, indent=2)

	print()
	

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("--host", default="127.0.0.1")
	parser.add_argument("--port", type=int, default=12345)
	parser.add_argument("--nagle", action="store_true")
	parser.add_argument("--delack", action="store_true")
	args = parser.parse_args()
	start_server(args.host, args.port, args.nagle, args.delack)
    
