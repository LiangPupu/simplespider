from selenium import webdriver
# from get_proxies1 import get_proxies
from selenium.webdriver.common.by import By
from get_font import get_font1
from woff_to_str import cur_num
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from lxml import etree
import re


chromeOptions = webdriver.ChromeOptions()
# chromeOptions.add_argument('--headless')

browser = webdriver.Chrome(chrome_options=chromeOptions)

wait = WebDriverWait(browser, 10) # 等待加载10s



def login():
    browser.get('http://glidedsky.com/login')
    input = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//input[contains(@id, 'email')]")))
    input.send_keys('1094122757@qq.com')
    input = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//input[contains(@id, 'password')]")))
    input.send_keys('tXtf5QtptygEzjh')
    submit = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[contains(@class, 'btn')]")))
    submit.click() # 点击登录按钮
    get_page_index()

def get_page_index():
    sum = 0
    for i in range(1, 1001):
        url = "http://glidedsky.com/level/web/crawler-font-puzzle-1?page={}"
        url = url.format(i)
        browser.get(url)
        # try:
        # print(browser.page_source)  # 输出网页源码
        html = etree.HTML(browser.page_source)
        fonts = html.xpath("//style/text()")[0]
        font_url = fonts.split('\n')[3].split("\"")[1]
        print(font_url)
        font_name = get_font1(font_url)

        nums = html.xpath("//div[contains(@class, 'col-md-1')]/text()")
        for num in nums:
            print(num)
            cn = cur_num(num.strip(), font_name)
            print(cn)
            sum += int(cn)
        print(sum)
        # except Exception as e:
        #     print(str(e))

login()