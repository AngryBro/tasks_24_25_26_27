a = [sorted([int(j) for j in i.split(';')]) for i in open('files/n9.csv').read().splitlines()]
count = 0
for row in a:
    if len(row)==len(set(row)) and sum(row)>=3*sum(row[2:4]):
        count += 1
print(count) #2097