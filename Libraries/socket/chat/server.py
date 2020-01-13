import socket
import select
import time

HEADERSIZE = 10
PORT = 1235


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((socket.gethostname(), PORT))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Connected with {address}")
    messages = [
            "Hi loser!",
            "I've got something to tell you.",
            "You suck",
            "In python",
            "And in JavaScript",
            "END"
            ]
    for message in messages:
        msg = f"{len(message):<{HEADERSIZE}}" + message

        clientsocket.send(bytes(msg, "utf-8"))
        time.sleep(2)
    break
s.close()

