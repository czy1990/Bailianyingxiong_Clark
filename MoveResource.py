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


def moveLeftHalf():
    u.moveLeftHalf()


def moveRightHalf():
    u.moveRightHalf()


def moveUpHalf():
    u.moveUpHalf()


def moveDownHalf():
    u.moveDownHalf()


def moveLeftUp():
    u.moveLeftUp()


def moveLeftDown():
    u.moveLeftDown()


def moveRightUp():
    u.moveRightUp()


def moveRightDown():
    u.moveRightDown()


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
    u.clickGoHome()


timer42 = 1.3


def move42寒风营地Diamond():
    print("move42寒风营地Diamond")
    clickItem.click42北风营地()
    moveLeft()
    moveLeft()
    moveDown()
    moveDown()  # 刚出门
    moveLeft()
    moveLeft()
    moveLeft()
    moveLeft()
    waitTimer(timer42)
    moveLeft()
    moveLeft()
    moveDown()
    moveLeft()
    moveDown()
    moveDown()
    waitTimer(timer42)
    moveUp()
    moveUp()
    moveLeft()
    moveLeft()
    waitTimer(timer42)
    moveUp()
    moveUp()
    moveUp()
    moveUp()
    waitTimer(timer42)

    moveLeft()
    moveLeft()
    waitTimer(timer42)
    moveUp()
    moveUp()
    moveUp()  # 到最上
    waitTimer(timer42)

    moveLeft()
    moveDown()
    moveDown()
    waitTimer(timer42)
    moveDown()
    moveLeft()
    moveLeft()
    moveLeft()
    moveDown()
    moveDown()
    waitTimer(timer42)
    u.clickGoHome()


def move42寒风营地DiamondCount(currentNumber):
    count = (3500 - currentNumber) / 60
    print("move42寒风营地DiamondCount: " + count.__str__())
    return count


def move51王座大厅WoodCount(currentNumber):
    count = (5000 - currentNumber) / 138
    print("move51王座大厅WoodCount: " + count.__str__())
    return count


timer51 = 1.5


def move51王座大厅Wood():
    print("move51王座大厅Wood")
    clickItem.click51王座大厅()
    # 进入王座大厅需要额外6秒
    waitTimer(6)
    moveLeft()
    moveUp()
    moveLeft()
    moveUp()
    moveUp()
    waitTimer(timer51)

    moveRight()
    moveUp()
    moveRight()
    moveUp()
    moveUp()
    moveUp()
    moveRight()
    waitTimer(timer51)  # 门拐角

    moveUp()
    moveRight()
    moveRight()
    moveRightUp()
    waitTimer(timer51)

    moveUp()
    moveLeft()
    moveLeftDown()
    moveLeft()
    moveRightUp()
    waitTimer(timer51)  # 桌子边上

    moveLeftUp()
    moveLeftUp()
    moveLeftUp()
    moveLeft()
    waitTimer(timer51)

    moveLeft()
    moveLeftDown()
    moveDown()
    moveLeftDown()
    moveLeftHalf()
    moveDownHalf()
    moveLeftDown()
    moveRightDown()
    waitTimer(timer51) # 出门

    moveLeftUp()
    moveLeft()
    moveLeft()
    moveUp()
    moveLeftUp()
    moveLeft()
    waitTimer(timer51)

    moveLeftDown()
    moveDown()
    moveDown()
    waitTimer(timer51)

    # 打突出的部分
    moveRightDown()
    moveRightDown()
    waitTimer(timer51)
    moveLeftUp()
    moveLeftUp()

    moveLeft()
    moveLeftUp()
    moveLeft()
    moveLeftUp()
    moveLeftDown()
    moveLeft()
    moveDown()
    moveLeftDown()  # 平台
    waitTimer(timer51)
    moveRightDown()
    moveRightDown()

    moveLeft()
    moveLeftUp()
    moveLeft()
    moveLeft()
    moveLeftDown()
    waitTimer(timer51)

    moveLeft()
    moveRightDown()
    moveRightDown()
    moveDown()
    waitTimer(timer51)

    moveLeft()
    moveDown()
    moveDown()
    moveDown()
    moveRightDown()
    waitTimer(timer51)
    moveLeftUp()
    moveLeftUp()
    moveLeftUp()

    moveLeft()
    moveLeft()
    moveLeft()
    moveLeftUp()
    waitTimer(timer51)
    moveLeftUp()

    moveLeft()
    moveUp()
    moveLeft()
    moveLeft()
    moveLeftUp()
    moveLeftUp()
    moveRightUp()
    waitTimer(timer51)

    moveLeftUp()
    moveLeft()
    moveLeftUp()
    moveLeft()
    waitTimer(timer51)

    moveLeft()
    moveLeft()
    moveDown()
    moveRightDown()
    waitTimer(timer51)

    moveRight()
    moveRight()
    waitTimer(timer51)
    u.clickGoHome_确认()

def click竞技场(numBer=3):
    # 用法: click竞技场(10)
    count = 0
    while count < numBer:
        count += 1
        print("-----" + count.__str__() + "-1-u.click_point(80, 66)")
        u.click_point(80, 75)
        u.waitTimer(8)
        # print("" + count.__str__() + "-2-u.moveRightHalf()")
        # u.moveRightHalf()
        u.waitTimer(10)
        print("" + count.__str__() + "-3-u.click_point(80, 66)")
        u.click_point(80, 75)
        u.waitTimer(5)
