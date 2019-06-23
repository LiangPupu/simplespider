import urllib.request


def get_font1(url):

    font_name = url[-9:]
    font_name = 'font/'+font_name
    urllib.request.urlretrieve(url, filename=font_name)
    return font_name

if __name__ == '__main__':
    url = "https://guyujiezi.com/fonts/40dXBL/3jZQSv.woff"
    print(get_font1(url))