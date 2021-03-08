# coding:utf-8
# python_lesson11_迭代器和生成器
# author：Qinyuan

#同时迭代 key、value
source = {'age':21, 'name':"qinyuan", 'gender':"boy"}
for key,value in source.items():
    print(key,value)

#判断对象是否可迭代
from collections.abc import Iterable
print(isinstance('qinyuan',Iterable)) #输出为True——可迭代
print(isinstance([1,2,3],Iterable))  #输出为True——可迭代
print(isinstance({'age':21,'name':'qinyuan'},Iterable)) #输出为True——可迭代
print(isinstance(21,Iterable)) #输出为False为不可迭代对象

#将可迭代对象加上索引号
source = {'age':21, 'name':"qinyuan", 'gender':"boy"}
for key,value in enumerate(source.items()):
    print(key,value)

###########
### 例1 ###
l = [1,2,3,4]
die = iter(l)
print('next输出: %d' % next(die))
print('for输出：')
for i in die:
    print(i, end="")

###########
### 例2 ###
import sys         #引入sys模块
li=[1,2,3,4]
di = iter(li)      #创建迭代器对象
while True:
    try:
        print(next(di))
    except StopIteration:
        sys.exit()

###########
### 例3 ###
class Number:
    def __iter__(self):
        self.num=1
        return self
    def __next__(self):
        x = self.num
        self.num += 1
        return x
myclass = Number()
my = iter(myclass)
for i in range(5):
    print(next(my))

###########
### 例4 ###
class Number1:
    def __iter__(self):
        self.num=1
        return self
    def __next__(self):
        if self.num <= 10:
            x = self.num
            self.num += 1
            return x
        else:
            raise StopIteration
myclass = Number1()
my = iter(myclass)
for i in my:
    print(i)

####创建生成器
g = (x*x for x in range(10))
print('第一个：',next(g))
print('for循环next输出：',end=" ")
for i in range(3):
    print(next(g),end=" ")
print('\nfor循环遍历g:',end=" ")
for x in g:
    print(x,end=" ")

###########
### 例5 ###
import sys
def fibonacci(n):   #生成器函数——斐波拉契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n): 
            return
        yield a
        a, b = b, a + b
        counter += 1
f = fibonacci(10)   #f是一个迭代器，由生成器返回生成
print('斐波拉契前10个数是：',end=" ")
while True:
    try:
        print (next(f), end=" ")
    except StopIteration:
        sys.exit()
