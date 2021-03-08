# coding:utf-8
# python_lesson3_数据类型和变量
# author：Qinyuan

# 1.1 整数
print(1000,-100)

# 1.2 浮点数，以及科学计数法的表示方法
print(12.435,1.3*10**3,1.3e3,1.3*10**-3,1.3e-3)
#可以看到科学计数法用e表示底数10时浮点类型存在误差，整数时完全相等的为True
b=(1.3*10**3==1.3e3)  #判断数值是否相等，完全相等返回True,不相等返回False
a=(1.3*10**-3==1.3e-3)
print(a,b)

# 1.3 字符串
print("I'm ok.")
# 转义字符 \
print('I\'m ok.')
# \t：制表符
# \n: 换行符
# 字符串前加 r:表示字符串默认不转义
print('\\\t\\')
print(r'\\\t\\')
# 多行字符输出
print('''line1
line2
line3''')
# 多行字符串'''...'''前加 r
print(r'''hello,\n
world''')

# 1.4 布尔值：True / Fales
#年龄判断
age=eval(input('请输入年龄：'))  #用eval()类型转换
if age >= 18:
    print('adult')
else:
    print('teenager')

#！作业练习
n = 123
f = 456.789
s1 = 'Hello, Qinyuan'
s2 = 'Hello, \'Qinyuan\''
s3 = r'Hello, "Qinyuan"'
s4 = r'''Hello,
Qinyuan!'''
print(n,f,s1,s2,s3,s4)
