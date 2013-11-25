from fichiers_definitions import fichier 
import socket

print ("User:")
donne = fichier(1, 'file_sample')
donne.read_print_fichier()

HOST = 'localhost' 
PORT = 50007              # The same port as used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall(b'Hello, world')
data = s.recv(1024)
s.close()
print('Received', repr(data))