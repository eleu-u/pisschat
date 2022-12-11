import socket 
import threading

ADDRESS = ("localhost", 6166)

clients = set()
names = {}

def get_name(address: str):
    # if its in the names dictionary, return the value from the dict
    if address in names:
        return names[address]
    # otherwise return the same value that was inputted
    return address

def send_all_clients(message):
    print(message)
    for i in clients:
        i.sendall(message.encode("utf-8"))

# handling client, doing stuff with the data that gets sent by clients
def handle_client(client, address):
    send_all_clients(f"[SERVER] {get_name(address)} connected to session")

    clients.add(client)

    while True:
        msg = client.recv(1024)
        if (len(msg) == 0) or (msg.decode("utf-8") == "!q"):
            send_all_clients(f"[SERVER] {get_name(address)} disconnected from session")
            
            print(f"[SERVER] active connections: {threading.activeCount() - 2}")
            break

        msg = msg.decode("utf-8")
        args = msg.split(" ")
        if len(args) > 1:
            if args[0] == "!set-name":
                send_all_clients(f"[SERVER] {get_name(address)} changed their name to {args[1]}")
                names[address] = args[1]
                continue

        send_all_clients(f"[{get_name(address)}] {msg}")
        
    clients.remove(client)
    client.close()

# sets up and connects clients properly with threading
def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDRESS)

    server.listen()
    print(f"listening on {ADDRESS[0]}:{ADDRESS[1]}")
    
    while True:
        try:
            conn, addr = server.accept()
        except KeyboardInterrupt:
            exit(0)

        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[SERVER] active connections: {threading.activeCount() - 1}")

if __name__ == "__main__":
    main()