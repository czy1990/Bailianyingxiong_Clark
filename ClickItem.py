import Utils as u

clickWaitTimer_Pad = 2
clickWaitTimer = 2


# 大目录-------start-------
def click1前哨平原():
    # print("click1前哨平原")
    u.click_point(30, 25)
    # 等1秒
    if u.isPad:
        u.waitTimer(clickWaitTimer_Pad)
    else:
        u.waitTimer(clickWaitTimer)


def click2荒芜之地():
    # print("click2荒芜之地")
    u.click_point(30, 33)
    # 等1秒
    if u.isPad:
        u.waitTimer(clickWaitTimer_Pad)
    else:
        u.waitTimer(clickWaitTimer)


def click3污染之林():
    # print("click3污染之林")
    u.click_point(30, 37)
    # 等1秒
    if u.isPad:
        u.waitTimer(clickWaitTimer_Pad)
    else:
        u.waitTimer(clickWaitTimer)

def click3熔火三层():
    # print("click3污染之林")
    click3污染之林()

def click4严寒地带():
    # print("click4严寒地带")
    u.click_point(30, 43)
    # 等1秒
    if u.isPad:
        u.waitTimer(clickWaitTimer_Pad)
    else:
        u.waitTimer(clickWaitTimer)


def click5冰冠堡垒():
    # print("click5冰冠堡垒")
    u.click_point(30, 50)
    # 等1秒
    if u.isPad:
        u.waitTimer(clickWaitTimer_Pad)
    else:
        u.waitTimer(clickWaitTimer)


def click6幽魂之地():
    u.click_point(30, 55)
    # 等1秒
    if u.isPad:
        u.waitTimer(clickWaitTimer_Pad)
    else:
        u.waitTimer(clickWaitTimer)


def click7燃烧平原():
    u.click_point(30, 63)
    # 等1秒
    if u.isPad:
        u.waitTimer(clickWaitTimer_Pad)
    else:
        u.waitTimer(clickWaitTimer)

def click8黑石堡垒():
    u.click_point(30, 68)
    # 等1秒
    if u.isPad:
        u.waitTimer(clickWaitTimer_Pad)
    else:
        u.waitTimer(clickWaitTimer)

def click2_2无尽深渊():
    u.click_point(70, 83)
    # 等1秒
    if u.isPad:
        u.waitTimer(clickWaitTimer_Pad)
    else:
        u.waitTimer(1)

# 大目录-------end-------
# 大目录-------end-------
# 子目录-------start-------
clickSubWaitTimer_Pad = 8
clickSubWaitTimer = 9


def click子条目1():
    u.click_point(70, 26)
    # 等6秒
    if u.isPad:
        u.waitTimer(clickSubWaitTimer_Pad)
    else:
        u.waitTimer(clickSubWaitTimer)


def click子条目2():
    u.click_point(70, 36)
    # 等6秒
    if u.isPad:
        u.waitTimer(clickSubWaitTimer_Pad)
    else:
        u.waitTimer(clickSubWaitTimer)


def click子条目3():
    u.click_point(70, 45)
    # 等6秒
    if u.isPad:
        u.waitTimer(clickSubWaitTimer_Pad)
    else:
        u.waitTimer(clickSubWaitTimer)

def click子条目4():
    u.click_point(70, 55)
    # 等6秒
    if u.isPad:
        u.waitTimer(clickSubWaitTimer_Pad)
    else:
        u.waitTimer(clickSubWaitTimer)

def click子条目5():
    u.click_point(70, 65)
    # 等6秒
    if u.isPad:
        u.waitTimer(clickSubWaitTimer_Pad)
    else:
        u.waitTimer(clickSubWaitTimer)

# 子目录-------end-------
def click12教堂山谷():
    print("click_1前哨平原_2教堂山谷")
    u.click传送阵()
    click1前哨平原()
    click子条目2()


def click21贫瘠营地():
    print("click_2荒芜之地_1贫瘠营地")
    u.click传送阵()
    click2荒芜之地()
    click子条目1()


def click22双峰山谷():
    print("click_2荒芜之地_2双峰山谷")
    u.click传送阵()
    click2荒芜之地()
    click子条目2()


def click31污染哨站():
    print("click_3污染之林_1污染哨站")
    u.click传送阵()
    click3污染之林()
    click子条目1()


def click32腐烂沼泽():
    print("click_3污染之林_2腐烂沼泽")
    u.click传送阵()
    click3污染之林()
    click子条目2()


def click33寒风营地():
    print("click_3污染之林_3寒风营地")
    u.click传送阵()
    click3污染之林()
    click子条目3()


def click41魔力之环():
    print("click_4严寒地带_1魔力之环")
    u.click传送阵()
    click4严寒地带()
    click子条目1()


def click42北风营地():
    print("click_4严寒地带_2北风营地")
    u.click传送阵()
    click4严寒地带()
    click子条目2()


def click51王座大厅():
    print("click_5冰冠堡垒_1王座大厅")
    u.click传送阵()
    click5冰冠堡垒()
    click子条目1()


def click52魔力回廊():
    print("click_5冰冠堡垒_2魔力回廊")
    u.click传送阵()
    click5冰冠堡垒()
    click子条目2()
    u.waitTimer(3)


def move51王座大厅Refresh():
    print("click_5冰冠堡垒_1王座大厅_Refresh")
    u.click传送阵()
    click5冰冠堡垒()
    click子条目1()
    # 王座大厅需要额外3秒
    u.waitTimer(3)
    u.clickGoHome_确认()


def click51王座大厅Refresh_NO_Home():
    print("click51王座大厅Refresh_NO_Home")
    u.click传送阵()
    click5冰冠堡垒()
    click子条目1()
    u.waitTimer(3)


def click61寂静山谷():
    print("click_6幽魂之地_1寂静山谷")
    u.click传送阵()
    click6幽魂之地()
    click子条目1()

def click62幽影墓园():
    print("click_6幽魂之地_2幽影墓园")
    u.click传送阵()
    click6幽魂之地()
    click子条目2()

def click63哀嚎营地():
    print("click_6幽魂之地_3哀嚎营地")
    u.click传送阵()
    click6幽魂之地()
    click子条目3()


def click72炽热哨站():
    print("click_7燃烧平原_2炽热哨站")
    u.click传送阵()
    click7燃烧平原()
    click子条目2()

def click82大厅楼道():
    print("click_8燃烧平原_2大厅楼道")
    u.click传送阵()
    click8黑石堡垒()
    click子条目2()

def click113熔火三层区域五():
    print("click_11熔火三层_区域五层")
    u.click传送阵()
    click2_2无尽深渊()
    click3熔火三层()
    click子条目5()



def clickCardMoney(timer=8):
    # print("click_Card_Money")
    u.click_point(50, 75)
    u.waitTimer(timer)

def click3x():
    u.click_point(73, 70)
    u.waitTimer(1)

def clickCardAbandon(timer=4):
    # print("click_Card_Abandon")
    u.click_point(50, 82)
    u.waitTimer(timer)
