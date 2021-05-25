# coding:utf-8
# python_lesson15_文件
# author：Qinyuan

##############
#### 例1 #####
# 打开文件

# read()
with open(r"F:\USER\Desktop\Benny\benny\python\code\file.txt",'r') as f:
    # 读取文件内容，并输出
    print(f.read())
# 关闭打开的文件
f.close()

# readline()
with open(r"F:\USER\Desktop\Benny\benny\python\code\file.txt",'r') as f:
    # 逐行读取，读到换行字符时停止，输出第一行
    print(f.readline())
    # 输出第二行
    print(f.readline())
# 关闭打开的文件
f.close()

# readlines()
with open(r"F:\USER\Desktop\Benny\benny\python\code\file.txt",'r') as f:
    # 读取所有行
    print(f.readlines())
# 关闭打开的文件
f.close()

##############
#### 例2 #####
#  输出文件名
with open(r"F:\USER\Desktop\Benny\benny\python\code\file.txt",'r') as f:
    # 读取文件内容，并输出
    print(f.name)
# 关闭打开的文件
f.close()

##############
#### 例3 #####
#  seek()函数
with open(r"F:\USER\Desktop\Benny\benny\python\code\file.txt",'r') as f:
    # 文件指针移动到第三个字符处
    print(f.seek(2))
    # 输出当前文件指针的位置
    print(f.tell())
# 关闭打开的文件
f.close()

##############
#### 例4 #####
# truncate()函数
with open(r"F:\USER\Desktop\Benny\benny\python\code\file.txt",'r+') as f:
    # 输出截断前的数据
    print(f.read())
    # 截断10个字节长度即第一行，换行符在win10中占两个字节
    f.truncate(10)
    # 将文件指针移动到文头
    f.seek(0)
    # 输出截断后的数据
    print(f.read())
# 关闭打开的文件
f.close()

##############
#### 例5 #####

# write()函数
with open(r"F:\USER\Desktop\Benny\benny\python\code\file.txt",'r+') as f:
    # 输出修改前的文件
    print(f.read())
    # 写入字符串数据
    f.write("qinyuan\n")
    # 将文件指针移动到文头
    f.seek(0)
    # 输出修改后的文件
    print(f.read())
# 关闭打开的文件
f.close()

# writelines()函数
with open(r"F:\USER\Desktop\Benny\benny\python\code\file.txt",'r+') as f:
    # 输出修改前的文件
    print(f.read())
    # 写入字符串数据
    f.writelines(["qinyuan\n","benny\n"])
    # 将文件指针移动到文头
    f.seek(0)
    # 输出修改后的文件
    print(f.read())
# 关闭打开的文件
f.close()
