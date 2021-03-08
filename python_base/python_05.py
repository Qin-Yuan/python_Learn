# coding:utf-8
# python_lesson5_列表
# author：Qinyuan

#列表
num=['0','1','2','1']
#下标查询
print(num.count('1'))
#列表数据个数计算
print(len(num))
##########  数据添加  ###########
# 1、append()
#单个数据
num.append('34') #添加一个数据
print(num)
#数据序列
num.append(['55','66'])  #添加多个数据
print(num)
# 2、extend()
num.extend('34')
print(num)
num.extend(['55','66']) #这时就可以将序列中的数据依次添加了
print(num)
# 3.insert()
num.insert(1,'qinyyuan')
print(num)

########### 删除 ########
#del()
num=['1','2','3']
del num
#print(num)  #删除列表​
#报错：NameError: name 'num' is not defined
num=['1','2','3']
del num[1]
print(num)
#pop()
num=['1','2','3']
pop_num=num.pop(1)
print(pop_num)
print(num)
#remove()
num=['1','2','3']
num.remove('2')
print(num)
num.clear()
print(num)

########## 修改 #############
#赋值修改
num=['1','2','3']
num[1]='4'
print(num)
#reverse()——逆置
num=['1','2','3']
num.reverse()
print(num)
#sort()——排序
num=['23','324','2']
num.sort()
print(num)
num.sort(reverse=True)
print(num)
#copy()——复制
num=['1','2','3']
copy_num=num.copy()
print(num)
print(copy_num)
#列表嵌套
num=[['1','2'],['3','4']]
print(num)
print(num[0])
print(num[1])
print(num[1][1])
