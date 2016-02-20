
import crypt

def testPass(cryptPass):
	salt = cryptPass[0:2]
	print salt
	dictFile = open('dictionary.txt','r')
	
	for word in dictFile.readlines():
		#print word
		#word = word.strip('\n')
		#print word
		cryptWord = crypt.crypt(str(word),str(salt))
		if (cryptWord == cryptPass):
			print "[+] Found Password: "+word+"\n"
			return
		else:
			print "[-] Password Not Found.\n"
			return

def main():
	passFile = open('password.txt')
	for line in passFile.readlines():
		if ":" in line:
			user = line.split(':')[0]
			cryptPass = line.split(':')[1].strip(' ')
			print cryptPass
			print "[*] Cracking Password For: "+user
			testPass(cryptPass)

if __name__ == "__main__":
	main()
