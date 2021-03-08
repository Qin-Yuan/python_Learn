# coding:utf-8
# python_lesson4_字符串与编码
# author：Qinyuan

#4.2-bytes类型
ty=type(b'qinyuan')
print(ty)
# 下面为错误写法，bytes里不得含有ASCII编码外字符
# name=b'覃原'

#4.3 str转为 bytes
name = '覃原'
utf=name.encode('utf-8')
print(utf)

#4.4 bytes转为str
utf = b'\xe8\xa6\x83\xe5\x8e\x9f'
name=utf.decode('utf8')
print(name)

#函数扩展
n=ord('覃') #获取字符的十进制表示
print(n)
n=chr(35203) #将十进制数转为字符
print(n)

#字符串格式化输出
# %
age = 21
name = '覃原'
weight= 60.50
student_id=1
print('我的名字是%s' % name)
print('我的学号是%04d' % student_id)
print('我的年龄是%d' % age)
print('我的体重是%.2f公斤'%weight)
# %输出
print('我的学号是%04d,名字%s,年龄%d,体重%.2f'%(student_id,name,age,weight))
# format输出
print('我的学号是{0:04d},名字{1},年龄{2},体重{3:.2f}'.format(student_id,name,age,weight))
# f-格式化字符串
print(f'我的学号是{student_id:04d},名字{name},年龄{age},体重{weight:.2f}')
