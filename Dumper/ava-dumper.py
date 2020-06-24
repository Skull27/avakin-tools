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

# Auth, put your avakin life email address in the Email field, your password in the Password field & the target's username/friend code in the User_id field... enjoy!
#=================[LOGIN INFO]=======================
Email = "example@email.com"
Password = "your_password"
User_id = "username_or_friendcode_oftarget"
#==================[SETTINGS]========================
url = "https://api.avkn.co/auth/1/auth/1/login"
url2 = "https://api.avkn.co/search/1/search/1/search"
url3 = "https://api.avkn.co/profile/1/profile/1/data"
url4 = "https://api.avkn.co/ws/1/lastseen/1/get"
timeout = 1000
cert_verify = False
#===================[CONTENT]========================

hash_object = hashlib.md5(Password.encode())
md5_hash = hash_object.hexdigest()

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
cert = False

s = requests.Session()
login_data = {"type":"email","request":{"password":md5_hash,"email_address":Email}}

r = s.post(url, json=login_data, timeout=timeout, verify=cert_verify)
Logincookies = r.headers
r.headers
r = s.post(url2, json={"contexts":["users"],"term":User_id}, headers=Logincookies, timeout=timeout, verify=cert_verify)
r = json.loads(r.text)

# Settings, get id from first response
id_From_Response1 = r["results"][0]['id']

big = {"widgets":{"main":{"profile":{"user_id":int(id_From_Response1)},"xp":{"user_id":int(id_From_Response1)},"item_stats":{"user_id":int(id_From_Response1)}}}}

big2 = {"user_ids":[int(id_From_Response1)]}

# Settings, set id of second response
r2 = s.post(url3, json=big, headers=Logincookies, timeout=timeout, verify=cert_verify)

r3 = s.post(url4, json=big2, headers=Logincookies, timeout=timeout, verify=cert_verify)
r3 = json.loads(r3.text)

class bcolors:
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    ENDC = '\033[0m'

pfp = ("Profile picture = https://profile.avkn.life/pass.php?soq=" + id_From_Response1)
print (bcolors.OKGREEN + "SUCCESS!" + bcolors.ENDC)
print (bcolors.OKGREEN + "========================================================================" + bcolors.ENDC)
print (pfp)
print (bcolors.OKGREEN + "========================================================================" + bcolors.ENDC)
pprint (r3)
print (bcolors.OKGREEN + "========================================================================" + bcolors.ENDC)
r2 = json.loads(r2.content)
pprint(r2)
print (bcolors.OKGREEN + "========================================================================" + bcolors.ENDC)
