import socket


class HServer:

	def __init__(self):
		self.TCP_PORT = 5005
		self.BUFFER_SIZE = 3

		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.s.bind(('', TCP_PORT))
		self.s.listen(1)

		conn, addr = s.accept()
print 'Connection address:', addr
while 1:
	data = conn.recv(BUFFER_SIZE)
	if not data: break;
	print 'received data:', data
	conn.send(data.upper())
conn.close()
