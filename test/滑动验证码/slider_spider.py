from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from lxml import etree
import time


chromeOptions = webdriver.ChromeOptions()
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
        url = "http://glidedsky.com/level/web/crawler-captcha-1?page={}"
        url = url.format(i)
        html = slide_code(url)
        try:
            # print(browser.page_source)  # 输出网页源码
            html = etree.HTML(html)
            nums = html.xpath("//div[contains(@class, 'col-md-1')]/text()")
            for num in nums:
                sum += int(num)
            print(sum)
        except Exception as e:
            print(str(e))


def slide_code(url):
    browser.get(url)
    frame = wait.until(EC.frame_to_be_available_and_switch_to_it(
        (By.XPATH, "//iframe[contains(@id, 'tcaptcha_iframe')]")))

    button = wait.until(EC.presence_of_element_located((By.ID,'tcaptcha_drag_button')))
    ActionChains(browser).click_and_hold(button).perform()
    time.sleep(1)
    for i in [130,50,10,5,2,3,5,6,1,1,1,1]:
        ActionChains(browser).move_by_offset(xoffset=i, yoffset=0).perform()
    time.sleep(1)
    ActionChains(browser).release().perform()
    time.sleep(5)

    html = browser.page_source
    return html







login()