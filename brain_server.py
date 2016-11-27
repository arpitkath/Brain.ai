from socket import *
from Brain import Brain
import re
import string


def clean_query(s):
	#s = re.sub(r'[^\w]', '', s)
	printable = set(string.printable)
	s = filter(lambda x: x in printable, s)
	s = s.strip('\r\n\t ')
	while ord(s[0]) < 97 or ord(s[0]) > 122:
		s = s[1:]
	return s

HOST = "192.168.43.46"
print HOST
PORT = 8007 #open port 7000 for connection
s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(99999999) #how many connections can it receive at one time
conn, addr = s.accept() #accept the connection
print "Connected by: " , addr #print the address of the person connected
brain = Brain()
while True:
    query = conn.recv(1024) #how many bytes of data will the server receive
    query = clean_query(query)
    print "Received: ", repr(query)
    reply = brain.response(query) #server's reply to the client
    print "Reply: ", reply
    conn.send(reply+'\r\n')
conn.close()
