import socket
import thread
from carcontrol import CarController

TCP_PORT = 6005
BUFFER_SIZE = 3
controller = CarController()

#this is the main loop for receiving data
def __mainLoop(s):
        global controller
	conn, addr = s.accept()

	#after connection is accepted start a new thread that will be able to accept a new connection
	thread.start_new_thread(__mainLoop, (s,))
	print ('Connected from ', addr)
	#read data while connection is live
	while 1:
		data = conn.recv(BUFFER_SIZE)
		if not data: 
			break
		if data[0] == 'L':
                        #left
                        if data[1] == 'D':
                                #key down
                                controller.startLeft()
                                pass
                        elif data[1] == 'U':
                                #key up
                                controller.stopLeft()
                                pass
                elif data[0] == 'R':
                        #right
                        if data[1] == 'D':
                                #key down
                                controller.startRight()
                                pass
                        elif data[1] == 'U':
                                #key up
                                controller.stopRight()
                                pass
                elif data[0] == 'F':
                        #forward
                        if data[1] == 'D':
                                #key down
                                controller.startForward()
                                pass
                        elif data[1] == 'U':
                                #key up
                                controller.stopForward()
                                pass
                elif data[0] == 'B':
                        #backward
                        if data[1] == 'D':
                                #key down
                                controller.startBackward()
                                pass
                        elif data[1] == 'U':
                                #key up
                                controller.stopBackward()
                                pass
		conn.send('OK')
	conn.close()

def startServer():
	#creating a socket
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind(('', TCP_PORT))
	s.listen(1)

	#start thread that gets connections
	thread.start_new_thread(__mainLoop, (s,))


startServer()
raw_input()
controller.__exit__(None, None, None)
