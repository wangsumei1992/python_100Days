from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time

driver = webdriver.Chrome()
# driver.get('https://www.baidu.com/')
# at = driver.find_element_by_id("kw").get_attribute('type')
# at1 = driver.find_element_by_id("kw").get_attribute('name')
# print(at, at1)
# driver.find_element_by_id("kw").send_keys("seleniumm")
# #删除多输入的一个m
# driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)
# #ctrl + a全选输入框内容
# driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'a')
# driver.get("https://www.baidu.com/")
# #获得当前句柄
# current_handle = driver.current_window_handle
# driver.find_element_by_link_text("登录").click()
# #获得当前打开所有窗口的句柄
# all_handles = driver.window_handles
# for handle in all_handles:
#     if handle != current_handle:
#         driver.switch_to.window(handle)
#         print("login now")
driver.get("http://www.youdao.com/")
cookie = driver.get_cookies()
print(cookie)


