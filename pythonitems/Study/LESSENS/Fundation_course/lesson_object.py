# auther:shixingjian  time:2020/6/24/0024
class Tiger:
    #1.静态属性：这个属性属于整个类所有的实例，大家共同的特征
    nickName = '老虎'#静态属性，昵称
    #2.大家有些特征不一样，----每个实例这个特征可以不一样
    def __init__(self,inweight): #初始化方法---只要创建实例，方法自动调用
        self.weight = inweight
        #1.实例.属性2.类.属性
t1 = Tiger(100)
print(t1.weight)

t2 = Tiger(200)
print(t2.weight)