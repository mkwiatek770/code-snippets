import socket
import sys

PORT = 1235
HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), PORT))
while True:
    full_msg = ""
    new_msg = True
    msg_len = 0

    while True:
        msg = s.recv(16).decode("utf-8")
        if new_msg:
            msg_len = int(msg[:HEADERSIZE].strip())
            new_msg = False
            full_msg += msg[HEADERSIZE:]
        else:
            full_msg += msg
        if len(full_msg) == msg_len:
            if full_msg == "END":
                print("Connection closed")
                s.close()
            print(f"Message received: {full_msg}")
            break


s.close()
