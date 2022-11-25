from selenium import webdriver
bs = webdriver.Chrome('/Users/chenxiangming/Desktop/tools/chromedriver')
bs.get('https://www.zhihu.com/explore')
bs.execute_script('window.scrollTo(0, document.body.scrollHeight)')
bs.execute_script('alert("To Bottom")')