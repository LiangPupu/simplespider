from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from lxml import etree
import time
import re


# ip_port = get_proxies()
# print(ip_port)

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument('--headless')

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
    result = 0
    for i in range(1, 1001):
        url = "http://glidedsky.com/level/web/crawler-css-puzzle-1?page={}"
        url = url.format(i)
        browser.get(url)
        # print(browser.page_source)  # 输出网页源码
        html = etree.HTML(browser.page_source)
        divlist = html.xpath("//div[contains(@class, 'col-md-1')]")
        for div in divlist:
            divs = div.xpath('./div')
            # 小于3，有两种情况，一种是两位数，一种是在css:content里面
            if len(divs) < 3:
                for div in divs:
                    text = div.xpath('./text()')
                    if len(text) == 0:
                        break
                # css:content里面
                if len(text) == 0:
                    classname = div.xpath('./@class')[0]
                    num = re.findall(r"\.{}\:before\s*.*?\s*content\:\"(\d*)\"".format(classname), browser.page_source, re.S)[0]
                    result += int(num)
                    print(num)
                else:
                    # 两位数
                    num1 = [-1, -1]
                    for i in range(0, len(divs)):
                        classname = divs[i].xpath('./@class')[0]
                        data = divs[i].xpath('./text()')[0]
                        left = re.findall(r"\.{}\s.*?\sleft\:(.*?)em".format(classname), browser.page_source)

                        if not left:
                            num1[i] = data
                        else:
                            num1[i + int(left[0])] = data
                    number = ''.join(num1)
                    print(number)
                    result += int(number)
                continue
            # 个数为3也有两种情况，一种是只有两位数，一种是3位数
            if len(divs) == 3:
                for i in range(0, len(divs)):
                    classname = divs[i].xpath('./@class')[0]
                    # print(classname)
                    magin_right = re.findall(r"\.{}\s.*?\smargin-right(.*?)em".format(classname),
                                             browser.page_source)

                    # 两位数情况，第一位假数据
                    if len(magin_right):
                        # print(magin_right)
                        divs = divs[1:]
                        break
                if len(divs) == 2:
                    num1 = [-1, -1]
                    for i in range(0, len(divs)):
                        classname = divs[i].xpath('./@class')[0]
                        data = divs[i].xpath('./text()')[0]
                        left = re.findall(r"\.{}\s.*?\sleft\:(.*?)em".format(classname), browser.page_source)

                        # 有left 说明位置需要变动
                        if not left:
                            num1[i] = data
                        else:
                            num1[i + int(left[0])] = data
                    number = ''.join(num1)
                    print(number)
                    result += int(number)
                    continue
            # 长度为4 第1位为假数据
            if len(divs) == 4:
                divs = divs[1:]
            num1 = [-1, -1, -1]

            for i in range(0, len(divs)):
                classname = divs[i].xpath('./@class')[0]
                data = divs[i].xpath('./text()')[0]
                left = re.findall(r"\.{}\s.*?\sleft\:(.*?)em".format(classname), browser.page_source)

                if not left:
                    num1[i] = data
                else:
                    num1[i+int(left[0])] = data
            number = ''.join(num1)
            print(number)
            result += int(number)
        print(f'结果是：{result}')

    browser.quit()


login()