'''
输入1-12的整数，表示几月份，例如输入4，输出四月份（字符串截取）。
str=一月份二月份三月份四月份五月份六月份七月份八月份九月份十月份十一月十二月
'''
str = "一月份二月份三月份四月份五月份六月份七月份八月份九月份十月份十一月十二月"
month = eval(input("请输入月份（1-12）："))
pos = (month - 1)*3
print(str[pos:pos+3])