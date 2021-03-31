import string
# x为flag，用于终止循环
x = 1
#验证ID合法性函数
def checkId(id):
    #验证长度
    if len(id)>8 or len(id)==0:
        print("ID长度不符合要求!")
        inputInfo('id')
    #尝试输出rule看看是个啥
    rule = string.ascii_letters + string.digits + '_'
    for i in id:
        if not i in rule:
            print("只能由数字、字母、下划线组成！")
            inputInfo('id')
    # if not id.isalnum():
    #     print("只能由数字、字母、下划线组成！")
    #     inputInfo('id')
    print("ID输入正确:{}".format(id))
    inputInfo('email')



#验证email合法性函数
def checkEmail(email):
    #验证email地址,首先判断是否包含了@和.两种格式字符，再判断特殊字符@和.是否大于2
    if not ('@' in email and '.' in email) or email.count('@')>=2 or email.count('.')>=2:
        print('不符合email地址规则')
        inputInfo('email')
    #截取用户名
    pos = email.find('@')
    email_head =email[0:pos]
    #判断用户名是否存在非法字符,在学习列表之前先用空格、‘%’、‘*’作为非法字符的依据，之后可以扩展
    if ' ' in email_head or '%' in email_head or '*' in email_head:
        print('用户名存在非法字符')
        inputInfo('email')
    inputInfo('sfz')

#验证身份证合法性函数
def checkSfz(sfz):
    if not sfz.isdigit():
        print("身份证号只能是数字!")
        inputInfo('sfz')
    if len(sfz) != 18:
        print("身份证长度不符合要求!")
        inputInfo('sfz')
    inputInfo('name')

#验证姓名合法性函数
def checkName(name):
    if len(name) > 4:
        print('名字最多4位!')
        inputInfo('name')
        return
    for ch in name:
        if not '\u4e00' <= ch <= '\u9fff':
            print("名字只能是中文")
            inputInfo('name')
    #在函数中使用global，将临时变量改变为全局变量，要不然里面的x和外面的是两个不同变量
    global x
    x = 0
    print('Great')

def inputInfo(type):
    while x!=0:
        if type == 'id':
            id = input("请输入ID号:")
            checkId(id)
        if type == 'email':
            email = input("请输入email地址:")
            checkEmail(email)
        if type == 'sfz':
            sfz = input("请输入18位身份证号:")
            checkSfz(sfz)
        if type == 'name':
            name = input("请输入4位以内的中文字符:")
            checkName(name)
#这里才是程序入口
inputInfo('id')