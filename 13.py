import itertools
def isRoute(gr,s):
    for i in range(len(s)-1):
        if s[i+1] not in gr[s[i]]: return 0
    return 1

graph = {
    'а':['б'],
    'б': ['з','в'],
    'в': ['г'],
    'г': ['д','ж','з'],
    'д': ['е','ж','а'],
    'е':['и','а'],
    'ж':['а','з'],
    'з':['в','а'],
    'и':['а']
}


count = 0
towns = ''.join(list(graph.keys())).replace('ж', '')
for length in range(2,len(graph)):
    perms = itertools.permutations(towns,length)
    perms = [''.join(i) for i in perms]
    for route in perms:
        if isRoute(graph, 'ж'+route+'ж'):
            count += 1
print(count) #8

