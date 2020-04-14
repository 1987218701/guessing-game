# 编写程序，模仿人机猜拳游戏，要求运行三次并判断输赢后输出结果！
import random
dic = {
    1: '剪刀',
    2: '石头',
    3: '布'
}
count = 0
print('本次游戏采取三局两胜制，能不能通关就看你的实力了！加油哦~少年！')
for i in range(3):
    player = random.randint(1, 3)
    user = int(input('请输入您选择的数字(1(剪刀)2(石头)3(布)):'))
    print(f'对手选择了{dic[player]}', end=',')
    print(f'您选择了{dic.get(user)}')
    if user < 1 or user > 3:
        print('用户输入错误！')
    else:
        if user == 1 and player == 3 or user == 2 and player == 1 or user == 3 and player == 2:
            print('恭喜你，你胜利了！')
            count += 1
        elif user == player:
            print('双方打成平手！')
        else:
            print('太遗憾了，差一点就赢了！')
            count -= 1
    print('==============================================|')
if count > 0:
    print('恭喜你通关！')
elif count < 0:
    print('通关失败！')
else:
    print('实力相当！')
