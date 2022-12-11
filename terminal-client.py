import socket
import threading

# getting IP and PORT information
IP: str = input("IP ADDRESS (LEAVE BLANK FOR LOCALHOST) > ")
if IP == "":
    IP = "localhost" 

PORT: str = input("PORT (LEAVE BLANK FOR DEFAULT 6166) > ")
if PORT == "":
    PORT = "6166"

# actual tuple that is used
ADDRESS = (IP, int(PORT))

def fetch_messages(client: socket.socket):
    while True:
        buf = client.recv(1024)
        if len(buf) != 0:
            print(buf.decode("utf-8"))

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("[CLIENT] connecting to server...")
    client.connect(ADDRESS)

    thread = threading.Thread(target=fetch_messages, args=(client,))
    thread.start()

    print(f"[CLIENT] successfully established connection with {ADDRESS}")

    while True:
        try:
            message = input()
        except KeyboardInterrupt:
            exit(0)

        if len(message) > 0:
            client.send(message.encode("utf-8"))
        if message == "!q":
            client.close()
            exit(0)
    
# dumb python shit
if __name__ == "__main__":
    main()