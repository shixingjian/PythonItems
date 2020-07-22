@echo off
echo 环境初始化开始
@echo on
del /f /s /q F:\pythonitems\Pytest_Auto_Test\report\tmp\*.json
del /f /s /q F:\pythonitems\Pytest_Auto_Test\report\tmp\*.jpg
del /f /s /q F:\pythonitems\Pytest_Auto_Test\report\report
@echo off
echo 环境初始化完成
@echo on

cd F:\pythonitems\Pytest_Auto_Test\testCase
pytest -sq --alluredir=../report/tmp
allure generate ../report/tmp -o ../report/report --clean

@echo off
echo 接口自动化运行成功
pause