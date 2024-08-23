import Utils as u
import ClickItem as clickItem


def waitTimer(timer=u.defultTimer):
    u.waitTimer(timer)


def move_point(fx, fy, tx, ty):
    u.move_point(fx, fy, tx, ty)


def moveUp():
    u.moveUp()


def moveUpHalf():
    u.moveUpHalf()


def moveDown():
    u.moveDown()


def moveDownHalf():
    u.moveDownHalf()


def moveLeft():
    u.moveLeft()


def moveLeftHalf():
    u.moveLeftHalf()


def moveRight():
    u.moveRight()


def moveRightHalf():
    u.moveRightHalf()


def moveLeftUp():
    u.moveLeftUp()


def moveLeftDown():
    u.moveLeftDown()


def moveRightUp():
    u.moveRightUp()


def moveRightDown():
    u.moveRightDown()


timer12 = 3


# ---------------------

def move11打羊Monster():
    print("move11打羊Monster")
    waitTimer(2)
    moveRightUp()
    moveRightUp()
    moveRightUp()
    moveRightHalf()
    moveRightUp()
    moveRightUp()
    moveLeftUp()
    moveLeftUp()
    waitTimer(2)
    #外加胖虎
    # moveRight()
    # moveRightUp()
    # moveRight()
    # moveRight()
    # moveRightUp()
    # moveRight()
    # moveRightUp()
    # moveRight()
    # moveRight()
    #
    # moveRightUp()
    # moveRightUp()
    # moveRight()
    # moveRight()
    # moveRight()
    # moveRightUp()
    # moveRight()
    # waitTimer(2.5)
    # 刷新
    u.clickGoHome(4)
    # move51王座大厅Refresh()


def move12教堂山谷Boss():
    print("move12教堂山谷Boss")
    clickItem.click12教堂山谷()
    moveRight()
    moveUp()
    moveUp()
    moveUp()
    moveUp()
    moveUp()
    waitTimer(timer12)
    moveDown()
    moveDown()
    moveDown()
    moveDown()
    moveDown()
    moveLeft()
    # u.clickGoHome()


timer21 = 3


def move21贫瘠营地Boss():
    print("move21贫瘠营地Boss")
    clickItem.click21贫瘠营地()
    moveRight()
    moveRight()
    moveRightHalf()
    waitTimer(timer21)
    moveLeftHalf()
    moveLeft()
    moveLeft()
    # u.clickGoHome()


timer21 = 2


def move22双峰山谷Boss():
    print("move21贫瘠营地Boss")
    clickItem.click22双峰山谷()
    moveRightUp()
    moveRightUp()
    moveRightHalf()
    moveRight()
    moveRight()
    moveRight()
    moveRight()
    moveRight()
    moveRight()
    moveRight()
    moveUpHalf()
    waitTimer(timer21)
    u.clickGoHome()


timer31 = 3


def move31污染哨站Boss():
    print("move31污染哨站Boss")
    clickItem.click31污染哨站()
    moveRight()
    moveRight()
    moveDown()
    moveDown()
    moveLeft()
    moveLeft()
    moveDown()
    moveDown()
    waitTimer(2)
    moveDown()
    moveDown()
    moveDown()
    moveDown()
    moveDown()
    moveDown()
    moveDown()
    waitTimer(timer31)
    u.clickGoHome()


timer32 = 3


def move32腐烂沼泽Boss1():
    print("move32腐烂沼泽Boss1")
    clickItem.click32腐烂沼泽()
    moveUp()
    moveUp()
    moveUp()
    moveRight()
    moveUp()
    moveUp()
    moveUp()
    moveRightUp()
    moveRightUp()
    moveUp()
    moveUp()
    moveRightUp()
    moveRightHalf()
    waitTimer(timer32)
    u.clickGoHome()


timer322 = 3


def move32腐烂沼泽Boss2():
    print("move32腐烂沼泽Boss2")
    clickItem.click32腐烂沼泽()
    moveLeft()
    moveLeft()
    moveLeft()
    moveLeft()
    moveLeft()
    moveLeft()
    moveLeft()
    moveLeft()
    waitTimer(timer322)
    u.clickGoHome()


timer33 = 2


def move33寒风营地Boss():
    print("move33寒风营地Boss")
    clickItem.click33寒风营地()
    moveRight()
    moveRight()
    moveUp()
    moveRight()
    moveUp()
    waitTimer(timer33)
    moveDown()
    moveLeft()
    moveDown()
    moveLeft()
    moveLeft()
    # u.clickGoHome()


timer41 = 5


