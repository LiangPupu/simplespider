from selenium import webdriver
from test.代理ip.get_proxies1 import get_proxies
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from lxml import etree
import time


# ip_port = get_proxies()
# print(ip_port)




def login(browser,wait):
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

def get_page_index():

    sum = 121971
    for i in range(50, 1001):
        url = '--proxy-server=http://' + get_proxies()

        chromeOptions = webdriver.ChromeOptions()
        chromeOptions.add_argument(url)

        # chromeOptions.add_argument('--headless')

        browser = webdriver.Chrome(chrome_options=chromeOptions)
        # browser.maximize_window()  # 最大化窗口
        wait = WebDriverWait(browser, 10)  # 等待加载10s
        login(browser, wait)

        url = "http://glidedsky.com/level/web/crawler-ip-block-1?page={}"
        print(i)
        url = url.format(i)
        browser.get(url)
        try:
            # print(browser.page_source)  # 输出网页源码
            html = etree.HTML(browser.page_source)
            nums = html.xpath("//div[contains(@class, 'col-md-1')]/text()")
            for num in nums:
                sum += int(num)
            with open('sum.txt', 'w') as f:
                f.writelines('第'+str(i)+"页，"+"累计："+str(sum))
            print(sum)
        except Exception as e:
            print(str(e))
        time.sleep(0.5)
        browser.quit()


get_page_index()
