'''
新建CEO类继承员工类，俩个类都实现了 sayHello方法, 在CEO 中的 sayHello方法中调用员工类的 sayHello方法。
'''
class Employee(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sayHello(self):
        print("父类方法\t{},sayHello".format(self.name))

class CEO(Employee):
    sex = ''
    def __init__(self, name, age, s):
        Employee.__init__(self, name, age)
        self.sex = s

    def sayHello(self):
        super(CEO,self).sayHello()

ceo1 = CEO('小明', 20, '男')
ceo2 = CEO('小白',22,'女')

ceo1.sayHello()
ceo2.sayHello()