def move41魔力之环Boss1():
    print("move41魔力之环Boss1")
    clickItem.click41魔力之环()
    moveLeft()
    moveDown()
    moveLeft()
    moveLeft()
    moveLeft()
    moveLeft()
    moveLeft()
    moveLeft()
    moveLeft()
    moveLeft()
    moveLeft()
    moveLeft()
    moveLeft()  #到达boss
    waitTimer(1)
    moveDown()
    moveDown()
    waitTimer(2)
    moveUp()
    moveUp()
    waitTimer(timer41)
    u.clickGoHome()


timer41 = 5


def move41魔力之环Boss2():
    print("move41魔力之环Boss1")
    clickItem.click41魔力之环()
    moveDown()
    moveDown()
    moveDown()
    moveDown()
    moveDown()
    waitTimer(timer41)
    moveUp()
    moveUp()
    moveUp()
    moveUp()
    moveUp()
    # u.clickGoHome()


timer42 = 6


def move42北风营地Boss():
    print("move42北风营地Boss")
    clickItem.click42北风营地()
    moveLeft()
    moveLeft()
    moveDown()
    moveDown()

    moveLeft()
    moveLeft()
    moveLeft()
    moveLeft()
    moveLeft()
    moveLeft()
    moveLeft()
    moveLeft()
    moveLeft()
    moveLeft()
    moveLeft()
    moveLeft()
    moveDown()
    moveLeft()
    waitTimer(timer42)
    u.clickGoHome()


timer52 = 10


def move52魔力回廊Boss_Refresh():
    print("move52魔力回廊Boss_Refresh")
    clickItem.click52魔力回廊()
    moveLeft()
    moveLeft()
    moveLeftUp()
    moveLeft()
    moveLeftUp()
    moveLeft()
    moveLeftUp()
    moveLeft()
    moveLeftUp()
    waitTimer(timer52)
    u.clickGoHome_确认()


def move51王座大厅Refresh():
    print("move51王座大厅Refresh")
    clickItem.move51王座大厅Refresh()


def move51王座大厅Refresh_NO_Home():
    print("move51王座大厅Refresh_NO_Home")
    clickItem.click51王座大厅Refresh_NO_Home()

timer61 = 2
def move61寂静山谷Monster():
    print("move61寂静山谷Monster")
    clickItem.click61寂静山谷()
    moveRightDown()
    moveDown()
    moveRightDown()
    moveDown()
    moveDown()
    moveDown()
    moveDown()
    waitTimer(timer61)

    moveRight()
    moveRightDown()
    moveRight()
    moveRight()
    moveRightUp()
    waitTimer(timer61)

    moveRightDown()
    moveRight()
    moveRightDown()
    moveRight()
    waitTimer(timer61)
    u.clickGoHome()


timer62 = 2
def move62幽影墓园Monster():
    print("move62幽影墓园Monster")
    # clickItem.click62幽影墓园()
    moveRightUp()
    moveRight()
    waitTimer(timer62)

    moveUp()
    moveRightUp()
    moveRightUp()
    waitTimer(timer62)

    moveLeft()
    moveLeft()
    moveLeft()
    moveLeftDown()
    moveLeftDown()
    moveLeft()
    waitTimer(timer62)

    moveUp()
    moveUp()
    moveLeft()
    waitTimer(timer62)
    moveUp()
    moveRight()

    moveRightUp()
    moveUp()
    moveUp()
    waitTimer(timer62)

    moveLeft()
    moveLeft()
    moveLeftUp()
    waitTimer(timer62)
    u.clickGoHome()




timer63 = 2


def move63哀嚎营地Monster():
    print("move52魔力回廊Boss_Refresh")
    clickItem.click63哀嚎营地()
    moveRightDown()
    moveRightDown()
    moveLeft()
    moveLeft()
    # waitTimer(timer63)
    moveLeftDown()
    moveLeftDown()
    moveLeft()
    moveLeft()
    moveDown()
    # waitTimer(timer63)

    moveDown()
    moveRight()
    moveRight()
    moveRight()
    moveRight()
    moveRight()
    moveRightDown()
    waitTimer(timer63)

    moveRight()
    moveRightUp()
    moveRightUp()
    moveRight()
    waitTimer(timer63)

    moveRightDown()
    moveRight()
    moveRightDown()
    waitTimer(timer63)
    u.clickGoHome()

def move82大厅楼道Boss():
    print("move82大厅楼道Boss")
    clickItem.click82大厅楼道()
    u.waitTimer(3)
    moveDown()
    moveDown()
    moveLeft()

    moveLeft()
    moveDown()
    moveDown()
    # 第1个BOSS 结束
    u.waitTimer(3)

    moveLeft()
    moveDown()
    moveLeft()
    # 第2个BOSS 结束
    u.waitTimer(3)

    moveLeft()
    moveLeft()
    moveUp()
    # 第3个BOSS 结束
    u.waitTimer(3)

    moveUp()
    moveUpHalf()
    # 第4个BOSS 结束
    u.waitTimer(3)

    u.clickGoHome_确认()
