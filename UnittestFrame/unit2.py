from smtplib import SMTP

from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from XTestRunner import HTMLTestRunner

class UnitTestCase2(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.bs = webdriver.Chrome('/Users/chenxiangming/Desktop/tools/chromedriver')

        # self.addCleanup(self.bs.quit())

    def testPageTitle2(self):
        self.bs.get('https://www.163.com')
        self.assertIn('网易', self.bs.title)

    def testclickElement2(self):
        self.bs.get('https://www.163.com')
        self.bs.find_element(By.XPATH, '//*[@id="js_index2017_wrap"]/div[2]/div[1]/div[2]/ul/li[1]/a[1]').click()
        self.bs.switch_to.window(self.bs.window_handles[1])  # 切换标签页
        self.assertIn('网易新闻', self.bs.title)
    @classmethod
    def tearDownClass(cls) -> None:
        cls.bs.close()


class UnitTestCaseScope(unittest.TestCase):
    '''前置用例执行顺序，setUpClass所有用例执行前执行，setUp每个用例都执行一遍'''
    @classmethod
    def setUpClass(cls) -> None:
        print('此类用例执行开始')
    @classmethod
    def tearDownClass(cls) -> None:
        print('此类用例执行结束')

    def setUp(self) -> None:
        print('用例执行开始')

    def tearDown(self) -> None:
        print('此用例执行结束')

    def testTitle(self):
        print('用户登陆')

    def testPageTitle(self):
        print('用例2')
