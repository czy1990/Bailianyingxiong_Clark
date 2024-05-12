import MoveBoss as moveBoss
import Utils as u
import ClickItem as clickItem
import MoveLevel as moveLevel
import MoveResource as moveResource

# 通过IP连接
# -------------------------------------------------
# 1，出城
# 2. 回城
# -------------------------------------------------
u.init(True)


def click刷钱1_3():
    moveBoss.move12教堂山谷Boss()
    moveBoss.move21贫瘠营地Boss()
    moveBoss.move31污染哨站Boss()
    moveBoss.move32腐烂沼泽Boss1()
    moveBoss.move32腐烂沼泽Boss2()
    moveBoss.move33寒风营地Boss()


def click刷钱2_3():
    moveBoss.move21贫瘠营地Boss()
    moveBoss.move31污染哨站Boss()
    moveBoss.move32腐烂沼泽Boss1()
    moveBoss.move32腐烂沼泽Boss2()
    moveBoss.move33寒风营地Boss()


def click升级4_1寒风营地():
    print("click升级4_1寒风营地")
    moveBoss.move41寒风营地UpLevel()


def getUpLevel():
    count = 0
    # 时间差
    print("------getUpLevel 起始时间" + u.currentTime())
    ctimer = u.currentTimerNow()

    diamondCount = moveResource.move42寒风营地DiamondCount(1471)
    woodCount = moveResource.move51王座大厅WoodCount(375) + diamondCount

    while True:  # 这将创建一个无限循环
        count += 1
        timerDiff = u.currentTimerNow() - ctimer

        print("------循环次数:" + str(count) + "当前时间" + u.currentTime() + ",时间差:" + timerDiff.__str__())

        if count < diamondCount:  # n 此以下执行此函数
            moveResource.move42寒风营地Diamond()  # 大致60一次
        elif count <= woodCount:
            moveResource.move51王座大厅Wood()
        else:
            upBoss()


def getUpBoss():
    count = 0
    print("------getUpBoss 起始时间" + u.currentTime())
    ctimer = u.currentTimerNow()
    while True:  # 创建一个无限循环
        count += 1
        timerDiff = u.currentTimerNow() - ctimer
        print("------循环次数:" + str(count) + ",当前时间:" + u.currentTime() + ",时间差:" + timerDiff.__str__())

        upBoss()


def upBoss():
    print("upBoss")
    # 0:05:42分钟 110金币的版本  大致一小时1157金币
    # moveBoss.move12教堂山谷Boss()  # 10
    # moveBoss.move21贫瘠营地Boss()  # 10
    # moveBoss.move22双峰山谷Boss()  # 10
    # moveBoss.move31污染哨站Boss()  # 10
    # moveBoss.move32腐烂沼泽Boss1()  # 10
    # moveBoss.move32腐烂沼泽Boss2()  # 10
    # moveBoss.move33寒风营地Boss()  # 10
    # moveBoss.move41魔力之环Boss2()  # 10
    # moveBoss.move42北风营地Boss()  # 10
    # moveBoss.move52魔力回廊Boss_Refresh()  # 10

    # 0:03:18 70 金币的版本 大致一小时1272金币
    # moveBoss.move12教堂山谷Boss()  # 10
    # moveBoss.move21贫瘠营地Boss()  # 10
    # moveBoss.move31污染哨站Boss()  # 20
    # moveBoss.move33寒风营地Boss()  # 10
    # moveBoss.move41魔力之环Boss2()  # 10
    # moveBoss.move52魔力回廊Boss_Refresh()  # 10

    # 0:02:31 60金币版本 大致一小时 1440金币
    moveBoss.move12教堂山谷Boss()  # 10
    moveBoss.move21贫瘠营地Boss()  # 10
    moveBoss.move31污染哨站Boss()  # 20
    moveBoss.move33寒风营地Boss()  # 10
    moveBoss.move41魔力之环Boss2()  # 10
    moveBoss.move51王座大厅Refresh_NO_Home()

getUpLevel()
