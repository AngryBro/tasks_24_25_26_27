def alg(n):
    def t2(x):
        if x.count('1')%2==0:
            x = x[1:]
            while x[0]=='0': x = x[1:]
        else:
            x = '1'+x+'00'
        return x
    n = bin(n)[2:]
    n = t2(t2(n))
    return int(n,2)
for n in range(1,1000):
    if alg(n)>100:
        print(n)
        break
#26