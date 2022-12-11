import socket
import threading
import wx

client = None

def connect_server(address: str, port: str, messages_box: wx.TextCtrl):
    global client
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    messages_box.AppendText(f"[SERVER] connecting to {address}:{port}...\n")
    client.connect((address, int(port)))
    messages_box.AppendText(f"[CLIENT] successfully established connection with {address}:{port}\n")

    thread = threading.Thread(target=update_messagesbox, args=(messages_box,))
    thread.daemon = True # this makes the wxpython window close properly
    thread.start()

def send_message(message: str):
    if len(message) > 0 and len(message) < 1023:
        client.send(message.encode("utf-8"))

def update_messagesbox(messages_box: wx.TextCtrl):
    while True:
        try:
            buf = client.recv(1024)
            if len(buf) != 0:
                messages_box.AppendText(buf.decode("utf-8") + "\n")
        except: # we make this do Nothing if an exception is thrown
            continue