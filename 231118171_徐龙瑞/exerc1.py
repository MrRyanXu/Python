'''
输入两个整数，打印他们相除后的结果，若输入的不是整数或除数为0，进行异常处理
'''
try:
    a = int(input("请输被除数（整数）：\n"))
    b = int(input("请输入除数（整数）：\n"))
    c = int(a/b)
    print(c)
except ZeroDivisionError:
    print("除数不能为零，请重新输入！")
except ValueError:
    print("请输入整数！")
except:
    print("其他错误")