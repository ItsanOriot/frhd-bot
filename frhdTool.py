from frpy import Client
from frpy import getUser
from frpy import getTrack
from frpy import getRace
import frpy
import os
import time

client = Client()

def ready(self):
    pass
client.on("ready", ready)

print("ORIOT'S FRHD TOOL")
print("----------------------------------------")
print("1) Sub Bot")
print("2) Like Bot")
print("3) Comment Bot")
print("4) Accounter Checker")
print("5) Spoof Race (WIP)")
print("select an option: ")

selection = int(input())

while not(isinstance(selection, int)) or not(selection>0 and selection<6):
    print("Improper input. try again: ")
    selection = int(input())

os.system('cls')
if selection == 1:
    with open("<insert your directory>\\users.txt", "r") as users:
        x = users.readline()
        client.login({"login": x.strip("\n"),"password": "INSERT PASSWORD OF ACCOUNTS"})
    print("Enter the username of the user you would like to sub bot: ")
    username = input()
    target = getUser(username)
    progress = 1
    with open("<insert your directory>\\users.txt", "r") as users:
        length = len(users.readlines())
    with open("<insert your directory>\\users.txt", "r") as users:
        for user in users:
            os.system('cls')
            print("Progress: ", progress, "/", length)
            print("Account: ", str(user).strip("\n"))
            try:
                client.login({"login": str(user).strip("\n"),"password": "supalegit"})
            except:
                print("login error. skipping account")
            try:
                target.subscribe()
            except:
                print("subscription error. skipping account")
            client.logout
            progress +=1
    print("Botting Complete")
elif selection == 2:
    userProgress = 1
    trackProgress = 1
    with open("<insert your directory>\\tracks.txt", "r") as tracks:
        trackLength = len(tracks.readlines())
    with open("<insert your directory>\\uncheckedUsers.txt", "r") as users:
        userLength = len(users.readlines())
    with open("<insert your directory>\\uncheckedUsers.txt", "r") as users:
        with open("<insert your directory>\\tracks.txt", "r") as tracks:
            for user in users:
                try:
                    client.login({"login": str(user).strip("\n"),"password": "supalegit"})
                    for track in tracks:
                        os.system('cls')
                        print("Botting Likes...")
                        print("Accounts liked: ", userProgress, "/", userLength)
                        print("Tracks Liked: ", trackProgress, "/", trackLength)
                        print("Account: ", str(user).strip("\n"))
                        try:
                            track.vote(1)
                            trackProgress +=1
                        except:
                            print("Error. Skipping track")
                except:
                    print("login error. skipping account")
                client.logout
                userProgress +=1
elif selection == 3:
    print("comment")
elif selection == 4:
    invalid = []
    unverified = []
    problemCount = 0
    progress = 1
    with open("<insert your directory>\\uncheckedUsers.txt", "r") as users:
        length = len(users.readlines())
    with open("<insert your directory>\\uncheckedUsers.txt", "r") as users:
        track = getTrack(52143)
        for user in users:
            os.system('cls')
            print("Checking all accounts...")
            print("Progress: ", progress, "/", length)
            print("Account: ", str(user).strip("\n"))
            try:
                client.login({"login": str(user).strip("\n"),"password": "supalegit"})
                try:
                    track.vote(1)
                except:
                    unverified.append(str(user))
                    problemCount+=1
                    print("account", str(user).strip("\n"), " not verified. skipping acccount")
            except:
                problemCount+=1
                invalid.append(str(user))
                print("login error. skipping account")
            client.logout
            progress +=1
        print("Account checking complete")
        print("Of the ", length, " accounts checked, ", length-problemCount, " worked and ", problemCount, " did not work.")
        print("Accounts with invalid details: ", invalid)
        print("Accounts which were not properly verified: ", unverified)
elif selection == 5:
    print("Enter the username of the account you would like to spoof with: ")
    username = input()
    print("Enter the password of the account you would like to spoof with: ")
    password = input()
    client.login({"login": str(username),"password": str(password)})
    print("Valid account. Enter the number of seconds you would like the run to take: ")
    seconds = int(input())
    os.system('cls')
    with open("<insert your directory>\\tracks.txt", "r") as tracks:
        length = len(tracks.readlines())
    with open("<insert your directory>\\tracks.txt", "r") as tracks:
        progress = 1
        for trackID in tracks:
            os.system('cls')
            print("Progress: ", progress, "/", length)
            track = getTrack(str(trackID).strip("\n"))
            print("Track: ", track.title)
            client.registerTime(tid=trackID, seconds=seconds, uid=6307499, code={"up_down":[0],"up_up":[1]})
            progress += 1
else:
    print("Error | Error Code 1")

time.sleep(100)
    
