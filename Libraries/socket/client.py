import socket

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

while True:

    full_msg = ""
    new_msg = True
    while True:
        msg = s.recv(16)
        if new_msg:
            msglen = int((msg[:HEADERSIZE].strip()))
            print(f"new message length: {msglen}")
            new_msg = False
            full_msg += msg.decode("utf-8")[HEADERSIZE:]
        else:
            full_msg += msg.decode("utf-8")
        if len(full_msg) == msglen:
            print("full msg received")
            print(full_msg)
            new_msg = True
            full_msg = ""

