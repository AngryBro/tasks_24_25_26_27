Z = 9+26
Y = Z-1
X = Y-1
def ZaYX(a): return Z*55**3+a*55**2+Y*55+X
def _2XaY(a): return 2*55**3+X*55**2+a*55+Y
def expression(a): return ZaYX(a)-_2XaY(a)
aa = []
for a in range(44):
    if expression(a)%29==0: aa.append(a)
mina = min(aa)
maxa = max(aa)
print(abs(expression(mina)-expression(maxa))) #0

