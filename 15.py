def f(x,y,A): return (680*y+256*x<A) or (5*x+3*y>11112)
A = 2518721
flag = 1
for x in range(1000):
    for y in range(1000):
        if not f(x,y,A): flag = 0
if flag:
    print(A)