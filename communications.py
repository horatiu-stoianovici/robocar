import socket
import _thread as thread

TCP_PORT = 5005
BUFFER_SIZE = 3

def __mainLoop(s):
	conn, addr = s.accept()
	print ('Connected from ', addr)
	while 1:
		data = conn.recv(BUFFER_SIZE)
		if not data: 
			break
		print('received data:', data)
		conn.send(data.upper())
	conn.close()

def startServer():
	#creating a socket
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind(('', TCP_PORT))
	s.listen(1)

	#start thread that gets connections
	thread.start_new_thread(__mainLoop, (s,))


startServer()
input()