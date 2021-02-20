f=open(r'C:\Users\bhats\Desktop\pee\p.txt','r')

q=f.readlines()
q=str(q)
q=q[2:-2]
q=q.split('->')

o=open(r'C:\Users\bhats\Desktop\pee\q.txt','w')
for i in q:
    if i==q[-1]:
        o.write(i)
        break
    o.write(i[0])

f.close()
o.close()