def alg(s):
    while '111' in s or '222' in s:
        if '111' in s:
            s = s.replace('111','22',1)
        else:
            s = s.replace('222','11',1)
    return s
def task(index):
    s = '1'*(index+1)+'2'+'1'*(202-index)
    return alg(s)
maxlen = 0
for i in range(-1,203):
    maxlen = max(maxlen,len(task(i)))
print(maxlen) #7