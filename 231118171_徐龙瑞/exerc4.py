'''
要求系统能随机生成一个由大小写字母组成的4位验证码。
'''
import random
s = ""
for i in range(0,4):
    if random.randint(0,1)==0:
        s = s + chr(random.randint(65,90))
    else:
        s = s + chr(random.randint(97, 122))
print(s)