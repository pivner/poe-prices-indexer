import requests
import json
import getter

def main():
    r = None
    while (r==None):
        r = getter.fetch(input("League:"),getter.filter(input("Item Type:")))
    c = json.loads(r[0].text)
    flipvalue = [((c["lines"][i]["chaosEquivalent"]-c["lines"][i]["receive"]["value"]),(c["lines"][i]["detailsId"])) for i in range(len(c["lines"]))] if r[1] else [((c["lines"][i]["chaosValue"])*c["lines"][i]["sparkline"]["totalChange"],(c["lines"][i]["detailsId"])) for i in range(len(c["lines"]))]
    flipvalue.sort()
    flipvalue.reverse()
    for i in flipvalue:
        print(i)
main()