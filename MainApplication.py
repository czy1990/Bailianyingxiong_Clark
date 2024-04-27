import uiautomator2 as u2

d = u2.connect('127.0.0.1:7555')  # 通过IP连接
# -------------------------------------------------
# 1，出城
# 2. 回城
# -------------------------------------------------
# 宽：1440 -1
displayX = 1439
# 高：2560
displayY = 2559


# 定义点击百分比, 输入比例， 0~100
def click_point(x, y):
    clickX = x / 100 * displayX
    clickY = y / 100 * displayY
    d.click(clickX, clickY)
    # print(clickX)
    # print(clickY)


# 移动百分比, 输入比例， 0~100 # 从坐标(100, 200)滑动到(300, 400)
def move_point(fx, fy, tx, ty):
    fxx = fx / 100 * displayX
    fyy = fy / 100 * displayY
    txx = tx / 100 * displayX
    tyy = ty / 100 * displayY
    d.swipe(fxx, fyy, txx, tyy)
    # print("移动坐标")
    # print(fxx)
    # print(fyy)
    # print(txx)
    # print(tyy)


def click传送阵():
    print("click传送阵")
    click_point(55, 40)
    waitTimer(1)


# 回城
def clickGoHome():
    print("回城")
    click_point(90, 90)
    # 等6秒
    waitTimer(8)


# 大目录-------start-------
def click1前哨平原():
    print("click1前哨平原")
    click_point(30, 20)
    # 等1秒
    waitTimer(1)


def click2荒芜之地():
    print("click2荒芜之地")
    click_point(30, 28)
    # 等1秒
    waitTimer(1)


def click3污染之林():
    print("click3污染之林")
    click_point(30, 35)
    # 等1秒
    waitTimer(1)


def click4严寒地带():
    print("click4严寒地带")
    click_point(30, 43)
    # 等1秒
    waitTimer(1)


# 大目录-------end-------
# 大目录-------end-------
# 子目录-------start-------
def click子条目1():
    click_point(70, 20)
    # 等6秒
    waitTimer(9)


def click子条目2():
    click_point(70, 35)
    # 等6秒
    waitTimer(9)


def click子条目3():
    click_point(70, 43)
    # 等6秒
    waitTimer(9)


# 子目录-------end-------
def click12教堂山谷():
    print("click_1前哨平原_2教堂山谷")
    clickGoHome()
    click传送阵()
    click1前哨平原()
    click子条目2()


def click21贫瘠营地():
    print("click_2荒芜之地_1贫瘠营地")
    clickGoHome()
    click传送阵()
    click2荒芜之地()
    click子条目1()


def click22双峰山谷():
    print("click_2荒芜之地_2双峰山谷")
    clickGoHome()
    click传送阵()
    click2荒芜之地()
    click子条目2()


def click31污染哨站():
    print("click_3污染之林_1污染哨站")
    clickGoHome()
    click传送阵()
    click3污染之林()
    click子条目1()


def click32腐烂沼泽():
    print("click_3污染之林_2腐烂沼泽")
    clickGoHome()
    click传送阵()
    click3污染之林()
    click子条目2()


def click33寒风营地():
    print("click_3污染之林_3污染之林")
    clickGoHome()
    click传送阵()
    click3污染之林()
    click子条目3()


def click41魔力之环():
    print("click_4严寒地带_1魔力之环")
    clickGoHome()
    click传送阵()
    click4严寒地带()
    click子条目1()


def move12教堂山谷Boss():
    move_point(50, 80, 70, 60)
    waitTimer(1)
    move_point(50, 80, 70, 60)
    waitTimer(0.5)
    move_point(50, 80, 70, 60)
    waitTimer(1)
    move_point(50, 80, 50, 50)
    waitTimer(0.5)
    move_point(50, 80, 50, 50)
    waitTimer(1)
    move_point(50, 80, 60, 50)
    waitTimer(5)

def move21贫瘠营地Boss():
    move_point(50, 80, 70, 80)
    waitTimer(0.5)
    move_point(50, 80, 70, 80)
    waitTimer(0.5)
    move_point(50, 80, 70, 80)
    waitTimer(5)

def move22双峰山谷钻石():
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


def move31污染哨站Boss():
    moveRight()
    moveRight()
    moveDown()
    moveDown()
    moveLeft()
    moveLeft()
    moveDown()
    moveDown()
    waitTimer(5)
    moveDown()
    moveDown()
    moveDown()
    moveDown()
    moveDown()
    waitTimer(5)
    moveDown()
    moveDown()
    moveDown()
    waitTimer(5)

def move32腐烂沼泽Boss1():
    moveUp()
    moveUp()
    moveUp()
    moveUp()
    moveUp()
    moveRight()
    moveRight()
    waitTimer(4)
    moveUp()
    moveUp()
    waitTimer(5)
    moveUp()
    moveRight()
    moveRight()
    moveUp()
    moveUp()
    waitTimer(13)

def move32腐烂沼泽Boss2():
    moveLeft()
    moveLeft()
    moveLeft()
    moveLeft()
    waitTimer(5)
    moveLeft()
    moveLeft()
    moveLeft()
    moveLeft()
    waitTimer(18)
    moveLeft()

def move33寒风营地Boss():
    moveRight()
    moveRight()
    moveUp()
    moveRight()
    moveRight()
    waitTimer(13)
    moveUp()
    moveRight()
    moveRight()
    waitTimer(10)
# 间隔时间
def waitTimer(timer=5.0):
    d.sleep(timer)

def moveUp():
    move_point(50, 80, 50, 50)
    waitTimer(0.3)

def moveDown():
    move_point(50, 50, 50, 80)
    waitTimer(0.3)

def moveLeft():
    move_point(50, 80, 20, 80)
    waitTimer(0.3)

def moveRight():
    move_point(50, 80, 80, 80)
    waitTimer(0.3)

count = 0
while True:  # 这将创建一个无限循环
    count += 1
    print(count)
    click12教堂山谷()
    move12教堂山谷Boss()
    click21贫瘠营地()
    move21贫瘠营地Boss()
    # click22双峰山谷()
    # move22双峰山谷钻石()
    click31污染哨站()
    move31污染哨站Boss()
    click32腐烂沼泽()
    move32腐烂沼泽Boss1()
    click32腐烂沼泽()
    move32腐烂沼泽Boss2()
    click33寒风营地()
    move33寒风营地Boss()
