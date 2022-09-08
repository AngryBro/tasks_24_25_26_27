#Программно:

def f(n):
    d = [1 for i in range(n+1)]
    for i in range(4,n+1):
        if i%2==0:
            d[i] = d[i-1]+d[i-2]+d[i-3]
    return d[n]
print(f(2008)-f(2006)) #2

#Аналитически:

# f(2008) = f(2006)+f(2007)+f(2005)
# f(2008)-f(2006) = f(2007)+f(2005) = 1+1=2