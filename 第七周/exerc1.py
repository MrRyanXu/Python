'''
幼儿园体检要对小朋友们的体重做评估，对超出平均体重的小朋友需要提示他们进行锻炼。
编程实现：输入若干个体重，输出比平均体重更重的那些体重。输入输出形式见示例说明。
'''
#输入体重，以逗号隔开
weight = eval(input("请输入体重（以逗号隔开）："))
#计算平均体重
s = 0
n = list(weight)
for i in weight:
    s = s + i
x = s / len(n)
for m in n:
    if m > x:
        print(m , end=' ')