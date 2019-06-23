import time
from urllib.request import urlretrieve
import subprocess
from selenium import webdriver


image_list = []
driver = webdriver.Chrome()
driver.get("http://www.amazon.com/War-Peace-Leo-Nikolayevich-Tolstoy/dp/1427030200")

driver.find_element_by_id("img-canvas").click()
time.sleep(5)

while "pointer" in driver.find_element_by_id("sitbReaderRightPageTurner").get_attribute("style"):
    driver.find_element_by_id("sitbReaderRightPageTurner").click()
    time.sleep(2)

    pages = driver.find_elements_by_xpath("//div[@class='pageImage']/div/img")

    for page in pages:
        image = page.get_attribute('src')
        image_list.append(image)
driver.quit()

for image in image_list:
    urlretrieve(image, 'page.jpg')
    p = subprocess.Popen(["tesseract", "page.jpg", "page"], stdout=subprocess.PIPE,stderr=subprocess.PIPE)

    f = open("./page.txt", "r")
    p.wait()
    print(f.read())