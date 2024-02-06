import requests
import json
import getter

def main():
    r = None
    while (r==None):
        l = input("League:")
        t = input("Item Type:")
        r = getter.fetch(l,getter.filter(t))
    c = json.loads(r[0].text)
    if r[1]:
        flipvalue = [((c["lines"][i]["chaosEquivalent"]-c["lines"][i]["receive"]["value"]),(c["lines"][i]["detailsId"])) for i in range(len(c["lines"]))]
        flipvalue.sort()
        flipvalue.reverse()
        for i in flipvalue:
            print(i)
    else:
        pass
main()