nodes=[]
sum=[]
start=[]
s=[]
g=[1,2,0,-1]
print('hello')

for i in range(4):
    j=g[i]
    s.append(i)

    temp=i
    node=1

    while s[0] != g[j] :
        
        node+=1
        temp+=g[j]
        
        
    if s[0] == g[j]:
        j=g[j]
        sum.append(temp)
        nodes.append(node)
        start.append(s[0])
        s.pop()
    elif j == -1 :
        s.pop()

print('hello')
print(nodes)
print(sum)
print(start)
print(s)
print('hello')