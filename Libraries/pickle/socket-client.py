import pickle
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1235))

msg = s.recv(1024)
deserialized_obj = pickle.loads(msg)
print(deserialized_obj)


