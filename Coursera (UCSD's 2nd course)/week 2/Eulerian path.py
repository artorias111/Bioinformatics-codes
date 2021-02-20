with open(r'C:\Users\bhats\Desktop\pee\o.txt', 'r') as file:
    graph = dict((line.strip().split(' -> ') for line in file))
    for key in graph:
        graph[key] = graph[key].split(',')

k=graph
l=[]
for i in k:
    l.append(i)
    for j in k[i]:
        l.append(j)

l=list(set(l))
l.sort()

deg={}
for i in l:
    deg[i]=0

x=list(k)

for i in deg:
    if i in x:
        deg[i]=len(k[i])

y=[]
for i in k:
    for j in k[i]:
        y.append(j)

for i in deg:
    if i in y:
        deg[i]=deg[i]-y.count(i)

min,max=0,0
fn,ln='','' #first and last node

for i in deg:
    if deg[i]<=min:
        min=deg[i]
        ln=i
    if deg[i]>=max:
        max=deg[i]
        fn=i
print(ln)
#if ln in k:
    #k[ln].append(fn)
k[ln]=[]
    #k[ln].append(fn)

#k-edges, l- nodeslist
s=[]
path=[]
#nodes-nodes, k-edges
v=fn
s.append(v)
u,w='',''


while(len(s)!=0):
    u=s[-1] 
    if k[u]!=[]:
        w=k[u][0]
        s.append(w)
        k[u].remove(w)
    
    elif k[u]==[]:
        s.pop()
        path.append(u)


path=path[::-1]
st=''
path.append(ln)
for i in path:
    st=st+i+'->' 

st=st.rstrip('->')

out=open(r'C:\Users\bhats\Desktop\pee\p.txt','w')

out.writelines(st[:-26])

file.close()
out.close()