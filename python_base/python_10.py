# coding:utf-8
# python_lesson10_函数
# author：Qinyuan

###########
### 例1 ###
def max(a,b):
    if a>b:
        return a
    else:
        return b
def sr():
    a = eval(input("请输入第一个数字a="))
    b = eval(input("请输入第二个数字b="))
    c=max(a,b)
    print('最大数为%d'%c)
sr()

###########
### 例2 ###
def change(a):
    print(id(a))   # 指向的是同一个对象
    a=10
    print(id(a))   # 一个新对象
a=1
print(id(a))
change(a)

###########
### 例3 ###
def kb(num):
    num.append([1,2,3])
    print ("函数内: ", num)
    return

# 调用changeme函数
num = [1,2,3]
kb( num )
print ("函数外: ", num)

###########
### 例4 ###
def shuchu( arg1, *args_tuple ):
   print ("输出: ")
   print (arg1)
   for arg in args_tuple:
      print (arg)
   return
# 调用shuchu函数
shuchu( 1 )
shuchu( 1,11,'qinyuan')

###########
### 例5 ###
def shuchu1( arg1, **args_dict):
   print ("输出: ")
   print (arg1)
   print (args_dict)
   return
# 调用shuchu函数
shuchu1( 1 )
shuchu1( 1,num = 11,name = 'qinyuan')

###########
### 例6 ###
sum = lambda a,b:a+b
# 调用sum函数
print("1+2=", sum(1,2))
