import Utils as u

# 大目录-------start-------
def click1前哨平原():
    print("click1前哨平原")
    u.click_point(30, 20)
    # 等1秒
    u.waitTimer(2)


def click2荒芜之地():
    print("click2荒芜之地")
    u.click_point(30, 28)
    # 等1秒
    u.waitTimer(2)


def click3污染之林():
    print("click3污染之林")
    u.click_point(30, 35)
    # 等1秒
    u.waitTimer(2)


def click4严寒地带():
    print("click4严寒地带")
    u.click_point(30, 43)
    # 等1秒
    u.waitTimer(2)


def click5冰冠堡垒():
    print("click5冰冠堡垒")
    u.click_point(30, 52)
    # 等1秒
    u.waitTimer(2)

def click6幽魂之地():
    u.click_point(30, 60)
    # 等1秒
    u.waitTimer(3)

# 大目录-------end-------
# 大目录-------end-------
# 子目录-------start-------
def click子条目1():
    u.click_point(70, 20)
    # 等6秒
    u.waitTimer(9)


def click子条目2():
    u.click_point(70, 35)
    # 等6秒
    u.waitTimer(9)


def click子条目3():
    u.click_point(70, 43)
    # 等6秒
    u.waitTimer(9)


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
    u.clickGoHome()
    u.click传送阵()
    click4严寒地带()
    click子条目2()

def click61寂静山谷():
    print("click_6幽魂之地_1寂静山谷")
    u.clickGoHome()
    u.click传送阵()
    click6幽魂之地()
    click子条目1()
