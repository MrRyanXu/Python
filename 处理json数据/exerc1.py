'''
要求从键盘输入一段文字，并将用户输入的文字输出保存在“D:\hello.txt”文件中
'''
fname = input("请输入你想写入的文字：")
fo = open("D:\\hello.txt", "w+")
fo.writelines(fname)
fo.seek(0)
for line in fo:
    print(line)
fo.close()
