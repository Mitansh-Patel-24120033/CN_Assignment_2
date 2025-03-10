import socket
import threading

def handle_client(client_socket):
    """TCP connection handler (legitimate traffic)"""
    try:
        while True:
            data = client_socket.recv(1024)  # Keep connection open
            if not data:
                break  # Client closed connection
            client_socket.send(b"Hi! We received...")
    except Exception as e:
        print(e)
    client_socket.close()

# Create TCP socket (SOCK_STREAM)
SER_IP=input("Enter Server IP: ")
SER_PORT=input("Enter Server Port: ")
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((SER_IP, SER_PORT))
server.listen(4096)  # Must match net.ipv4.tcp_max_syn_backlog
server.settimeout(150)

print(f"TCP Server listening on {SER_IP}:{SER_PORT}...")
while True:
    try:
        client, addr = server.accept()  # Completes TCP handshake
        print(addr)
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()
    except Exception as e:
        print(e)
        server.close()
        break


