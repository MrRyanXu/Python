'''
编写一个员工类(Employee), 每次实例化该类后会自动记录+1，要求最后统计输出员工类总共实例化了多少对象。
'''
class Employee(object):
    employee_count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Employee.employee_count += 1

    def display_count(self):
        print("总共实例化了{}个对象".format(Employee.employee_count))

    def display_employee(self):
        print("name：{},age:{}".format(self.name,self.age))

employee1 = Employee('flkhalkdf', 20)
employee2 = Employee('flkl',22)

employee1.display_count()
employee1.display_employee()
employee2.display_employee()






