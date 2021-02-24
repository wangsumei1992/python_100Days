from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep

dr = webdriver.Chrome()
dr.maximize_window()
#dr.set_window_size(480,800)
dr.get("https://www.baidu.com")
dr.find_element_by_id("kw").send_keys("seleniumm")
dr.implicitly_wait(10)
#sleep(10)
dr.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)
# dr.find_element_by_id("kw").send_keys("指数基金")
# dr.find_element_by_name("wd").send_keys("wangsumei")
# dr.find_element_by_class_name("s_ipt").send_keys("hengniu")
#dr.find_element_by_link_text("新闻").click()
dr.find_element_by_xpath("//input[@id='su']").click()
# dr.refresh()
# dr.back()
# dr.quit()
ele = dr.find_element_by_id("s-usersetting-top")
ActionChains(dr).move_to_element(ele).perform()
dr.find_element_by_link_text("高级搜索").click()
#dr.find_element_by_xpath("//*[@id='s-user-setting-menu']/div/a[1]").click()
# dr.quit()