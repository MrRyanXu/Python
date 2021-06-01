'''
要求用户输入身高、体重，请根据BMI公式（体重除以身高的平方）计算BMI指数，并根据BMI指数进行以下判断。
低于18.5：过轻
18.5-25：正常
25-28：过重
28-32：肥胖
高于32：严重肥胖
'''
height = eval(input("请输入您的身高（米）："))
weight = eval(input("请输入您的体重（KG）："))
BMI = weight/(height**2)
print("BMI数值为：{:.2f}".format(BMI))
result = ""
if BMI < 18.5:
    result = "过轻"
elif 18.5 <= BMI < 25:
    result = "正常"
elif 25 <= BMI < 28:
    result = "过重"
elif 28 <= BMI < 32:
    result = "肥胖"
else:
    result = "严重肥胖"
print("BMI指标为：{}".format(result))