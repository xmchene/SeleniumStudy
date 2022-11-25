from selenium import webdriver
from selenium.webdriver.common.by import By
import os
print(os.path.dirname('..'))
bs = webdriver.Chrome('/Users/chenxiangming/Desktop/tools/chromedriver')
bs.get('http://www.163.com')
title = bs.title  # 打印网页标题
bs.find_element(By.XPATH, '//*[@id="js_index2017_wrap"]/div[2]/div[1]/div[2]/ul/li[1]/a[1]').click()
