from datetime import datetime, timedelta

import time
import MoveBoss as moveBoss
import Utils as u
import ClickItem as clickItem
import MoveResource as moveResource

# 通过IP连接
# -------------------------------------------------
# 1，出城
# 2. 回城
# -------------------------------------------------
u.init(True)


def getUpLevel(wood=4000, diamond=2500, hours=1000, minutes=0):
    count = 0
    # 运行时间
    print("------getUpLevel 起始时间" + u.currentTime())
    ctimer = u.currentTimerNow()

    diamondCount = moveResource.move42寒风营地DiamondCount(diamond)
    woodCount = moveResource.move51王座大厅WoodCount(wood) + diamondCount

    start_time = time.time()  # 获取当前时间的时间戳
    end_time = start_time + hours * 3600 + minutes * 60  # 1小时后的时间戳 1 * 3600, 秒为单位

    # 第一次 自动点击城镇按钮
    u.click_point(57, 33)

    # while True:
    while start_time < end_time:  # 这将创建一个无限循环
        count += 1
        timerDiff = u.currentTimerNow() - ctimer

        print("------循环次数:" + str(count) + "当前时间" + u.currentTime() + ",运行时间:" + timerDiff.__str__())
        print("start_time:" + u.formatTimer(start_time) + " ,end_time:" + u.formatTimer(end_time))

        if count < diamondCount:  # n 此以下执行此函数
            moveResource.move42寒风营地Diamond()  # 大致60一次
        elif count <= woodCount:
            moveResource.move51王座大厅Wood()
        else:
            upBoss()
        # 更新运行时间
        start_time = time.time()
        # 第goHomeNumber次回家
        goHomeNumber = 40
        goHomeCount = (count % goHomeNumber)
        isGoHome = goHomeCount == 0
        print("goHomeCount" + goHomeCount.__str__() + ",isGoHome: +" + isGoHome.__str__())
        if isGoHome:
            u.clickGoHome_确认()


def getUpBoss():
    count = 0
    print("------getUpBoss 起始时间" + u.currentTime())
    ctimer = u.currentTimerNow()
    while True:  # 创建一个无限循环
        count += 1
        timerDiff = u.currentTimerNow() - ctimer
        print("------循环次数:" + str(count) + ",当前时间:" + u.currentTime() + ",运行时间:" + timerDiff.__str__())

        upBoss()


def getCard(money, max3X=False):
    count = 0
    print("------getCard 起始时间" + u.currentTime())
    ctimer = u.currentTimerNow()

    if max3X:
        moneyCount = money // 300
    else:
        moneyCount = money // 100

    while count < moneyCount:  # 创建一个无限循环
        count += 1
        timerDiff = u.currentTimerNow() - ctimer
        print("------剩余次数:" + str(moneyCount - count) + "/" + moneyCount.__str__()
              + ",当前时间:" + u.currentTime() + ",运行时间:" + timerDiff.__str__())

        if max3X:
            clickItem.click3x()

        clickItem.clickCardMoney()
        u.screenshot(count)
        clickItem.clickCardAbandon()


def upBoss():
    print("upBoss")
    # 0:02:05 50金币版本 大致一小时
    u.waitTimer(3)
    moveBoss.move21贫瘠营地Boss()  # 10
    moveBoss.move12教堂山谷Boss()  # 10
    moveBoss.move31污染哨站Boss()  # 20
    moveBoss.move33寒风营地Boss()  # 10
    moveBoss.move51王座大厅Refresh_NO_Home()


def click竞技场(numBer=3):
    # 用法: click竞技场(10)
    count = 0
    while count < numBer:
        count += 1
        print("-----" + count.__str__() + "-1-u.click_point(80, 66)")
        u.click_point(80, 66)
        u.waitTimer(8)
        print("" + count.__str__() + "-2-u.moveRightHalf()")
        u.moveRightHalf()
        u.waitTimer(13)
        print("" + count.__str__() + "-3-u.click_point(80, 66)")
        u.click_point(80, 66)
        u.waitTimer(5)


# 竞技场(次数)  慎用, 绿钻
# click竞技场()

# 金币抽卡
# getCard(6264, True)

#刷钱+资源(木头+钻石)
getUpLevel(4000, 2500)
