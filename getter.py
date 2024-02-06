import requests

def currency(league, trade):
    r = requests.get(F'https://poe.ninja/api/data/currencyoverview?league={league}&type={trade}')
    return(r)