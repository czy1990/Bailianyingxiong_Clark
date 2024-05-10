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
    diamondCount = moveResource.move42寒风营地DiamondCount(1689)
    woodCount = moveResource.move51王座大厅WoodCount(1555) + diamondCount
    while True:  # 这将创建一个无限循环
        count += 1
        print("------循环次数:" + str(count) + "当前时间" + u.currentTime())

        if count < diamondCount:  # n 此以下执行此函数
            moveResource.move42寒风营地Diamond()  # 大致60一次
        elif count <= woodCount:
            moveResource.move51王座大厅Wood()
        else:
            upBoss()


def getUpBoss():
    count = 0
    while True:  # 创建一个无限循环
        count += 1
        print("------循环次数:" + str(count) + "当前时间" + u.currentTime())
        upBoss()


def upBoss():
    print("upBoss")
    moveBoss.move12教堂山谷Boss()
    moveBoss.move21贫瘠营地Boss()
    moveBoss.move31污染哨站Boss()
    moveBoss.move33寒风营地Boss()
    moveBoss.move41魔力之环Boss2()
    moveBoss.move51王座大厅Refresh()


getUpLevel()
