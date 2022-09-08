a = [int(i) for i in open('files/n17.txt').read().splitlines()]
a52 = [i for i in a if i%100==52]
dif = max(a52)-min(a52)
sums = []
for i in range(len(a)-1):
    if min(a[i:i+2])<dif and max(a[i:i+2])>=dif:
        sums.append(sum(a[i:i+2]))
print(len(sums),max(sums)) #214 18188