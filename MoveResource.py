import Utils as u
import ClickItem as clickItem


def waitTimer(timer=u.defultTimer):
    u.waitTimer(timer)


def move_point(fx, fy, tx, ty):
    u.move_point(fx, fy, tx, ty)


def moveUp():
    u.moveUp()


def moveDown():
    u.moveDown()


def moveLeft():
    u.moveLeft()


def moveRight():
    u.moveRight()


# ---------------------
def move22双峰山谷_钻石():
    print("move22双峰山谷_钻石")
    clickItem.click22双峰山谷()
    move_point(50, 80, 50, 50)
    waitTimer(4)
    move_point(50, 80, 50, 50)
    waitTimer(4)
    move_point(50, 80, 50, 50)
    waitTimer(3)
    move_point(50, 80, 50, 50)
    waitTimer(3)
    move_point(50, 80, 30, 80)
    waitTimer(3)
    move_point(50, 80, 30, 80)
    waitTimer(3)
    move_point(50, 80, 50, 110)
    waitTimer(4)
    move_point(50, 80, 50, 110)
    waitTimer(4)


def move42寒风营地Diamond():
    print("move42寒风营地Diamond")
    clickItem.click42北风营地()
    moveLeft()
    moveLeft()
    moveDown()
    moveDown()
    waitTimer(1)
    moveLeft()
    moveLeft()
    moveLeft()
    moveLeft()
    waitTimer(1)
    moveLeft()
    moveLeft()
    waitTimer(1)
    moveDown()
    moveLeft()
    moveDown()
    moveDown()
    waitTimer(1)
    moveUp()
    moveUp()
    moveLeft()
    moveLeft()
    waitTimer(1)
    moveUp()
    moveUp()
    moveUp()
    moveUp()
    waitTimer(1)
    moveLeft()
    moveLeft()
    waitTimer(1)
    moveUp()
    moveUp()
    moveUp()
    waitTimer(1)
    moveLeft()
    moveDown()
    moveDown()
    moveDown()
    moveLeft()
    moveLeft()
    moveLeft()
    waitTimer(1)
    moveDown()
    moveDown()
    waitTimer(1)


def move51王座大厅Wood():
    print("move51王座大厅Wood")
    clickItem.click51王座大厅()
    moveLeft()
    moveUp()
    moveLeft()
    moveUp()
    waitTimer(1)

    moveUp()
    moveRight()
    moveUp()
    moveRight()
    moveUp()
    waitTimer(1)
    moveUp()
    moveUp() # 门拐角


    moveRight()
    moveUp()
    moveRight()
    moveRight()
    moveUp()
    waitTimer(1)
    moveUp()
    moveLeft()
    moveUp() #桌子

    moveLeft()
    moveLeft()
    moveUp()
    waitTimer(1)
    moveLeft()
    moveLeft()
    moveLeft()
    moveDown()
    waitTimer(1)
    moveDown() #第二个门

    moveLeft()
    moveDown()
    moveLeft()
    moveLeft()
    waitTimer(1)
    moveLeft()
    moveUp()
    moveLeft()

    moveLeft()
    moveDown()
    waitTimer(1) # 平台

    moveDown()
    moveDown()
    moveDown()
    moveDown()
    waitTimer(1)

    moveLeft()
    moveLeft()
    moveDown()
    moveLeft()
    moveDown()
    moveDown()
    moveDown()
    moveDown()
    waitTimer(1)
    moveDown() # 第二个门

    moveLeft()
    moveDown()
    moveLeft()
    moveLeft()
    moveDown()
    moveLeft()
    moveLeft()
    waitTimer(1)

    moveUp()
    moveLeft()
    moveLeft()
    moveUp()
    moveUp()
    moveLeft()
    moveLeft()
    waitTimer(1)

    moveLeft()
    moveUp()
    moveLeft()
    moveUp()
    moveLeft()
    moveUp()
    moveLeft()
    moveLeft()
    moveUp()

    moveLeft()
    moveLeft()
    moveUp()
    waitTimer(21)
