def trap(x,y): return x<y*3**0.5<8*3**0.5-x and 0<x<2*3**0.5
count = 0
for x in range(10):
    for y in range(10):
        if trap(x, y): count+=1
print(count) #17