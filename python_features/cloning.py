import copy

l = [1,2,3,44, ["dddd"], [0, [1]], []]
s = copy.deepcopy(l)
d = copy.copy(l)
v = l[:]
print(s)
print(d)
print(v)