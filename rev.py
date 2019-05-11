
def comp(seq):
    comp_dict = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    seq_comp = ""
    for char in seq:
        if char in comp_dict:
            seq_comp += comp_dict[char]
        else:
            seq_comp += '?'
    return seq_comp

def rev(seq):
    seq_rev = ""
    ln = len(seq) - 1
    while ln > -1:
        seq_rev += seq[ln]
        ln -= 1
    return seq_rev

def rev_comp(seq):
    tmp = comp(seq)
    return rev(tmp)

src = input("DNA sequence : ")
cnvt = int(input("1(comp), 2(Rev), 3(Rev_Comp): "))
if (cnvt >= 1 and cnvt <= 3):
    if (cnvt == 1):
        rst = comp(src)
    elif (cnvt == 2):
        rst = rev(src)
    else:
        rst = rev_comp(src)
    print(src, "->", rst)
else:
    print("1(comp), 2(Rev), 3(Rev_Comp)!!")
