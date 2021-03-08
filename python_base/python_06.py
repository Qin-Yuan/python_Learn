# coding:utf-8
# python_lesson6_元组和集合
# author：Qinyuan

#################### 元组-tuple ################
#多个数据元组
print('###############元组-tuple##############')
t1=(1,2,3)
print(t1)
#定义一个元组
t2=(1,)
print(t2)

#下标查找
print(t1[1])
#函数index()查找
print(t1.index(1))
#count()
t3=(1,1,3,4,'a','a')
print(t3.count(1))
#len()
print(len(t1))
#错误语法，不能改变元组数据
''' 
t1[0]=2
'''
t1 = (1,2,3,[2,4])
t1[3][0]=1
print(t1)

#################### 集合 ################
print('#################### 集合 ################')
s={1,2,'a','f',('a','c',3)}
s1=set('qinyuan')
print(s)
print(s1)
####添加####
#add()
s.add('qinyaun')
s.add('a')
print(s)
##update()
s={1,2,'a','f',('a','c',3)}
s.update('abc')
print(s)
s.update([12,34])
print(s)
####删除####
#remove()
s={1,2,3}
s.remove(2)
print(s)
# 报错
'''
s.remove(4)
'''
#pop()随机删除
s={1,2,3}
pop_date=s.pop()
print(pop_date)
