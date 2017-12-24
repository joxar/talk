import urllib.request as req
import json, subprocess

# download JSON data of weather information
id = "130010"   # tokyo
url = "http://weather.livedoor.com/forecast/webservice/json/v1?city=" + id
savename = "weather.json"
req.urlretrieve(url, savename)

# analyze JSON file
data = json.load(open(savename, "r", encoding="utf-8"))
# print(data)
text = data['description']['text']
text = text.replace("\n", "")

# read
def exec(cmd):
    r = subprocess.check_output(cmd, shell=True)
    return r.decode("utf-8").strip()

# read by one statement
lines = text.split("。")
for s in lines:
    if s == "": continue
    print(s)
    exec('./AquesTalkPi "' + s + '" | aplay')

