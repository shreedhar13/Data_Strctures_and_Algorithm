Graph={
    'A':[('B',6),('C',12)],
    'B':[('A',6),('D',3),('E',5)],
    'C':[('A',6),('D',3),('E',2)],
    'D':[('B',3),('F',4),('C',3)],
    'E':[('C',2),('B',5),('F',1)],
    'F':[('D',4),('E',1)]
}

H_dist={
    'B':10,
    'C':12,
    'D':5,
    'E':4,
    'F':0
}

def heuristic(n):
    return H_dist[n]
def neighbours(n):
    nighbours=Graph[n]
    l=[]
    for neighbour in len(nighbours):
        l.append(nighbours[neighbour][neighbour])
    return len

x=Graph['A']
print(x)
