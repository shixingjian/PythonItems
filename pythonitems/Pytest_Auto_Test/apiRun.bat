@echo off
echo ������ʼ����ʼ
@echo on
del /f /s /q F:\pythonitems\Pytest_Auto_Test\report\tmp\*.json
del /f /s /q F:\pythonitems\Pytest_Auto_Test\report\tmp\*.jpg
del /f /s /q F:\pythonitems\Pytest_Auto_Test\report\report
@echo off
echo ������ʼ�����
@echo on

cd F:\pythonitems\Pytest_Auto_Test\testCase
pytest -sq --alluredir=../report/tmp
allure generate ../report/tmp -o ../report/report --clean

@echo off
echo �ӿ��Զ������гɹ�
pause