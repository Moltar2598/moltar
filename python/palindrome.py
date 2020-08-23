def palindrome(s,lst):
    if s == s[::-1]:
       lst.append(s)
       return lst

n1,n2 = input(),input()
count = 0
lst=[]

for n in range(0,int(n2)-int(n1)+1):
    for h in range(0,24):
        if h<10:
            h = str(0)+str(h)
        for m in range(0,60):
            if m <10:
                m = str(0)+str(m)
            for s in range(0,60):
                
                if s<10:
                    s = str(0)+str(s)
                    p = str(n)+str(h)+str(m)+str(s)
                    palindrome(p,lst) 
                else:
                        palindrome(p,lst)
print(len(lst))
print(lst)

