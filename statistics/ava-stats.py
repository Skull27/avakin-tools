import requests
import hashlib
import json
from pprint import pprint
from urllib3.exceptions import InsecureRequestWarning

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
#==========================================================
Email = "@example@email.com"
Password = "your_password"
#==========================================================
req_payload = {}

hash_object = hashlib.md5(Password.encode())
md5_hash = hash_object.hexdigest()
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

s = requests.Session()
login_data = {"type":"email","request":{"password":md5_hash,"email_address":Email}}

url = "https://api.avkn.co"
r = s.post("https://api.avkn.co/auth/1/auth/1/login", json=login_data, timeout=1000, verify=False)
Logincookies = r.headers
r.headers
r = s.post("https://api.avkn.co/profile/1/profile/1/get", json=req_payload, headers=Logincookies, timeout=1000, verify=False)
r = json.loads(r.text)

r2 = s.post("https://api.avkn.co/ws/1/stat/1/get", json=req_payload, headers=Logincookies, timeout=1000, verify=False)
r2 = json.loads(r2.text)

r3 = s.post("https://api.avkn.co/ws/1/xp/1/get", json=req_payload, headers=Logincookies, timeout=1000, verify=False)
r3 = json.loads(r3.text)

r4 = s.post("https://api.avkn.co/ws/1/balance/1/get", json=req_payload, headers=Logincookies, timeout=1000, verify=False)
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