from fichiers_definitions import fichier 
import socket
import json
import pickle

print ("User:")
donne = fichier(2, 'file_sample')
output = open('data.pkl', 'wb')
print(donne.to_JSON())
dump=pickle.dumps(donne)
print(dump)
donne.print_text()

HOST = 'localhost' 
PORT = 50007              

'''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
line='hello,world'
s.sendall(str.encode(line))
data = s.recv(1024)
s.close()
print('Received', repr(data))
'''