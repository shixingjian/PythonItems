# auther:shixingjian  time:2020/06/26
'''
需求分析：
    请定义一个函数 mySort，参数为一个列表，参数列表中的元素都是整数.
    mySort 函数需要将参数列表中的元素按从小到大排序，最终返回一个新的list。

思路分解：
    1. 创建一个新的列表newList
    2. 先找出所有元素中最小的，append在newList里面
    3. 再找出剩余的所有元素中最小的，append在newList里面
    4. 依次类推，直到所有的元素都放到newList里面

'''
#aList = [3,5,1,6,8]
# def mySort(List):
#     newList = []
#     for i in range(0,len(List)-1):
#         for j in range(0,len(List)-i-1):
#             if List[j] < List[j+1]:
#                 List[j],List[j+1] = List[j+1],List[j]
#         newList.append(List[-(i+1)])
#     newList.append(List[0])
#     return newList

aList = [3,5,1,6,8]
def mySort(inList):
    newList = []
    #循环不知道次数时用while
    while len(inList)>0:
        minData = min(inList)
        newList.append(minData)
        inList.remove(minData)
    return newList

# aList = [3,5,1,6,8]
# def mySort(inList):
#     newList = []
#     while len(inList)>0:
#         minData = inList[0]
#         minIndx = 0
#         indx = 0
#         #假设第一个值与列表中的值比较出最小
#         for one in inList:
#             if minData >one:
#                 minData = one#更新最小值
#                 minIndx = indx#更新最小值下标
#             indx += 1
#         #将最小值放入列表
#         newList.append(minData)
#         del inList[minIndx]#删除列表中的最小值
#     return newList
#
# print(mySort(aList))
