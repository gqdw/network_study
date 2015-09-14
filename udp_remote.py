import random
import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM )
MAX = 65535
PORT = 1060

interface = sys.argv[2] if len(sys.argv) >2 else ''

if sys.argv[1] == 'server':
	s.bind((interface,PORT))
	print 'listening at',s.getsockname()
	while True:
		data,address = s.recvfrom(MAX)
		if random.randint(0,1):
			print 'the client at',address,'says:',repr(data)
			s.sendto('your data was %d bytes' % len(data),address)
		else:
			print 'Pretending to drop packet from', address
elif sys.argv[1] == 'client':
	hostname = sys.argv[2]
	s.connect(( hostname,PORT))	
	print 'Client socket name is', s.getsockname()
	delay = 0.1
	while True:
		s.send('this is another message')
		print 'Waiting up to', delay, 'seconds for a reply'
		s.settimeout(delay)
		try:
			data = s.recv(MAX)
		except socket.timeout:
			delay *=2 
			if delay > 2.0:
				raise RuntimeError('I think the server is down')
		except:
			raise
		else:
			break
	print 'the server says',repr(data)
else:
	print >> sys.stderr ,'usage: udp_remote.py server [ <interface> ]'	
	print >> sys.stderr, ' or: udp_remote.py client <host>'
	sys.exit(2)




