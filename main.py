import json
import getter
import printcolor

def main():
    r = None
    while (r==None):
        r = getter.fetch(input("League:"),getter.filter(input("Item Type:")))
    c = json.loads(r[0].text)
    if r[1]:
        output = [(((l["chaosEquivalent"]-l["receive"]["value"])),(l["detailsId"])) for l in c["lines"]]
    else:
        output = [((l["chaosValue"])*(l["sparkline"]["totalChange"]/100),(l["detailsId"])) for l in c["lines"]]
    output.sort()
    output.reverse()
    for i in range(len(output)):
        if output[i][0]>0:
            print(printcolor.colors.blue, round(output[i][0], 4),end="")
        else:
            print(printcolor.colors.red, round(output[i][0], 4),end="")
        print(printcolor.colors.pink, output[i][1],end="\n")
main()
