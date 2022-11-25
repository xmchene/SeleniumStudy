import os

import pytest
import allure
@allure.feature('测试模块')
class TestScopeClass:
    @allure.story('测试用例1')
    def test_one(login):
        print('测试用例1')
    @allure.story('测试用例2')
    def test_two(self):
        print('测试用例2')
    @allure.story('测试用例3')
    def test_three(login):
        print('测试用例3')


if __name__ == '__main__':
    pytest.main(['test_Scope.py', '--alluredir', './allure', '-s', '-v'])
    os.system('allure serve allure')

# def test_one(login):
#     print('测试用例1')
#
#
# def test_two():
#     print('测试用例2')
#
#
# def test_three(login):
#     print('测试用例3')
