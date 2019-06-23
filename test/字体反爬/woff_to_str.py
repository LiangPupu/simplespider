import re
from fontTools.ttLib import TTFont
from get_font import get_font1

# font = TTFont('20xATf.woff') #打开本地的ttf文件
# gly_list = font.getGlyphOrder()
# gly_list = gly_list[2:]    # 前两个值不是，切片去掉
# gly = {}
# for i,num in enumerate(gly_list):
#     gly[num]=i
# print(gly)
#
# font_map = font.getBestCmap()
# print(gly_list)
# nums = {}
# for i,num in enumerate(font_map):
#     nums[i] = font_map[num]
# print(nums)
#
# str1 = '1234'
# new_str =''
# for s in str1:
#     new_str += str(gly[nums[int(s)]])
# print(new_str)


def cur_num(str1, woff_name):
    font = TTFont(woff_name)
    # print(type(font))
    gly_list = font.getGlyphOrder()
    gly_list = gly_list[2:]
    gly = {}
    for i, num in enumerate(gly_list):
        gly[num] = i
    # print(gly)

    font_map = font.getBestCmap()
    # print(gly_list)
    nums = {}
    for i, num in enumerate(font_map):
        nums[i] = font_map[num]
    # print(nums)
    new_str = ''
    for s in str1:
        new_str += str(gly[nums[int(s)]])

    return new_str


if __name__ == '__main__':
    url = "https://guyujiezi.com/fonts/40dXBL/3jZQSv.woff"
    font_name = get_font1(url)

    print(cur_num('915359',font_name))


