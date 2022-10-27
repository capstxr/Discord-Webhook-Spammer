import requests
import time
import pyfiglet
import os

banner = pyfiglet.figlet_format("SPAMMER")
print(banner)

print("Message mode:")
messageMode = input("File list or One: ")
webHook = input("Webhook link: ")

def send(message, webhookLink):
    try:
        data = requests.post(webhookLink, json={'content': message})

        if data.status_code == 204:
            print(f"\nMessage: {message} was succesfully sent.")
        time.sleep(3)
    except:
        print("Webhook is not available.")
        time.sleep(5)
        exit()

if messageMode == "File list":
    pathToArr = input("Path containing text file: ")

    for root, dirs, files in os.walk(pathToArr):
        for file in files:
            if file.endswith('.txt'):
                print("File found.\nStarting spam.")
                time.sleep(1)

                lines = tuple(
                    open(pathToArr + "\\" + file, 'r')
                )

                while True:
                    for i in lines:
                        send(i, webHook)    
else: 
    a = input("Message to spam: ")
    while True:  
        send(a, webHook)