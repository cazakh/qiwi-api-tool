import QiwiMaster
#API FROM TO
f = open("config.txt", 'r')
n = int(f.readline() )- 1
otstup = "    "

getFrom = list(map(str, f.readline().strip().split(' ')))
for i in range(0, n):
    putTo = list(map(str, f.readline().strip().split(' ')))
    print(putTo)
    j = open("config.json", 'w+')
    j.write('{')
    j.write("\n" + otstup + '"' + "main-token" + '"' + " : " + '"' + getFrom[0] + '"' + ',')
    j.write("\n" + otstup + '"' + "main-number" + '"' + " : " + '"' + getFrom[1] + '"' + ',')
    j.write("\n" + otstup + '"' + "number-client" + '"' + " : " + '"' + putTo[1] + '"')
    j.write("\n}")
    j.close
    getFrom = putTo
    QiwiMaster.summa()
