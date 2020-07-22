#coding=utf8
# auther:shixingjian  time:2020/07/11
import yaml
import pprint
import json
def get_yaml_data():
    yamlurl = '../data/login.yaml'
    with open(yamlurl,'r',encoding='utf8') as fo:
        reslist = yaml.load(fo,Loader=yaml.FullLoader)
        dataList = []
        for one in reslist:
            dataList.append((json.dumps(one['data']),json.dumps(one['check'])))
        return dataList
print(get_yaml_data())