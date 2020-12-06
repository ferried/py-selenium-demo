'''
Author: ferried
Email: harlancui@outlook.com
Date: 2020-12-06 18:17:01
LastEditTime: 2020-12-06 18:34:03
LastEditors: ferried
Description: Basic description
FilePath: /py-selenium-demo/firefox.py
LICENSE: Apache-2.0
'''

from selenium import webdriver  # 用于打开网站


class FirefoxBrowser:

    def __init__(self):
        self.driver = webdriver.Firefox()

    def open(self, url):
        self.driver.get(url)

    def shortcut(self):
        url = self.driver.current_url.replace('.', '').replace('/', '').replace('https', '').replace('http', '').replace(':', '').replace('?', '').replace('&', '')
        print(url)
        self.driver.save_screenshot('./assets/'+url+'.png')
