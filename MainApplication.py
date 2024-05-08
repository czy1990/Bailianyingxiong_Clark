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
    while True:  # 这将创建一个无限循环
        count += 1
        print("------循环次数:" + str(count) + "当前时间" + u.currentTime())
        if count < 1:  # n 此以下执行此函数
           # moveResource.move42寒风营地Diamond()
           #  moveLevel.move61寂静山谷UpLevelWood()
           #  moveLevel.move61寂静山谷UpLevelWood()
            moveResource.move51王座大厅Wood()
        else:
            moveLevel.move72制热哨站UpLevel()
            # moveLevel.move63哀嚎营地UpLevel()


def getUpBoss():
    count = 0
    while True:  # 创建一个无限循环
        count += 1
        print("------循环次数:" + str(count) + "当前时间" + u.currentTime())
        # moveBoss.move41魔力之环Boss1()  # 远
        moveBoss.move12教堂山谷Boss()  # 近
        moveBoss.move21贫瘠营地Boss()  # 近
        moveLevel.move61寂静山谷UpLevelWood()

        # moveBoss.move42北风营地Boss()  # 远
        moveBoss.move31污染哨站Boss()  # 近
        moveBoss.move32腐烂沼泽Boss1()  # 远
        moveLevel.move61寂静山谷UpLevelWood()

        # moveBoss.move41魔力之环Boss1()  # 远
        moveBoss.move32腐烂沼泽Boss2()  # 远
        moveBoss.move33寒风营地Boss()  # 近
        moveLevel.move61寂静山谷UpLevelWood()


getUpLevel()
# getUpBoss()
# moveLevel.move72制热哨站UpLevel()
