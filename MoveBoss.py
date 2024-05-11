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
    u.clickGoHome()


timer21 = 3


def move21贫瘠营地Boss():
    print("move21贫瘠营地Boss")
    clickItem.click21贫瘠营地()
    moveRight()
    moveRight()
    moveRightHalf()
    waitTimer(timer21)
    u.clickGoHome()

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
    u.clickGoHome()


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
    u.clickGoHome()

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
