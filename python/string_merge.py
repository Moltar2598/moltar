ls = input()    # large string 
nss= int(input()) #no. of small strings
s = []
for i in range(0,nss):
    s.append(input()) #small string
ls = ls.replace(' ','')
ls = sorted(ls)
s = sorted(s)
sep = ""
print(ls)
s = sep.join(s)
print(s)
s=sorted(s)
print(s)

if ls == s:
    print('Yes')
else:
    print('No')