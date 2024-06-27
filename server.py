import socket
import threading
import time

def handle_client(client_socket, address):
    print(f"Accepted connection from {address}")
    while True:
        data = client_socket.recv(1024)
        if not data:
            print(f"Connection from {address} closed")
            break
        message = data.decode('ascii')
        print(f"Received from {address}: {message}")
        time.sleep(10)  # Introduce a 10-second delay
        modified_data = message + ' (processed)'
        client_socket.send(modified_data.encode('ascii'))
    client_socket.close()

def main():
    host = '127.0.0.1'
    port = 12345
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")
    try:
        while True:
            client_socket, address = server_socket.accept()
            client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
            client_thread.start()
    except KeyboardInterrupt:
        print("Server shutting down")
        server_socket.close()

if __name__ == "__main__":
    main()