import requests
import json
import getter
import printcolor

def main():
    r = None
    while (r==None):
        r = getter.fetch(input("League:"),getter.filter(input("Item Type:")))
    c = json.loads(r[0].text)
    if r[1]:
        flipvalue = [((l["chaosEquivalent"]-l["receive"]["value"])) for l in c["lines"]]
    else:
        flipvalue = [(l["chaosValue"])+(l["chaosValue"])*(l["sparkline"]["totalChange"]/100) for l in c["lines"]]
    names = [(c["lines"][i]["detailsId"]) for i in range(len(c["lines"]))]
    flipvalue.sort()
    flipvalue.reverse()
    for i in range(len(flipvalue)):
        if flipvalue[i]>0:
            print(printcolor.colors.blue, flipvalue[i],end="")
        else:
            print(printcolor.colors.red, flipvalue[i],end="")
        print(printcolor.colors.pink, names[i],end="\n")
main()