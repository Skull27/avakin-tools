import requests
import hashlib
import json
from pprint import pprint
from urllib3.exceptions import InsecureRequestWarning
#===================[LOGO]=========================
print('''

  ██████▓█████ █     ████▄    █ ██ ▄█▀██▓███▄    █ 
▒██    ▒▓█   ▀▓█░ █ ░███ ▀█   █ ██▄█▒▓██▒██ ▀█   █ 
░ ▓██▄  ▒███  ▒█░ █ ░▓██  ▀█ ██▓███▄░▒██▓██  ▀█ ██▒
  ▒   ██▒▓█  ▄░█░ █ ░▓██▒  ▐▌██▓██ █▄░██▓██▒  ▐▌██▒
▒██████▒░▒████░░██▒██▒██░   ▓██▒██▒ █░██▒██░   ▓██░
▒ ▒▓▒ ▒ ░░ ▒░ ░ ▓░▒ ▒░ ▒░   ▒ ▒▒ ▒▒ ▓░▓ ░ ▒░   ▒ ▒ 
░ ░▒  ░ ░░ ░  ░ ▒ ░ ░░ ░░   ░ ▒░ ░▒ ▒░▒ ░ ░░   ░ ▒░
░  ░  ░    ░    ░   ░   ░   ░ ░░ ░░ ░ ▒ ░  ░   ░ ░ 
      ░    ░  ░   ░           ░░  ░   ░          ░ 
	''')

# put your email address in the email field & your password in the password field to get the FULL & hidden statistics about your profile, enjoy!
#==================[LOGIN INFO]======================
Email = "example@email.com"
Password = "your_password"
#==================[SETTINGS]========================
url = "https://api.avkn.co/auth/1/auth/1/login"
url2 = "https://api.avkn.co/profile/1/profile/1/get"
url3 = "https://api.avkn.co/ws/1/stat/1/get"
url4 = "https://api.avkn.co/ws/1/xp/1/get"
url5 = "https://api.avkn.co/ws/1/balance/1/get"
timeout = 1000
cert_verify = False
req_payload = {}
#===================[CONTENT]========================
hash_object = hashlib.md5(Password.encode())
md5_hash = hash_object.hexdigest()
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

s = requests.Session()
login_data = {"type":"email","request":{"password":md5_hash,"email_address":Email}}

r = s.post(url, json=login_data, timeout=timeout, verify=cert_verify)
Logincookies = r.headers
r.headers
r = s.post(url2, json=req_payload, headers=Logincookies, timeout=timeout, verify=cert_verify)
r = json.loads(r.text)

r2 = s.post(url3, json=req_payload, headers=Logincookies, timeout=timeout, verify=cert_verify)
r2 = json.loads(r2.text)

r3 = s.post(url4, json=req_payload, headers=Logincookies, timeout=timeout, verify=cert_verify)
r3 = json.loads(r3.text)

r4 = s.post(url5, json=req_payload, headers=Logincookies, timeout=timeout, verify=cert_verify)
r4 = json.loads(r4.text)

class bcolors:
    OKGREEN = '\033[92m'
    ENDC = '\033[0m'
print (bcolors.OKGREEN + "SUCCESS!" + bcolors.ENDC)
print (bcolors.OKGREEN + "========================================================================" + bcolors.ENDC)
pprint(r4)
print (bcolors.OKGREEN + "========================================================================" + bcolors.ENDC)
pprint(r)
print (bcolors.OKGREEN + "========================================================================" + bcolors.ENDC)
pprint(r2)
print (bcolors.OKGREEN + "========================================================================" + bcolors.ENDC)
pprint(r3)
print (bcolors.OKGREEN + "========================================================================" + bcolors.ENDC)
