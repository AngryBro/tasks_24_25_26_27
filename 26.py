a = [[int(j) for j in i.split()] for i in open('files/n26'+input()+'.txt').read().splitlines()]
m = a.pop(0)[1]
b = {i[0]:[] for i in a}
for i in a: b[i[0]].append(i[1])
for i in b: b[i].sort()
#0#1
d = {k:[{i:0 for i in b} for j in range(max(b[i])+2)] for k in ['+','-','count']}
#2
for i in b:
    for j in range(2,len(d['-'])):
        if j-1 in b[i]:
            d['-'][j][i] = d['-'][j-1][i]+1
    for j in range(len(d['+'])-2,0,-1):
        if j+1 in b[i]:
            d['+'][j][i] = d['+'][j+1][i]+1
    for j in range(len(d['count'])):
        if j not in b[i]: d['count'][j][i] = d['+'][j][i]+d['-'][j][i]
#3
print(sum([1 for j in range(len(d['count'])) for i in b if d['count'][j][i]>=m]),
max([i for i in b for j in range(len(d['count'])) if d['count'][j][i]>=m]))
#15 1692

# Переструктурирование данных:
#     Ключ: этаж
#     Значение: сортированный массив занятых мест

# Динамическое программирование:

# 0. Определение: d[-][j][i] - количество занятых соседних мест слева от места j на этаже i
#                 d[+][j][i] - аналогично, но справа
#                 d[count][j][i] - количество занятых мест соседних с свободным j на этаже i
#                 j от 1 до максимального занятого места на этаже + 1
# 1. Стартовые значения:
#     всё по нулям
# 2. Шаг динамики: 
#     если j-1 место занято, то d[-][j][i] = d[-][j-1][i]+1, j от 2 до последнего
#     если j+1 место занято, то d[+][j][i] = d[+][j+1][i]+1, j от предпоследнего до 1
#     если место j свободное, то d[count][j][i] = d[-][j][i]+d[+][j][i]
# 3. Ответ: количество мест j на этажах i таких, что d[count][j][i]>=m,
#             максимальный этаж, на котором d[count][j][i]>=m