def task19():
    def game19(s,i):
        m = 10
        yes = s<=m and i==2
        no = s<=m and i<2 or s>m and i==2
        if yes: return 1
        if no: return 0
        return game19(s-10,i+1) or game19(s//3,i+1)
    for s in range(10000,10,-1):
        if game19(s, 0): return s
def task20():
    def p2(s,i):
        m = 10
        yes = s<=m and i==3
        no = s<=m and i<3 or s>m and i==3
        if yes: return 1
        if no: return 0
        if i%2:
            return p2(s-10,i+1) and p2(s//3,i+1)
        else:
            return p2(s-10,i+1) or p2(s//3,i+1)
    ss = []
    for s in range(11,10000):
        if p2(s,0): ss.append(s)
    return [min(ss),max(ss)]
def task21():
    def v1(s,i):
        m = 10
        yes = s<=m and i==2
        no = s<=m and i<2 or s>m and i==2
        if yes: return 1
        if no: return 0
        if i%2:
            return v1(s-10,i+1) or v1(s//3,i+1)
        else:
            return v1(s-10,i+1) and v1(s//3,i+1)
    def v2(s,i):
        m = 10
        yes = s<=m and i in [2,4]
        no = s<=m and i in [0,1,3] or s>m and i==4
        if yes: return 1
        if no: return 0
        if i%2:
            return v2(s-10,i+1) or v2(s//3,i+1)
        else:
            return v2(s-10,i+1) and v2(s//3,i+1)
    count = 0
    for s in range(11,10000):
        if v2(s,0) and not v1(s,0): count+=1
    return count
print('19:',task19())
print('20:',task20())
print('21:',task21())

# 19: 98
# 20: [43, 128]
# 21: 20
    
