def minPosminTps(begin,end,elem,exept=[]):
    mintps = -float('inf')
    for i in range(begin[0],end[0]+1):
        for j in range(begin[1],end[1]+1):
            if [i,j] not in exept and a[i][j]==elem:
                mintps = max(mintps,b[i][j])
    return mintps
def minElem(begin,end,exept=[]):
    m = float('inf')
    for i in range(begin[0],end[0]+1):
        for j in range(begin[1],end[1]+1):
            if [i,j] not in exept and a[i][j]<m:
                m = a[i][j]
    return m

a = [[int(j) for j in i.split(';')] for i in open('files/n18l1.csv').read().splitlines()]
b = [[0 for j in range(len(a[0]))] for i in range(len(a))]

for i in range(2,8):
    el = minElem([0,0], [i-2,0])
    if el<=a[i-1][0]:
        b[i][0] = minPosminTps([0,0], [i-2,0], el)+1
    else:
        b[i][0] = b[i-1][0]
b[8][0] = minPosminTps([0,0], [6,0], minElem([0,0], [6,0]))+1
for i in range(9,15):
    el = minElem([0,0], [i-2,0])
    if el<=a[i-1][0]:
        b[i][0] = minPosminTps([0,0], [i-2,0], el)+1
    else:
        b[i][0] = b[i-1][0]
for i in range(2,7):
    el = minElem([0,0], [0,i-2])
    if el<=a[0][i-1]:
        b[0][i] = minPosminTps([0,0], [0,i-2], el)+1
    else:
        b[0][i] = b[0][i-1]
b[0][7] = minPosminTps([0,0], [0,5], minElem([0,0], [0,5]))+1
for i in range(8,15):
    el = minElem([0,0], [0,i-2])
    if el<=a[0][i-1]:
        b[0][i] = minPosminTps([0,0], [0,i-2], el)+1
    else:
        b[0][i] = b[0][i-1]
for i in range(1,8):
    for j in range(1,7):
        el = minElem([0,0], [i,j],[[i,j],[i-1,j],[i,j-1]])
        if el<=min(a[i][j-1],a[i-1][j]):
            b[i][j] = minPosminTps([0,0], [i,j],el,[[i,j],[i-1,j],[i,j-1]])+1
        elif a[i-1][j]<a[i][j-1]:
            b[i][j] = b[i-1][j]
        elif a[i-1][j]>a[i][j-1]:
            b[i][j] = b[i][j-1]
        else:
            b[i][j] = max(b[i-1][j],b[i][j-1])
    el = minElem([0,0], [i,7],[[i,7],[i-1,7],[i,6]])
    if el<=a[i-1][7]:
        b[i][7] = minPosminTps([0,0], [i,7],el,[[i,7],[i-1,7],[i,6]])+1
    else:
        b[i][7] = b[i-1][7]
for i in range(1,8):
    for j in range(8,15):
        el = minElem([0,0], [i,j],[[i,j],[i-1,j],[i,j-1]])
        if el<=min(a[i][j-1],a[i-1][j]):
            b[i][j] = minPosminTps([0,0], [i,j],el,[[i,j],[i-1,j],[i,j-1]])+1
        elif a[i-1][j]<a[i][j-1]:
            b[i][j] = b[i-1][j]
        elif a[i-1][j]>a[i][j-1]:
            b[i][j] = b[i][j-1]
        else:
            b[i][j] = max(b[i-1][j],b[i][j-1])
for j in range(1,7):
    el = minElem([0,0], [8,j],[[8,j],[7,j],[8,j-1]])
    if el<=a[8][j-1]:
        b[8][j] = minPosminTps([0,0], [8,j],el,[[8,j],[7,j],[8,j-1]])+1
    else:
        b[8][j] = b[8][j-1]
b[8][7] = minPosminTps([0,0], [8,7], minElem([0,0], [8,7],[[8,7],[7,7],[8,6]]),[[8,7],[7,7],[8,6]])+1
for j in range(8,15):
    el = minElem([0,0], [8,j],[[8,j],[7,j],[8,j-1]])
    if el<=a[8][j-1]:
        b[8][j] = minPosminTps([0,0], [8,j],el,[[8,j],[7,j],[8,j-1]])+1
    else:
        b[8][j] = b[8][j-1]
for i in range(9,15):
    for j in range(1,7):
        el = minElem([0,0], [i,j],[[i,j],[i-1,j],[i,j-1]])
        if el<=min(a[i][j-1],a[i-1][j]):
            b[i][j] = minPosminTps([0,0], [i,j],el,[[i,j],[i-1,j],[i,j-1]])+1
        elif a[i-1][j]<a[i][j-1]:
            b[i][j] = b[i-1][j]
        elif a[i-1][j]>a[i][j-1]:
            b[i][j] = b[i][j-1]
        else:
            b[i][j] = max(b[i-1][j],b[i][j-1])
for i in range(9,15):
    el = minElem([0,0], [i,7],[[i,7],[i-1,7],[i,6]])
    if el<=a[i-1][7]:
        b[i][7] = minPosminTps([0,0], [i,7],el,[[i,7],[i-1,7],[i,6]])+1
    else:
        b[i][7] = b[i-1][7]
for i in range(9,15):
    for j in range(8,15):
        el = minElem([0,0], [i,j],[[i,j],[i-1,j],[i,j-1]])
        if el<=min(a[i][j-1],a[i-1][j]):
            b[i][j] = minPosminTps([0,0], [i,j],el,[[i,j],[i-1,j],[i,j-1]])+1
        elif a[i-1][j]<a[i][j-1]:
            b[i][j] = b[i-1][j]
        elif a[i-1][j]>a[i][j-1]:
            b[i][j] = b[i][j-1]
        else:
            b[i][j] = max(b[i-1][j],b[i][j-1])
print(b[14][14])

# мин тп = 5