# coding:utf-8
# python_lesson8_条件判断
# author：Qinyuan

#########
## 例1 ##
while True:
    score=int(input('请输入您的数学成绩：'))
    if score>100 :
        print('请输出正确的数学成绩')
    elif score>=90 :
        print('您的等级为A')
    elif score>=80 :
        print('您的等级为B')
    elif score>=60 :
        print('您的等级为C')
    else :
        print('您的等级为D')    

#########
## 例2 ##
while True:
    gender = input('请输入性别(男/女)：')
    if gender == '男' :
        score = eval(input('请输入50米时间(5.0~10.0)：'))
        if score<=6.0 :
            print('您的等级为A')
        elif score<=7.0 :
            print('您的等级为B')
        elif score<=8.0 :
            print('您的等级为C')
        else :
            print('您的等级为D')    
    elif gender == '女' :
        score = eval(input('请输入50米时间(5.0~10.0)：'))
        if score<=7.0 :
            print('您的等级为A')
        elif score<=8.0 :
            print('您的等级为B')
        elif score<=9.0 :
            print('您的等级为C')
        else :
            print('您的等级为D') 
    else :
        print('请输入正确的性别')
