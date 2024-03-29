import requests
import json

def filter(strinput):
        return(strinput,True) if strinput == "Currency" or strinput == "Fragment" else (strinput,False)

def fetch(league, trade):
    if trade[1]:
        try:
            r = requests.get(F'https://poe.ninja/api/data/currencyoverview?league={league}&type={trade[0]}')
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
        if "lines" in json.loads(r.text):
            return(r,True)
    else:
        try:
            r = requests.get(F'https://poe.ninja/api/data/itemoverview?league={league}&type={trade[0]}')
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
        if "lines" in json.loads(r.text):
            return(r,False)
    print("League or Item Type does not exist")
    return(None)
