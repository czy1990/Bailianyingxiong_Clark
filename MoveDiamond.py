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
def move22双峰山谷Diamond():
    print("move22双峰山谷钻石")
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
