# from selenium import webdriver
# import os
#
# dr = webdriver.Chrome()
# dr.maximize_window()
# dr.get("https://www.baidu.com")
# # #dr.find_element_by_link_text("登录").click()
# # #dr.implicitly_wait(5)
# # #dr.find_element_by_link_text("立即注册").click()
# # cookie = dr.get_cookies()
# # print(cookie)
import unittest
class TestCount(unittest.TestCase):

    def setUp(self):
        pass
    def test_add(self):
        pass
    def tearDown(self):
        pass
if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestCount("test_add"))
    runner = unittest.TextTestRunner()
    runner.run(suite)