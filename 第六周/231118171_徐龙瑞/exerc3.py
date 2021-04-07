'''
有一个函数“letters”它的作用接收一个字符串参数，
将字符串中的非英文字母剔除，还有一个函数“reverse”它的作用接收一个字符串参数，并将字符串反转。
完成这两个函数的设计，用户在输入一串字符串后先剔除非英文字母的字符再将字符串进行反转输出。
'''
def letters(s1):
    if s1.isalpha() == True:
        return s1
    else:
        return "".join(filter(str.isalpha,s1))
def reverse(s):
    if s == "":
        return s
    else:
        return reverse(s[1:]) + s[0]
str = input("请输入一个字符串：")
print(reverse(letters(str)))