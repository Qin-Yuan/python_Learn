# coding:utf-8
# python_lesson12_函数式编程
# author：Qinyuan

##############
#### 例1 #####
#### map() ###
num = [1,2,3,4,5]
def f(x):
    return x*x
l = map(f,num)
print(list(l))

##############
#### 例2 #####
#### reduce()  python2
num = [1,2,3,4,5]
def f(x,y):
    return x*y
l = reduce(f,num)
print(l)

##############
#### 例3 #####
num = [1,2,3,4,5]
def f(x):
    return x%2==1
l = filter(f,num)
print(list(l))

##############
#### 例4 #####
构造生成器，生成从3开始的奇数序列
def f_iter():
    n=1
    while True:
        n+=2       # 不断将n加2
        yield n    # 迭代n
#筛选函数
def f_what(n):
    return lambda x:x%n>0  #匿名函数判断x%n是否有余数
#定义生成器，不断返回下一个素数
def p_iter():
    yield 2  #返回第一个素数2
    num = f_iter()  #利用f_iter返回第一个为3的奇数序列
    while True:
        n = next(num) #返回序列的第一个数
        yield n
        num = filter(f_what(n),num) #构造新序列
#执行函数，并设置范围
for n in p_iter():
    if n<100:
        print(n,end=" ")
    else:
        break

##############
#### 例5 #####
from operator import itemgetter
tup = [('d',95),('a',85),('c',93),('b',100)]
# 按名字从小到大排序
print('名字从小到大：',sorted(tup,key=itemgetter(0)))
# 按数值从小到大排序
print('数值从小到大：',sorted(tup,key=lambda t:t[1]))
# 按数值从小到大排序
print('数值从大到小：',sorted(tup,key=itemgetter(1),reverse=True))

##############
#### 例6 #####
导入库函数
import functools
#创建新函数
int2 = functools.partial(int , base = 2)
#字符串转换
print(int2("10000001"))
print(int2("11111111"))

##############
#### 例7 #####
将sum求和函数赋值给add变量
add = sum
#通过变量名add调用求和函数；注意sum()里面为列表形式传入
print(add([1,2,3,4,5]))
#输出原函数名
print(add.__name__)

##############
#### 例8 #####
装饰器函数
def name(func):    #传入函数参数
    # 返回函数wrapper
    def wrapper(*args,**kw):
        # 输出函数名    
        print("函数名：%s"%func.__name__)
        # 返回传入函数
        return func(*args,**kw)
    # 返回函数wrapper并执行
    return wrapper
# 放置在add函数前，用于执行前输出函数名
@name
def add():
    print("Benny") # 输出
# 执行函数
add()

##############
#### 例9 #####
import functools
def name(str1):
    def decorator(func):
        @functools.wraps(func)  #作用：wrapper.__name__=func.__name__
        def wrapper(*args,**kw):
            print("%s"%str1)
            print("函数名：%s"%func.__name__)
            return func(*args,**kw)
        return wrapper
    return decorator
@name("覃原")
def add():
    print("Benny")
add()
print(add.__name__)
