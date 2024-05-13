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
    count = (2500 - currentNumber) / 60
    print("move42寒风营地DiamondCount: " + count.__str__())
    return count


def move51王座大厅WoodCount(currentNumber):
    count = (4000 - currentNumber) / 100
    print("move51王座大厅WoodCount: " + count.__str__())
    return count


timer51 = 1.5


def move51王座大厅Wood():
    print("move51王座大厅Wood")
    clickItem.click51王座大厅()
    # 进入王座大厅需要额外4秒
    waitTimer(4)
    moveLeft()
    moveUp()
    moveLeft()
    moveUp()
    waitTimer(timer51)

    moveUp()
    moveRight()
    moveUp()
    moveRight()
    waitTimer(timer51)
    moveUp()
    moveUp()
    moveUp()  # 门拐角

    moveRight()
    waitTimer(timer51)
    moveUp()
    moveRight()
    moveRight()
    moveUp()
    waitTimer(timer51)
    moveUp()
    moveLeft()
    moveUp()  # 桌子
    waitTimer(timer51)

    moveLeft()
    moveLeft()
    moveUp()
    waitTimer(timer51)
    moveLeft()
    moveLeft()
    moveLeft()
    moveDown()
    waitTimer(timer51)
    moveDown()  # 第二个门

    moveLeft()
    moveDown()
    moveLeft()
    moveLeft()
    waitTimer(timer51)
    moveLeft()
    moveUp()
    moveLeft()

    moveLeft()
    moveDown()
    waitTimer(timer51)  # 平台

    moveDown()
    moveDown()
    moveDown()
    waitTimer(timer51)
    moveDown()

    moveLeft()
    moveLeft()
    moveDown()
    waitTimer(timer51)
    moveLeft()
    moveDown()
    moveDown()
    moveDown()
    waitTimer(timer51)
    moveDown()
    moveDown()  # 第三个门

    moveLeft()
    moveDown()
    moveLeft()
    waitTimer(timer51)
    moveLeft()
    moveDown()
    moveLeft()
    moveLeft()
    waitTimer(timer51)

    moveUp()
    moveLeft()
    moveLeft()
    moveUp()
    waitTimer(timer51)
    moveUp()
    moveLeft()
    moveLeft()
    moveLeft()
    waitTimer(timer51)

    moveUp()
    moveLeft()
    moveUp()
    waitTimer(timer51)
    moveLeft()
    moveUp()
    moveLeft()
    moveLeft()
    waitTimer(timer51)
    moveUp()

    moveLeft()
    moveLeft()
    moveUp()
    waitTimer(timer51)
    u.clickGoHome_确认()
