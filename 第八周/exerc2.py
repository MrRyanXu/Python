'''
读取“xiaofei.csv”文件中的内容，并将“江西”、“甘肃”两省的“衣着”消费支出打印
'''
with open("xiaofei.csv","r") as f:
    cs = f.read()
    ls = cs.split()
    for i in range(len(ls)):
        lim = ''.join(ls[i]).split(',')
        if lim[0]=='江西':
            print("江西衣着消费为：",lim[3])
        if lim[0]=='甘肃':
            print("甘肃衣着消费为：",lim[3])