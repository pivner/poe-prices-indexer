import requests
import json
import getter

def main():
    r = 0
    while (r==0):
        l = input("League:")
        t = input("Item:")
        r = json.loads(getter.currency(l,t).text)
    flipvalue = [((r["lines"][i]["chaosEquivalent"]-r["lines"][i]["receive"]["value"]),(r["lines"][i]["detailsId"])) for i in range(len(r["lines"]))]
    flipvalue.sort()
    flipvalue.reverse()
    for i in flipvalue:
        print(i)
main()