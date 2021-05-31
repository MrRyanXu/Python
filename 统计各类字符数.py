s = input("请输入一行字符：")
char = 0
space = 0
digit = 0
others = 0
for str in s:
    if str.isalpha():
        char = char + 1
    elif str.isspace():
        space = space + 1
    elif str.isdigit():
        digit = digit + 1
    else:
        others = others + 1
print("这行字符中有",char,"个英文字母，有",space,"个空格，有",digit,"个数字，有",others,"个其他字符。")
