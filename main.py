# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import unittest

# import UnittestFrame.Unittest
#from UnittestFrame.Unittest import UnitTestCase
from UnittestFrame.unit2 import UnitTestCase2
from UnittestFrame.unit2 import UnitTestCaseScope
from XTestRunner import HTMLTestRunner


if __name__ == '__main__':
    report = "./selenium_result.html"
    # suit = unittest.TestSuite()
    # suit.addTest(unittest.TestLoader().loadTestsFromModule([UnittestFrame.Unittest]))
    with(open(report, 'wb')) as fp:
        unittest.main(testRunner=HTMLTestRunner(
            stream=fp,
            title='Selenium自动化测试报告',
            description=['类型：selenium', '操作系统：Windows', '浏览器：Chrome', '执行人：陈湘明']
        ))
    smtp = SMTP(user="xmchene@163.com", password="xp101FUwMF<.,", host="smtp.163.com")
    smtp.sender(to="103529625@qq.com", subject="XTestRunner测试邮件", attachments=report)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
