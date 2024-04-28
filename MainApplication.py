import MoveBoss as moveBoss
import Utils as u
import MoveLevel as moveLevel
import MoveDiamond as moveDiamond
 # 通过IP连接
# -------------------------------------------------
# 1，出城
# 2. 回城
# -------------------------------------------------
u.init()
def click刷钱1_3():
    moveBoss.move12教堂山谷Boss()
    moveBoss.move21贫瘠营地Boss()
    moveBoss.move31污染哨站Boss()
    moveBoss.move32腐烂沼泽Boss1()
    moveBoss.move32腐烂沼泽Boss2()
    moveBoss.move33寒风营地Boss()
def click刷钱2_3():
    moveBoss.move21贫瘠营地Boss()
    moveBoss.move31污染哨站Boss()
    moveBoss.move32腐烂沼泽Boss1()
    moveBoss.move32腐烂沼泽Boss2()
    moveBoss.move33寒风营地Boss()


def click升级4_1寒风营地():
    print("click升级4_1寒风营地")
    moveBoss.move41寒风营地UpLevel()


count = 0
while True:  # 这将创建一个无限循环
    count += 1
    print(count)
# moveBoss.move33寒风营地Boss()
# 测试:
# moveBoss.move12教堂山谷Boss()
# moveBoss.move21贫瘠营地Boss()
# moveBoss.move31污染哨站Boss()
# moveBoss.move32腐烂沼泽Boss1()
# moveBoss.move32腐烂沼泽Boss2()
# moveBoss.move33寒风营地Boss()
    moveLevel.move41寒风营地UpLevel()
    moveLevel.move42寒风营地UpLevel()
# moveLevel.move41寒风营地UpLevel()

