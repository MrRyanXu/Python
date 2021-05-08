'''
”json.txt”文件中有用户的注册信息，先要求：
（1）.读取json.txt中的信息
（2）.为用户编写UserInfo类，对Json数据中的每个对象进行封装
（3）.使用魔术方法__str__可以输出每个用户的基本信息
（4）.将Json数据中所有的用户信息进行数据封装并存入列表中
（5）.遍历列表输出所有的用户信息
'''
import json
class UserInfo:
    _email=''
    _name=''
    _password=''
    _qq=''

    #构造方法
    def __init__(self,email='none',name='no',password='no',qq='no'):
        self._email=email
        self._name=name
        self._password=password
        self._qq=qq

    def __str__(self) -> str:
        return "姓名:{},邮箱:{},密码:{},qq:{}".format(self._name,self._email,self._password,self._qq)

#读取json文件
js=open("json.txt","r")
data=json.load(js)
users=[]
for user in data:
    user= UserInfo(name=user["name"],email=user["email"],password=user["password"],qq=user["qq"])
    users.append(user)
for user in users:
    print(user)