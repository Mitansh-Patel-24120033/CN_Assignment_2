import socket
import argparse
import time

def start_client(host, port, nagle, delack):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print()
    print(f"Nagle: {nagle} & Delayed ACK: {delack}")
    print(f"Sending to {host}:{port}...")
    # Apply Nagle and Delayed-ACK settings
    if not nagle:
        client_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    if not delack:
        client_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_QUICKACK, 1)

    client_socket.connect((host, port))
    
    with open('4KB_file.txt', "rb") as f:
        while chunk := f.read(40):  # 40 B/s rate
            client_socket.sendall(chunk)
            time.sleep(1)  # Throttle to ~2 minutes for 4KB

    client_socket.close()
    print("File sent")
    print()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=12345)
    parser.add_argument("--nagle", action="store_true")
    parser.add_argument("--delack", action="store_true")
    args = parser.parse_args()
    start_client(args.host, args.port, args.nagle, args.delack)
