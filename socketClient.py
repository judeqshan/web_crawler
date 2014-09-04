
import socket
import time

HOST = '192.168.1.105'

PORT = 50007

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((HOST, PORT))

while 1:
	cmd = raw_input("Your command:").strip()
	s.sendall(cmd)
	s.settimeout(10)
	try:
		data = s.recv(1024)
	except Exception, e:
		continue
	#time.sleep(2)
	print data

s.close()	 
