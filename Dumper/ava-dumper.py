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
	''') #Just a logo

# Auth, put your avakin life email address in the Email field, your password in the Password field & the target's username/friend code in the User_id field... enjoy!
#===================================================
Email = "example@email.com"
Password = "password"
User_id = "friend_code_username"
#===================================================

hash_object = hashlib.md5(Password.encode())
md5_hash = hash_object.hexdigest()

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
cert = False

s = requests.Session()
login_data = {"type":"email","request":{"password":md5_hash,"email_address":Email}}

url = "https://api.avkn.co"
r = s.post("https://api.avkn.co/auth/1/auth/1/login", json=login_data, timeout=1000, verify=cert)
Logincookies = r.headers
r.headers
r = s.post("https://api.avkn.co/search/1/search/1/search", json={"contexts":["users"],"term":User_id}, headers=Logincookies, timeout=1000, verify=cert)
r = json.loads(r.text)

# Settings, get id from first response
id_From_Response1 = r["results"][0]['id']

big = {"widgets":{"main":{"profile":{"user_id":int(id_From_Response1)},"xp":{"user_id":int(id_From_Response1)},"item_stats":{"user_id":int(id_From_Response1)}}}}

big2 = {"user_ids":[int(id_From_Response1)]}

# Settings, set id of second response
r2 = s.post("https://api.avkn.co/profile/1/profile/1/data", json=big, headers=Logincookies, timeout=1000, verify=cert)

r3 = s.post("https://api.avkn.co/ws/1/lastseen/1/get", json=big2, headers=Logincookies, timeout=1000, verify=cert)
r3 = json.loads(r3.text)

pfp = ("Profile picture = https://profile.avkn.life/pass.php?soq=" + id_From_Response1)
print ("========================================================================")
print (pfp)
print ("========================================================================")
pprint (r3)
print ("========================================================================")
r2 = json.loads(r2.content)
pprint(r2)
print ("========================================================================")
