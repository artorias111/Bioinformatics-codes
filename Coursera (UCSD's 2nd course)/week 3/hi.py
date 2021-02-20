AA = ['G', 'A', 'S', 'P', 'V', 'T', 'C', 'I', 'L', 'N', 'D', 'K', 'Q', 'E', 'M', 'H', 'F', 'R', 'Y', 'W']
AAM=[ 57, 71, 87, 97, 99, 101, 103, 113, 113, 114, 115, 128, 128, 129, 131, 137, 147, 156, 163, 186]

k={}
for i in range(len(AA)):
    k[AA[i]]=AAM[i]

def lees(s,k):
#s='LEQN'
    pm=[]
    pm.append(0)
    m=0
    for i in s:
        m+=k[i]
        pm.append(m)

    for i in range(len(s)):
        for j in AA:
            if j==s[i]:
                pm[i]=pm[i-1]+k[j]

    ls=[0]
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            ls.append(pm[j]-pm[i])
        

    lss=[]
    for i in ls:
        if i<0:
            i*=-1
        lss.append(i)
    

    lss.sort()
    return lss

s='MTAI'
ppm=lees(s[:-1],k)
pm=lees(s,k)
tm=pm[-1]
c=[]

for i in ppm:
    c.append(tm-i)

for i in c:
    ppm.append(i)
ppm.sort()

o=open(r'C:\Users\bhats\Desktop\Oggle\o.txt','w')
for i in ppm:
    o.writelines(str(i)+' ')

o.close()
