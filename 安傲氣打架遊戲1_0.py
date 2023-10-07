#文字遊戲
import time
import random
暫停一次=False
class 怪物:
    生命=200
class 玩家:
  生命=150

安傲氣=怪物()
player=玩家()
def 玩家行動():
  動作=input("輸入動作名稱:")
  match 動作:
    case "回血":
      print("玩家使用了回血!")
      player.生命 = player.生命 + 50
      time.sleep(2)
      print("你增加了50點血")
      time.sleep(2)
    case "頭頭攻擊":
      print("玩家使用頭部撞擊!")
      player.生命 = player.生命 - 30
      安傲氣.生命-=70
      time.sleep(2)
      print("玩家少了30點生命，安傲氣少了70滴血")
    case "空氣炮":
      print("玩家使用了空氣炮！")
      time.sleep(2)
      安傲氣.生命-=45
      print("安傲氣減少了45點血")
    case _:
      print("沒有這個動作再選一次")
      time.sleep(2)
      玩家行動()

def 怪物行動():
  怪物動作=random.randint(1,5)
  match 怪物動作:
    case 1:
      print("安傲氣用阿嬤的水果刀攻擊你了!")
      player.生命 = player.生命 - 20
      time.sleep(2)
      print(f"你被攻擊了，攻擊力：20")
    case 2:
      print("安傲氣用安啊飛刀攻擊你了!")
      player.生命 = player.生命 - 30
      time.sleep(2)
      print(f"你被攻擊了，攻擊力：30")
    case 3:
      print("安傲對你比拳頭！")
    case 4:
      print("安傲氣用神奇的魔法回血了30點的血！")
      安傲氣.生命 += 30
    case 5:
      print("安傲氣用火箭炮攻擊你了")
      player.生命 = player.生命 - 25
      time.sleep(2)
      print("攻擊力:25")
    case 6:
      print("安傲氣耍帥丟鐵錘打到自己了！")
      time.sleep(2)
      安傲氣.生命-=70
      print("安傲氣少了70點血！")
    case 7:
      print("安傲氣用過肩摔把你摔倒了！")
      time.sleep(2)
      player.生命-=60
      print("玩家少了60點血！")

print("程序加載中…")
time.sleep(2)
print("正在加載遊戲資源…")
time.sleep(2)
print("我們開始吧！")
time.sleep(2)
print("提示：安傲氣是你的敵人！")
time.sleep(2)
print("安傲氣:來打架啊!"	)
time.sleep(2)

while player.生命 and 安傲氣.生命>0:
    print("---------------------------------------------------------------------------")
    怪物行動()
    time.sleep(2)
    print(f"你的生命:{player.生命}")
    time.sleep(2)
    print(f"安傲氣生命:{安傲氣.生命}")
    time.sleep(2)
    print("你可以用的動作：\n名稱:回血\n用途:使用魔法回復回復50點血 ")
    time.sleep(2)
    print("\n名稱:頭頭攻擊\n用途:使用頭來撞擊敵人，自己會損失30點血，但安傲氣會損失70點血！")
    time.sleep(2)
    print("\n名稱:空氣炮\n用途:安傲氣會損失45點血！ ")
    time.sleep(2)
    玩家行動()

print("遊戲結束了！")
