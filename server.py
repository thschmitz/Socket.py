import socket 
import threading

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname()) #127.0.1.1
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print("[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT) # How many bites we are going to send at a time.
        msg_length = int(msg_length)
        msg = conn.recv(msg_length).decode(FORMAT)
        if msg==DISCONNECT_MESSAGE:
            connected = False

        print("[{%}] {%}".format(addr, msg))
    conn.close()


def start():
    server.listen()
    print(f"[*] Listening on {SERVER}:{PORT}")
    while True:
        conn, addr = server.accept()
        print(f"[+] {addr} connected.")
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print("[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

print("[STARTING] server is starting...")
start()