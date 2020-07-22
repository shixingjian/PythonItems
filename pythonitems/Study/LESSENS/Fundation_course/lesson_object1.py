# auther:shixingjian  time:2020/6/24/0024
class Sheep:
    nickName = "羊"

    def __init__(self, inweight=100):
        self.weight = inweight
        # 叫，实例方法

    def roar(self):
        print('我是羊-------Wow，体重减少5斤')
        self.weight -= 5
        # 吃，实例方法

    def feed(self, food):
        if food == "草":
            self.weight += 10
            print("喂食正确，体重加10斤")
        else:
            self.weight -= 10
            print("喂食错误，体重减少10斤")
class Room:
    def __init__(self,inNum,inAnimal):
        self.num = inNum
        self.animal = inAnimal
    pass
class Tiger:
    nickName = "老虎"
    def __init__(self,inweight = 200):
        self.weight = inweight
        #叫，实例方法
    def roar(self):
        print('我是老虎-------Wow，体重减少5斤')
        self.weight -= 5
        #吃，实例方法
    def feed(self,food):
        if food == "肉":
            self.weight += 10
            print("喂食正确，体重加10斤")
        else:
            self.weight -= 10
            print("喂食错误，体重减少10斤")
    #静态方法：所有实例都一样的操作
    @staticmethod
    def static_roar():
        print('静态方法---Wow')

# t1 = Tiger(200)
# print(t1.weight)
#
# t1.roar()
# t1.feed("1")
# t1.static_roar()
# print(t1.weight)

# r1 = Room(2,t1)
# r1.animal.roar()

#--------------游戏初始化-----------创建10个房间1-10，动物随机
from random import randint #randint(0,2) 双闭区间0，1，2
import time
# print(time.time())#1970到现在的秒数
start = time.time()
roomList = []
for one in range(1,11):
    if randint(0,1) == 0:
        ani = Tiger()
    else:
        ani = Sheep()
    room = Room(one,ani)
    roomList.append(room)#房间实例

#时间差:
while True:
    curTime = time.time()
    if curTime - start >=20:
        #打印所有房间号/动物/体重----操作列表里每一个元素----遍历
        for one in roomList:
            print(f'房间号是:{one.num}，动物是:{one.animal.nickName}，体重是:{one.animal.weight}')
        break
    roomNum = randint(1,10)#int
    roomObject = roomList[roomNum - 1]#在列表中取出房间实例对象
    #提示用户房间号，是否需要敲门
    answer = input(f'当前房间编号为:{roomNum},是否需要敲门(y/n)？')
    if answer == 'y':
        roomObject.animal.roar()
    else:
        food1 = input('请投喂食物(肉/草)？')
        roomObject.animal.feed(food1)



