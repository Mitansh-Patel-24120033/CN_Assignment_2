import socket
import time
import threading
import json

SERVER_IP = input("Enter Server IP: ")
PORT = input("Enter Server Port: ")
fl='metrics_2.json'
threads=[]
conn_data=[]
	
print("Legitimate Traffic START")
def client_conn(client_id):
	try:
		#Establishes proper TCP connection
		start=time.time()
		cnt=0
		c=0
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((SERVER_IP, PORT))
		cnt=time.time()
		while True:
		    s.send(b"Hello Server, How Are You?")
		    s.recv(1024)  # Wait for response
		    c+=1
		    if time.time()-start >= 140:
		    	break			

	except Exception as e:
		print(f"Client {client_id}: Connection failed - {str(e)}")
		s.close()
	finally:
		end=time.time()
		if cnt!=0:
			print(f"Client {client_id} ran for {end-start:.2f}s, took {cnt-start}s to connect, {c} messages")
			_j={'id':client_id, 'conn_time':round(cnt-start,5), 'num_msgs':c}
			conn_data.append(_j)
		s.close()
for i in range(100):
	thread = threading.Thread(target=client_conn, args=(i+1,))
	threads.append(thread)
	thread.start()
	time.sleep(0.25)  # Stagger connection attempts

# Wait for all threads to complete
for thread in threads:
	thread.join()
with open(fl, 'w') as f:
    json.dump(conn_data, f, indent=4)
print("Legitimate Traffic END")
