def checkVulns(banner):
	f = open("vuln_banners.txt",'r')
	for line in f.readlines():
		if line.strip('\n') in banner:
			print "[+] Server is vulnerable: "+banner.strip('\n')
