import uiautomator2 as u2
import datetime
import time

# 手机像素宽：1440-1
# displayX = 720
displayX = 1600
# 手机像素高：2560-1
# displayY = 1280
displayY = 2560

isPad = False


def init(pad: bool):
    global context  # 声明PI为全局变量
    global isPad
    # context = u2.connect('127.0.0.1:7555')
    context = u2.connect('a801ab2d')
    isPad = pad
    print("isPad:" + isPad.__str__())


def isPad():
    isPad()


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


click传送阵Timer_Pad = 2
click传送阵Timer = 3


def click传送阵():
    # print("click传送阵")
    click_point(55, 40)
    if isPad:
        waitTimer(click传送阵Timer_Pad)
    else:
        waitTimer(click传送阵Timer)


# 回城
GoHomeX_Pad = 90
GoHomeY_Pad = 85
GoHomeX = 90
GoHomeY = 90

GoHomeTimer_Pad = 9
GoHomeTimer = 9


def clickGoHome():
    # print("回城")

    if isPad:
        click_point(GoHomeX_Pad, GoHomeY_Pad)
    else:
        click_point(GoHomeX, GoHomeY)

    # 等9秒
    if isPad:
        waitTimer(GoHomeTimer_Pad)
    else:
        waitTimer(GoHomeTimer)


clickGoHome_确认Timer_Pad = 1.5
clickGoHome_确认Timer = 4
clickGoHome_确认WatingTimer_Pad = 11
clickGoHome_确认WatingTimer = 18


def clickGoHome_确认():
    print("clickGoHome_确认")
    if isPad:
        click_point(GoHomeX_Pad, GoHomeY_Pad)
    else:
        click_point(GoHomeX, GoHomeY)

    if isPad:
        waitTimer(clickGoHome_确认Timer_Pad)
    else:
        waitTimer(clickGoHome_确认Timer)

    # 点击 确认 的位置
    click_point(60, 60)

    if isPad:
        waitTimer(clickGoHome_确认WatingTimer_Pad)
    else:
        waitTimer(clickGoHome_确认WatingTimer)


# 移动百分比, 输入比例， 0~100 # 从坐标(100, 200)滑动到(300, 400)
def move_point(fx, fy, tx, ty):
    fxx = fx / 100 * displayX
    fyy = fy / 100 * displayY
    txx = tx / 100 * displayX
    tyy = ty / 100 * displayY
    context.swipe(fxx, fyy, txx, tyy, 0.0)


def moveUp():
    move_point(50, 85, 50, 55)


def moveUpHalf():
    move_point(50, 85, 50, 70)


def moveDown():
    move_point(50, 55, 50, 85)


def moveDownHalf():
    move_point(50, 70, 50, 85)


def moveLeft():
    move_point(55, 80, 25, 80)


def moveLeftHalf():
    move_point(55, 80, 40, 80)


def moveRight():
    move_point(55, 80, 85, 80)


def moveRightHalf():
    move_point(55, 80, 70, 80)


def moveLeftUp():
    move_point(60, 60, 40, 40)


def moveLeftDown():
    move_point(60, 40, 40, 60)


def moveRightUp():
    move_point(40, 60, 60, 40)


def moveRightDown():
    move_point(40, 40, 60, 60)


def devicesInfo():
    print(context.window_size())


def currentTime():
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_time

def currentTimerNow():
    return datetime.datetime.now()

def formatTimer(formatT):
    local_time_tuple = time.localtime(formatT)
    return time.strftime('%Y-%m-%d %H:%M:%S', local_time_tuple)
