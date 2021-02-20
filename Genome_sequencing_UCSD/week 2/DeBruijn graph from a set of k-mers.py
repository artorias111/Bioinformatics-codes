from collections import OrderedDict
file=open(r'C:\Users\bhats\Desktop\pee\h.txt','r')

f=file.readlines()
l=[]
for i in f:
    l.append(i.strip())

k={}

for i in l:
    k[i[:-1]]=[]
    k[i[1:]]=[]

od = OrderedDict(sorted(k.items()))

for i in l:
    od[i[:-1]].append(i[1:])

for i in od:
    od[i].sort()

out=open(r'C:\Users\bhats\Desktop\pee\o.txt','w')

for i in od:
    od[i]=str(od[i])
    od[i]=od[i][1:-1]
    od[i]=od[i].replace(", ",",")
    od[i]=od[i].replace("'","")


for i in od:
    if od[i]=="":
        continue
    out.writelines(i+' -> '+od[i]+'\n')

file.close()
out.close()