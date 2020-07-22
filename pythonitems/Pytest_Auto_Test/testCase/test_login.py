#coding=utf8
# auther:shixingjian  time:2020/07/09
from lib.ApiLogin import LoginClass
import json
import pytest
from lib.GetYamlData import get_yaml_data
from lib.GetExcelData import get_excelData
import allure
@allure.feature('登录模块')#一级标题
@allure.story('登录接口')
@allure.title('登录接口用例')
@pytest.mark.login(order = 1)#定制化运行标签
@pytest.mark.parametrize('inData,expreValue',get_yaml_data())
def test_login(inData,expreValue):
    res = LoginClass().api_login(inData,getSession=False)
    assert res['retcode'] == json.loads(expreValue)['retcode']
    print("-----------runninglogintest---------")

@allure.story('登录界面')
@allure.description('截图效果')
def test_login_image():
    allure.attach.file(r'../data/test.jpg','这是附件截图名字',attachment_type=allure.attachment_type.JPG)

if __name__ == '__main__':
    pytest.main(['test_login.py','-s'])