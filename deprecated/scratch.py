import json
with open("pref.json", "r") as rw_file:
    data = json.load(rw_file)
    print(data)