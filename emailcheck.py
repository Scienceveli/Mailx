import requests
import string
import random
import time
from user_agent import generate_user_agent
lst = open("email.txt","r")
print("""
    ███████╗███╗   ███╗ █████╗ ██╗██╗      ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗
    ██╔════╝████╗ ████║██╔══██╗██║██║     ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝
    █████╗  ██╔████╔██║███████║██║██║     ██║     ███████║█████╗  ██║     █████╔╝ 
    ██╔══╝  ██║╚██╔╝██║██╔══██║██║██║     ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ 
    ███████╗██║ ╚═╝ ██║██║  ██║██║███████╗╚██████╗██║  ██║███████╗╚██████╗██║  ██╗
    ╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝
by @Makavael +201029107547""")
print("")
print("click Ctrl Z to stop")
sleep = int(input("sleep : "))
while True:
    reads = lst.readline().split('\n')[0]
    time.sleep(sleep)
    req = requests.session()
    req.headers = {'user-agent': generate_user_agent()}
    req.headers.update({'X-CSRFToken': "missing"})    
    rz = requests.get(f'https://emailsverified-django.herokuapp.com/api/yahoo/?username={reads.replace("@yahoo.com","")}').text
    rg = requests.get(f'https://emailsverified-django.herokuapp.com/api/gmail/?username={reads.replace("@gmail.com","")}').text
    if "taken" in rz:
        print(f"{reads}: Taken[!]")
        with open("Linked.txt", "a") as Linked:
            Linked.write(reads + "\n")
    elif "available" in rz:
        print(f"{reads} : Available[*]")
        with open("NotLinked.txt", "a") as Linked:
            Linked.write(reads + "\n")
    elif "available" in rg:
        print(f"{reads} : Available[*]")
        with open("NotLinked.txt", "a") as Linked:
            Linked.write(reads + "\n")
    elif "taken" in rg:
        print(f"{reads} : Taken[!]")
        with open("Linked.txt", "a") as Linked:
            Linked.write(reads + "\n")
    else:
        print(f"{reads} : Unknown[*]")
else:
    
    print(f"UnLinked : {reads}")
