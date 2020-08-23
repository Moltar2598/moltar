def forward_prop(var):
    lnth = len(var)
    var2 = []
    for i in range(1,lnth):
        var2.append((var[i]-var[i-1]))
    return var2
def backward_prop(var,var2):
    lnth = len(var)
    lnth2 = len(var2)
    var3 = var[lnth-1] + var2[lnth2 - 1] 
    return var3

seq = [10,37,45,95]
print('seq1 = ',seq)
seq2 = forward_prop(seq)
print('seq2 = ',seq2)
seq3 = forward_prop(seq2)
print('seq3 = ',seq3)
seq4 = forward_prop(seq3)
print('seq4 = ',seq4)

seq3.append(backward_prop(seq4,seq3))
print('seq3 = ',seq3)
seq2.append(backward_prop(seq3,seq2))
print('seq2 = ',seq2)
seq.append(backward_prop(seq2,seq))
print('seq1 = ',seq)