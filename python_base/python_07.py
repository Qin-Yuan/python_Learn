# coding:utf-8
# python_lesson7_字典
# author：Qinyuan

#字典举例
dict={'name': 'qinyuan', 'age':21, 'url':''}
#打印字典中的name部分
print("dict['name']:",dict['name'])
#打印字典中的age部分
print("dict['age']:",dict['age'])
#打印不存在的键值会报错
#print(dict['name1'])

#修改字典中的age
dict['age']=18
#向字典中新加键值
dict['school']='cq'
print(dict['age'],dict['school'])

#删除字典元素
#删除键值
del dict['name']
#print(dict['name'])
print('age:',dict['age'])
#清空字典
dict.clear()
#print(dict['age'])
#删除字典
del dict

#键创建两次
dict = {'name': 'BB', 'name': 'qinyuan'}
print('name:',dict['name'])

#不能用列表命名键
#dict1 = {['name']:'qinyaun' , 'age': 21}
del dict

#len()函数
dict={'name': 'qinyuan', 'age':21, 'url':''}
print('len:',len(dict))

#str()函数
print(str(dict))

#type()函数
print(type(dict))

#clear()函数
dict.clear()
print(len(dict))

#copy()函数
dict={'name': 'qinyuan', 'age':21, 'url':''}
dict1 = dict.copy()
dict2 = dict
dict['url']='www.qinyuan.com'
print(dict)
print(dict1)
print(dict2)

del dict
#fromkeys()函数创建字典
seq = ('name','age','url')
dict = dict.fromkeys(seq)
print('新建字典：%s' % str(dict))
dict = dict.fromkeys(seq,'qinyuan')
print('新建字典：%s' % str(dict))

del dict
#get()函数查找指定键
dict={'name': 'qinyuan', 'age':21, 'url':''}
print('name: %s ' % dict.get('name'))
print('name1: %s ' % dict.get('name1','NO'))

#in 判断键是否存在
dict={'name': 'qinyuan', 'age':21, 'url':''}
print('age' in dict)
print('name1' in dict)

#item()遍历
dict={'name': 'qinyuan', 'age':21, 'url':''}
print(dict.items())

#keys()转换成列表
dict={'name': 'qinyuan', 'age':21, 'url':''}
print(dict.keys())
print(dict.values())

#default(key,default)查找 + 插入
dict={'name': 'qinyuan', 'age':21, 'url':''}
print(dict.setdefault('name')) #查找name的值
print(dict.setdefault('name1', None)) #查找无name1，则插入name1键并赋值为None

#update()更新字典
dict={'name': 'qinyuan', 'age':21, 'url':''}
dict1={'name':'TQQ','school':'CQ'}
dict.update(dict1)
print(dict)

#pop()删除
dict={'name': 'qinyuan', 'age':21, 'url':''}
print(dict.pop('name','NO'))
print(dict.pop('name1','NO'))

#popitem()删除末尾
dict={'name': 'qinyuan', 'age':21, 'url':''}
print(dict.popitem())
print(dict)
