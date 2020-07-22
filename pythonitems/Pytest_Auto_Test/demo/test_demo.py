#coding=utf8
# auther:shixingjian  time:2020/07/08
import pytest
import json
class TestOne:

    def test_001(self):
        assert 1 == 1

    def test_002(self):
        assert 1 == 1

if __name__ == '__main__':
    # pytest.main(['test_demo.py'-s'])
    str = '{"username":"auto","password":"sdfsdfsdf"}'
    print(json.loads(str))