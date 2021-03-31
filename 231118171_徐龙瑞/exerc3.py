'''
系统随机生成8个1-33的整数形成一注中奖号码，用户在控制台输入8位数字看是否中奖
'''
import random
x=[random.randint(1,33) for i in range(8)]
a = dict.fromkeys(x)
b = list(a.keys())
print("中奖号码是：{}".format(b))
arr = input("请输入您购买的彩票号码：")
num = [int(n) for n in arr.split()]
print(num)
