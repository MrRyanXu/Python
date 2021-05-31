'''
编写一个用户注册小程序，要求用户在控制台输入“ID”、“EMAIL地址”、“身份证号”、“姓名”。要求：
	ID长度不能超过8位，且只能由数字、字母、下划线组成
	EMAIL地址要求符合基本电子邮件格式
	身份证号要求符合基本格式
	姓名只能中文且不能超过4位
	以上操作均不能用正则表达式
验证合法后输出用户的所有信息，要求在信息中体现出性别。
'''
def IsId(Id):
    while True:
            if len(Id) > 8:
                print("用户名长度不能大于8个字符")
                Id = input("请重新输入用户名：")
            for i in Id[0:]:
                #只要有一个字符不符合,便不是合法的变量;alnum表示字母或数字
                if not (Id[0:].isalnum() or Id[0:] in '_'):
                    print("用户名只能由数字、字母、下划线组成")
                    break
                    Id = input("请重新输入用户名：")
            else:
                print("用户名输入正确！")
                break

Id = (input("请输入用户名："))
IsId(Id)
Email = input("请输入邮箱：")
IdCard = input("请输入身份证号码：")
Name = input("请输入姓名：")

