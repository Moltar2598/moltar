# merging two lists of strings 
# while eliminating duplicates 
class Pop:
    def merge(name1,name2):
        var = []
        for i in name1:
            for j in name2:
                if i==j:
                    if i not in var:
                       var.append(i)
                if i != j:
                    if str(i) not in var:
                        var.append(i)
                    if str(j) not in var:
                        var.append(j)
        return var
name1 = ['top','lin','ren']
name2 = ['ben','ren','hen']
merge = Pop.merge(name1,name2)
print(merge)