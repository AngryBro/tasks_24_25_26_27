F = [1,1]
while F[-1]+F[-2]<100:
    F.append(F[-1]+F[-2])
F.pop(0)
starValues = [str(i) for i in range(10)]+['']
numbers = []
for star in starValues:
    for f1 in F:
        for f2 in F:
            number = int('73'+star+'5'+str(f1)+'486'+str(f2))
            if number<=10**9 and number%43==0:
                numbers.append(number)
numbers.sort()
for i in numbers:
    print(i,i//43)    

# 73584868 1711276
# 734514863 17081741
# 735554861 17105927
# 735554861 17105927
# 735894862 17113834
# 737524863 17151741
