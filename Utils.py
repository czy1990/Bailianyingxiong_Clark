import uiautomator2 as u2

# 手机像素宽：1440-1
displayX = 1439
# 手机像素高：2560-1
displayY = 2559

def init():
    global context  # 声明PI为全局变量
    context = u2.connect('127.0.0.1:7555')
# 定义点击百分比, 输入比例， 0~100
def click_point(x, y):
    clickX = x / 100 * displayX
    clickY = y / 100 * displayY
    context.click(clickX, clickY)
    # print(clickX)
    # print(clickY)


defultTimer = 5.0


# 等待时间, 默认我5秒
def waitTimer(timer=defultTimer):
    context.sleep(timer)


def click传送阵():
    print("click传送阵")
    click_point(55, 40)
    waitTimer(4)

    # 回城


def clickGoHome():
    print("回城")
    click_point(90, 90)
    # 等9秒
    waitTimer(9)


# 移动百分比, 输入比例， 0~100 # 从坐标(100, 200)滑动到(300, 400)
def move_point(fx, fy, tx, ty):
    fxx = fx / 100 * displayX
    fyy = fy / 100 * displayY
    txx = tx / 100 * displayX
    tyy = ty / 100 * displayY
    context.swipe(fxx, fyy, txx, tyy)


def moveUp():
    move_point(50, 85, 50, 55)
    waitTimer(0.3)


def moveDown():
    move_point(50, 55, 50, 85)
    waitTimer(0.3)


def moveLeft():
    move_point(55, 80, 25, 80)
    waitTimer(0.3)


def moveRight():
    move_point(55, 80, 85, 80)
    waitTimer(0.3)
