
from selenium import webdriver
import time
wd = webdriver.Chrome()
wd.implicitly_wait(8)

wd.get('http://10.100.185.10:8084/#/homePage/main')
time.sleep(2)

zy = wd.find_elements_by_xpath('//a//span')
for element in zy:
    if '数据挖掘' in element.text:
        element.click()

sj = wd.find_element_by_xpath("//div//*[@class='ant-btn arrows-right-type ant-btn-default ant-btn-icon-only']")
for i in range(2):
    time.sleep(2)
    sj.click()


wd.find_element_by_css_selector('.ant-select-selection__rendered').click()
sj1 = wd.find_elements_by_xpath("//div//ul[@class='ant-select-dropdown-menu ant-select-dropdown-menu-root ant-select-dropdown-menu-vertical']//li")
for element in sj1:
    if '娄邵' in element.text:
        element.click()

time.sleep(2)
wd.find_element_by_xpath("//div//*[@href='svc/api/data-analysis/export?zone=ls']").click()


xn = wd.find_elements_by_xpath('//a//span')
for element in zy:
    if '消纳评估' in element.text:
        element.click()

time.sleep(2)

wd.find_elements_by_xpath('//span//i//*[@class="ng-tns-c19-22"]').click()
xn1 = wd.find_elements_by_xpath("//div//ul[@class='ant-select-dropdown-menu ant-select-dropdown-menu-root ant-select-dropdown-menu-vertical']")
for element in zy:
    if '日内' in element.text:
        element.click()

time.sleep(2)

wd.find_elements_by_css_selector('button[_ngcontent-iyp-c28]').click()

zy = wd.find_elements_by_xpath('//a//span')
for element in zy:
    if '设置' in element.text:
        element.click()


