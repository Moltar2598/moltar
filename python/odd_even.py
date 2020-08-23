from itertools import permutations
low = int(input())
high = int(input())
k = int(input())
lst = []
for i in range(low,high + 1):
    lst.append(i)
perm = permutations(lst,k) 
print(list(perm))

for i in list(perm):
    s = 0
    for j in range(0,k):
        s = i[j] + s
    if s%2 == 0:
        lst.append(i)
print(len(lst))