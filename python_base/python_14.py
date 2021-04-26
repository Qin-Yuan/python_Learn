# coding:utf-8
# python_lesson14_面向对象
# author：Qinyuan

##############
#### 例1 #####
# 创建一个类对象
class obj_1:
    name = 'Benny'
    # self是方法的第一个参数，表示自身
    def p(self):
        print("关注覃原，一起学习")
# 实例化类
obj_1 = obj_1()
print("类的name是：", obj_1.name )
print("方法输出：", end=' ')
obj_1.p()

##############
#### 例2 #####
# __init()__
class obj_2:
    # self是方法的第一个参数，表示自身
    age = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age
obj_2 = obj_2('Benny',21)
print("name ：%s \nage ：%d"%(obj_2.name,obj_2.age))

##############
#### 例3 #####
# 类的方法
class obj_3:
    def func1(self):
        print("这是一个基本方法")
    def __func2(self):
        print("这是一个私有方法")
    def func3(self):
        print("类调用私有方法：", end='')
        self.__func2()
obj_3 = obj_3()
#调用基本方法
obj_3.func1()
#不能在类外调用私有方法
#obj_3.__func2()  报错：AttributeError: 'obj_3' object has no attribute '__func2'
#在类里面调用私有方法
obj_3.func3()

##############
#### 例4 #####
# 类的变量
class obj_4:
    #基本属性
    name = ''
    #私有属性，前面加两个下划线
    __age = 0
    # self是方法的第一个参数，表示自身
    def __init__(self,name,age):
        self.name = name
        self.__age = age
    def sc(self):
        #通过类的方法输出私有属性
        print(self.__age)
    def get_age(self):
        return self.__age
obj_4 = obj_4('Benny',21)
print("name: %s"%obj_4.name)
#不能在类外访问私有属性
#print("age: %d"%obj_4.__age)  报错：AttributeError: 'obj_3' object has no attribute '__age'
#私有属性访问
print(obj_4._obj_4__age)
#通过函数封装返回私有变量
print(obj_4.get_age())
#类里面输出私有变量
print("age: ",end='')
obj_4.sc()

##############
#### 例5 #####
# 继承
# 定义一个父类，里面定义两个变量和一个方法
class obj_5():
    name = 'qinyuan'
    age = 21
    def sc(self):
        print("这是父类")
# 定义一个子类，继承父类
class obj_5A(obj_5):
    def sc1(self):
        print("这是子类")
#子类实例化
obj_5 = obj_5A()
#输出继承父类的名字
print(obj_5.name)
#调用继承父类的方法
obj_5.sc()
#调用子类的方法
obj_5.sc1()

##############
#### 例6 #####
# 重写
# 定义一个父类，里面定义两个变量和一个方法
class obj_6():
    name = 'qinyuan'
    age = 21
    def sc(self):
        print("这是父类")
# 定义一个子类，继承父类
class obj_6A(obj_6):
    #重写name变量值
    name = 'Benny'
    #重写输出函数
    def sc(self):
        print("这是子类")
#子类实例化
obj_6 = obj_6A()
#输出继承父类重写的name
print(obj_6.name)
#输出继承父类的age
print(obj_6.age)
#调用继承父类的重写的方法
obj_6.sc()

##############
#### 例7 #####
# 多继承
# 创建base1
class base1():
    name = 'qinyuan'
    def sc1(self):
        print(self.name)
class base2():
    age = 23
    def sr2(self):
        print(self.age)
class NEWclass(base1,base2):
    pass
#子类实例化
obj = NEWclass()
# 输出继承父类1的name变量
print(obj.name)
# 调用继承父类2的方法
obj.sr2()
