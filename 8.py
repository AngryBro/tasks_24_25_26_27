from itertools import permutations
s = 'АТТЕСТАТ'
perms = permutations(s)
words = [''.join(i) for i in perms]
print(len(set(words)))