data = open("data.csv", "r")
time = data.readline()[:-1]
time = time.split(",")[::-1]
for i in range(len(time)-1):
    if "年" in  time[i]:
        time[i] = time[i][:-1]

data_all = []
for i in data:
    i = i[:-1]
    i = i.split(",")[::-1]
    for n in range(len(i)):
        if i[n] == "":
            i[n] = "0"
    data_all.append(i)

output = "name,type,value,date\n"
for i in range(len(data_all)):
    for n in range(len(data_all[i])-1):
        out = data_all[i][-1] + ",," + data_all[i][n] + "," + time[n] + "\n"
        output += out

outputfile = open("output.csv",'w+')
print(output,file=outputfile)
outputfile.close()