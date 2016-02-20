try:
	print "[+] 1337/0 = "+str(1337/0)
except:
	print "[-] Error. "

#etape2
try:
	print "[+] 1337/0 = "+str(1337/0)
except Exception, e:
	print "[-] Error = "+str(e)

#etape 3
import socket
socket.setdefaulttimeout(2)
s = socket.socket()
try:
	s.connect(("192.168.95.149",21))
except Exception, e:
	print "[-] Error = "+str(e)
