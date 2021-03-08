# coding:utf-8
# python_lesson9_循环语句
# author：Qinyuan

###########
### 例1 ###
n=eval(input('请输入1~100的数字n='))
sum = 0
while n > 0:
    sum = sum + n
    n -= 1 
print('1~n的和为sum=%d' % sum )

###########
### 例2 ###
name = "qinyuan"
for i in name :
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        print("%s为元音字母" % i )
    else:
        print('%s不是元音字母' % i)
else: print('已输出完')

###########
### 例3 ###
name = ['Q','T','Y','S']
for i in range(len(name)):
    print(i, name[i])

###########
### 例4 ###
n = 2
while n:
    print("#### while无限循环 ####")
    for i in range(10):
        if i==6:
            print("#### break跳出循环体 ####")
            break
        elif (i%2)==0:
            print(i,"continue结束本次循环")
            continue
        elif (i%2)==1:
            print("执行for循环体")
    n -= 1

###########
### 例5 ###

name = "qinyuan"
for i in name :
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        pass
    else:
        print('当前字母：%s' % i)
else: print('已输出完')
