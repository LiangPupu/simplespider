from selenium import webdriver
from test.代理ip.get_proxies1 import get_proxies
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from lxml import etree


ip_port = get_proxies()
url = '--proxy-server=http://'+ip_port

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument(url)

browser = webdriver.Chrome(chrome_options=chromeOptions)
browser.maximize_window()  # 最大化窗口
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
        url = "http://glidedsky.com/level/web/crawler-basic-2?page={}"
        url = url.format(i)
        browser.get(url)
        try:
            # print(browser.page_source)  # 输出网页源码
            html = etree.HTML(browser.page_source)
            nums = html.xpath("//div[contains(@class, 'col-md-1')]/text()")
            for num in nums:
                sum += int(num)
            print(sum)
        except Exception as e:
            print(str(e))

login()
