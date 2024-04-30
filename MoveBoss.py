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
def move12教堂山谷Boss():
    print("move12教堂山谷Boss")
    clickItem.click12教堂山谷()
    moveRight()
    moveUp()
    moveUp()
    moveUp()
    moveUp()
    moveUp()
    moveUp()
    waitTimer(4)


def move21贫瘠营地Boss():
    print("move21贫瘠营地Boss")
    clickItem.click21贫瘠营地()
    moveRight()
    moveRight()
    moveRight()
    waitTimer(4)


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
    waitTimer(4)


def move32腐烂沼泽Boss1():
    print("move32腐烂沼泽Boss1")
    clickItem.click32腐烂沼泽()
    moveUp()
    moveUp()
    moveUp()
    moveUp()
    moveUp()
    moveRight()
    moveRight()
    moveUp()
    moveUp()
    moveUp()
    moveRight()
    moveRight()
    moveUp()
    moveUp()
    moveUp()
    moveUp()
    moveRight()
    moveUp()
    waitTimer(7)


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
    moveLeft()
    moveLeft()
    moveLeft()
    waitTimer(8)


def move33寒风营地Boss():
    print("move33寒风营地Boss")
    clickItem.click33寒风营地()
    moveRight()
    moveRight()
    moveUp()
    moveRight()
    moveRight()
    moveUp()
    waitTimer(6)


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
    waitTimer(12)


def move41魔力之环Boss2():
    print("move41魔力之环Boss1")
    clickItem.click41魔力之环()
    moveDown()
    moveDown()
    moveDown()
    moveDown()
    moveDown()
    waitTimer(10)


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
    waitTimer(10)
