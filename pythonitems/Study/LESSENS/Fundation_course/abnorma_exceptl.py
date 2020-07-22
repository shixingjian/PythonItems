# auther:shixingjian  time:2020/6/25/0025
import traceback
while True:
    num = input("请输入数字：")
    try:
        print('100/%s = %s' % (num,100/int(num)))
    # except ZeroDivisionError:
    #     print("不要输入0，请重新输入")
    # except ValueErro r as err:
    #     print('请输入数值！',err)
    # except Exception as err:
    #     print("异常，同一处理",err)
    except:
        print('统一处理异常',traceback.format_exc())