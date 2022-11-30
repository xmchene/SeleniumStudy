#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import re
import pytest
import unittest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By


@allure.feature("测试百度模块")
class TestSearch:
    @pytest.fixture(scope='function', autouse=True)
    def open_baidu(self):
        """打开百度"""
        self.bs = webdriver.Chrome('/Users/chenxiangming/Desktop/tools/chromedriver')
        self.bs = webdriver.Chrome('/Users/chenxiangming/Desktop/tools/chromedriver')

    @allure.story("搜索selenium结果用例")
    def test_001(self):
        """搜索"""
        self.bs.get('https://www.163.com')
        # self.assertIn('网易', self.bs.title)
        assert '网易' in self.bs.title
    # @allure.story("测试搜索候选用例")
    # def test_002(self, drivers):
    #     """测试搜索候选"""
    #     search = SearchPage(drivers)
    #     search.input_search("selenium")
    #     log.info(list(search.imagine))
    #     assert all(["selenium" in i for i in search.imagine])


if __name__ == '__main__':
    pytest.main(['test_AllureReport.py', '--alluredir', './allure'])
    os.system('allure serve allure')
