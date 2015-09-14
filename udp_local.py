import socket,sys

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
max = 65535
port = 1060
print sys.argv[1:]
if sys.argv[1:] == ['server']:
	s.bind(('127.0.0.1',port))
	print 'listening at',s.getsockname()
	while True:
		data,address = s.recvfrom(max)
		print 'The client at', address, 'says', repr(data)
		s.sendto('Your data was %d bytes' % len(data), address)
elif 'client' in sys.argv[1:]  :
#elif sys.argv[1:] == ['client']:
	print 'Address before sending:', s.getsockname()
	s.sendto( sys.argv[2], ('127.0.0.1', port))
	#s.sendto('This is my message2', ('127.0.0.1', port))
	print 'Address after sending', s.getsockname()
	data, address = s.recvfrom(max) # overly promiscuous - see text!
	print 'The server', address, 'says', repr(data)
else:
	print >>sys.stderr, 'usage: udp_local.py server|client'
