#Универсальное решение:

def programs(functions,numbers,no = []):
    def simplePrograms(start,number,functions,no):
        d = {i:0 for i in range(start,number+(1 if number>=start else -1),1 if number>=start else -1)}
        d[start] = 1
        for i in range(start,number+1,1 if number>=start else -1):
            if i in no: d[i] = 0
            for f in functions:
                if f(i)<=number and number>=start or f(i)>=number and number<=start:
                    d[f(i)] += d[i]
        return d[number]
    k = 1
    for i in range(len(numbers)-1):
        k *= simplePrograms(numbers[i],numbers[i+1], functions, no)
    return k

print(programs([lambda x: x-3,lambda x: x//2], [108,42,12])) #30

#Классическое решение:

def f(a,b):
    #0
    d = {i:0 for i in range(a,b-1,-1)}
    #1
    d[a] = 1
    #2
    for i in range(a-1,b-1,-1):
        d[i] = (d[i+3] if i+3<=a else 0) + (d[i*2] if i*2<=a else 0) + (d[i*2+1] if i*2+1<=a else 0)
    #3
    return d[b]
print(f(108,42)*f(42,12)) #30

#Динамическое программирование:

# 0. Определение: d[i] - количество программ получить из a число i
# 1. Стартовые значения: d[a] = 1
# 2. Шаг динамики: i могло быть получено из i+3, i*2, i*2+1, поэтому сумма количество
#     программ для них будет равна количеству программ для i, условно 
#         d[i] = d[i+1]+d[i*2]+d[i*2+1]
# 3. Ответ: d[b]