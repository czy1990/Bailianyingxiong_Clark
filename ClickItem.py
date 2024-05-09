import Utils as u

clickWaitTimer_Pad = 1.5
clickWaitTimer = 2
# 大目录-------start-------
def click1前哨平原():
    print("click1前哨平原")
    u.click_point(30, 20)
    # 等1秒
    if u.isPad:
        u.waitTimer(clickWaitTimer_Pad)
    else:
        u.waitTimer(clickWaitTimer)

def click2荒芜之地():
    print("click2荒芜之地")
    u.click_point(30, 28)
    # 等1秒
    if u.isPad:
        u.waitTimer(clickWaitTimer_Pad)
    else:
        u.waitTimer(clickWaitTimer)


def click3污染之林():
    print("click3污染之林")
    u.click_point(30, 35)
    # 等1秒
    if u.isPad:
        u.waitTimer(clickWaitTimer_Pad)
    else:
        u.waitTimer(clickWaitTimer)


def click4严寒地带():
    print("click4严寒地带")
    u.click_point(30, 43)
    # 等1秒
    if u.isPad:
        u.waitTimer(clickWaitTimer_Pad)
    else:
        u.waitTimer(clickWaitTimer)


def click5冰冠堡垒():
    print("click5冰冠堡垒")
    u.click_point(30, 52)
    # 等1秒
    if u.isPad:
        u.waitTimer(clickWaitTimer_Pad)
    else:
        u.waitTimer(clickWaitTimer)


def click6幽魂之地():
    u.click_point(30, 60)
    # 等1秒
    if u.isPad:
        u.waitTimer(clickWaitTimer_Pad)
    else:
        u.waitTimer(clickWaitTimer)


def click7燃烧平原():
    u.click_point(30, 66)
    # 等1秒
    if u.isPad:
        u.waitTimer(clickWaitTimer_Pad)
    else:
        u.waitTimer(clickWaitTimer)


# 大目录-------end-------
# 大目录-------end-------
# 子目录-------start-------
clickSubWaitTimer_Pad = 7
clickSubWaitTimer = 9
def click子条目1():
    u.click_point(70, 20)
    # 等6秒
    if u.isPad:
        u.waitTimer(clickSubWaitTimer_Pad)
    else:
        u.waitTimer(clickSubWaitTimer)

def click子条目2():
    u.click_point(70, 35)
    # 等6秒
    if u.isPad:
        u.waitTimer(clickSubWaitTimer_Pad)
    else:
        u.waitTimer(clickSubWaitTimer)


def click子条目3():
    u.click_point(70, 43)
    # 等6秒
    if u.isPad:
        u.waitTimer(clickSubWaitTimer_Pad)
    else:
        u.waitTimer(clickSubWaitTimer)

# 子目录-------end-------
def click12教堂山谷():
    print("click_1前哨平原_2教堂山谷")
    u.clickGoHome()
    u.click传送阵()
    click1前哨平原()
    click子条目2()


def click21贫瘠营地():
    print("click_2荒芜之地_1贫瘠营地")
    u.clickGoHome()
    u.click传送阵()
    click2荒芜之地()
    click子条目1()


def click22双峰山谷():
    print("click_2荒芜之地_2双峰山谷")
    u.clickGoHome()
    u.click传送阵()
    click2荒芜之地()
    click子条目2()


def click31污染哨站():
    print("click_3污染之林_1污染哨站")
    u.clickGoHome()
    u.click传送阵()
    click3污染之林()
    click子条目1()


def click32腐烂沼泽():
    print("click_3污染之林_2腐烂沼泽")
    u.clickGoHome()
    u.click传送阵()
    click3污染之林()
    click子条目2()


def click33寒风营地():
    print("click_3污染之林_3污染之林")
    u.clickGoHome()
    u.click传送阵()
    click3污染之林()
    click子条目3()


def click41魔力之环():
    print("click_4严寒地带_1魔力之环")
    u.clickGoHome()
    u.click传送阵()
    click4严寒地带()
    click子条目1()


def click42北风营地():
    print("click_4严寒地带_2北风营地")
    u.clickGoHome()
    u.click传送阵()
    click4严寒地带()
    click子条目2()


def click51王座大厅():
    print("click_5冰冠堡垒_1王座大厅")
    u.clickGoHome_确认()
    u.click传送阵()
    click5冰冠堡垒()
    click子条目1()


def click61寂静山谷():
    print("click_6幽魂之地_1寂静山谷")
    u.clickGoHome()
    u.click传送阵()
    click6幽魂之地()
    click子条目1()


def click63哀嚎营地():
    print("click_6幽魂之地_3哀嚎营地")
    u.clickGoHome()
    u.click传送阵()
    click6幽魂之地()
    click子条目3()


def click72炽热哨站():
    print("click_7燃烧平原_2哨站")
    u.clickGoHome()
    u.click传送阵()
    click7燃烧平原()
    click子条目2()
