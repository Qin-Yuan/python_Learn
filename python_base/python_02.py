# coding:utf-8
# python_lesson2_输入输出
# author：Qinyuan

#code 1
print('hello world')
print('Qinyuan','studies','python')
print('Qinyuan'+' '+' '+'studies'+' '+' python')
print('1'+'day')
print('1 + 2 =',1+2)

#code 2
name=input('please enter your name:')#等待用户输入
print('hello,my name is',name)

#code 3 课后习题
a=int(input('请输入第一个数字:')) #强制类型转换为int型
b=int(input('请输入第二个数字:')) #或者使用eval()(自动类型转换)
print('a + b =',a+b)
