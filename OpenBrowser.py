from selenium import webdriver

bs = webdriver.Chrome('/Users/chenxiangming/Desktop/tools/chromedriver')
bs.get('http://www.163.com')
title = bs.title #打印网页标题
if title == '网易':
    print('验证通过')
bs.close()