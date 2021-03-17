count = 0
a_set=[1,2,3,4]
for i in a_set:
    for j in a_set:
        for k in a_set:
            if i != j and i!=k and j!=k:
                count = count+1
                print(i,j,k,end='')
                print()
print("共有",count,"个互不相同且无重复数字的三位数")
