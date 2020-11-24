'''
Author: ferried
Email: harlancui@outlook.com
Date: 2020-11-24 13:47:50
LastEditTime: 2020-11-24 14:56:47
LastEditors: ferried
Description: Basic description
FilePath: /isee-verification-code/main.py
LICENSE: Apache-2.0
'''
import re  # 用于正则
import io
import pytesseract  # 用于图片转文字
from PIL import Image
from selenium import webdriver  # 用于打开网站
import time  # 代码运行停顿


class VerificationCode:

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.find_element = self.driver.find_element_by_css_selector

    def get_pictures(self):
        self.driver.get('http://jiaowu.tsc.edu.cn/tscjw/cas/login.action')  # 打开登陆页面
        self.driver.save_screenshot('pictures.png')  # 全屏截图
        page_snap_obj = Image.open('pictures.png')
        img = self.find_element('#randpic')  # 验证码元素位置
        '''username'''
        username = self.find_element('#yhmc')
        username.send_keys("123")
        '''password'''
        password = self.find_element('#yhmm')
        password.send_keys("123")
        time.sleep(1)
        location = img.location
        size = img.size  # 获取验证码的大小参数
        print("验证码图片大小:", size)
        left = location['x']
        print("左侧坐标:", left)
        top = location['y']
        print("顶部坐标:", top)
        right = left + size['width']
        print("右侧坐标:", right)
        bottom = top + size['height']
        print("下方坐标:", bottom)
        image_obj = page_snap_obj.crop((left, top, right, bottom))  # 按照验证码的长宽，切割验证码
        image_obj.show()  # 打开切割后的完整验证码
        self.driver.close()  # 处理完验证码后关闭浏览器
        return image_obj


if __name__ == "__main__":
    vc = VerificationCode()
    img = Image.open(vc.get_pictures(), mode='r')
    imgByteArr = io.BytesIO()
    img.save(imgByteArr, format='JPEG')
    imgByteArr = imgByteArr.getvalue()
    print(imgByteArr)
    pass
