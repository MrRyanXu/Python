'''
要求用户输入整数，以递归的形式完成斐波拉契数列的计算。
1,1,2,3,5,8,13
'''
def fib(n):
    if n < 3:
        return 1
    else:
        return fib(n-1) + fib(n-2)
num = eval(input("请输入您需要输出的斐波那契数列的个数："))
if num < 3:
    print("请输入大于3的整数！")
else:
    print("斐波那契数列为：")
    for i in range(num):
        print(fib(i+1))