a = 0.5
b = 0.165
m = int(input("请输入你的体重（kg）:"))
for i in range(11):
    n = m+a*i
    print(i,"年后你在地球上的体重是：{}".format(n))
    q = n*0.165
    print(i,"年后你在月球上的体重：{}".format(q))