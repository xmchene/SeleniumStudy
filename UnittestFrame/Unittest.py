from smtplib import SMTP

from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By

class UnitTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.bs = webdriver.Chrome('/Users/chenxiangming/Desktop/tools/chromedriver')
        # self.addCleanup(self.bs.quit())

    def testPageTitle(self):
        self.bs.get('https://www.163.com')
        self.assertIn('网易', self.bs.title)
        self.a
    def testclickElement(self):
        self.bs.get('https://www.163.com')
        self.bs.find_element(By.XPATH, '//*[@id="js_index2017_wrap"]/div[2]/div[1]/div[2]/ul/li[1]/a[1]').click()
        self.bs.switch_to.window(self.bs.window_handles[1])  # 切换标签页
        self.assertIn('网易新闻', self.bs.title)

    def tearDown(self) -> None:
        self.bs.close()



