import json
import datetime
import time
import urllib.parse
import requests

today = datetime.datetime.today()
today = today.strftime("%a, %d %b %Y")

lat = 60.45148
lon = 22.26869
n = 7

ONapi = 'http://api.open-notify.org/iss/v1/?'
ISSlocation = 'http://api.open-notify.org/iss-now.json'
astros = 'http://api.open-notify.org/astros.json'

url = ONapi + urllib.parse.urlencode({"lat":lat, "lon": lon,"n":n})
json_data = requests.get(url).json()
json_location = requests.get(ISSlocation).json()
onboard = requests.get(astros).json()

latitude = json_location["iss_position"]["latitude"]
longitude = json_location["iss_position"]["longitude"]

print("This script should print the passing times for International Space Station over Turku, Finland for today")
print("If ISS doesn't pass Turku today, the next pass date and time will be printed instead.")
print("\n")

print("Today is ", today)
print()

json_data = requests.get(url).json()
allpasses = 0
for i in range (0, 6, 1):
    epoch = json_data['response'][i]['risetime']
    ISOtime = datetime.datetime.fromtimestamp(epoch)
    ISOtime = datetime.datetime.isoformat(ISOtime)
    seconds = json_data['response'][i]['duration']
    passtime = round(seconds/60)
    next_pass = time.strftime("%a, %d %b %Y %H:%M:%S %Z", time.localtime(epoch))
    testpass = time.strftime("%a, %d %b %Y", time.localtime(epoch))
    if(testpass != today):
        break
    else:
        print("The next ISS pass will be: ", next_pass, "ISO8061: ", ISOtime)
        print("Duration of this pass is", passtime, "minutes")
        allpasses +=1
if allpasses == 0:
    print("ISS doesn't pass this location today at local time")
    print("The next ISS pass will be: " + (next_pass, "ISO8061", ISOtime))
    print("Duration of this pass is", passtime, "minutes")
else:
    print("Total number of passes today:", allpasses)

print("\n")

print("Current location of ISS is:")
print("Latitude:", latitude)
print("Longitude:", longitude)

print("\n")

totalnum = onboard["number"]
print("Number of people onboard ISS at the moment:", totalnum)
print()
print("Their assigned crafts and names are:")
for i in range (0, totalnum-1, 1):
    print(onboard["people"][i]["craft"])
    print(onboard["people"][i]["name"])
    print()