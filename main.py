'''
Author: ferried
Email: harlancui@outlook.com
Date: 2020-12-06 18:16:27
LastEditTime: 2020-12-06 18:19:59
LastEditors: ferried
Description: Basic description
FilePath: /py-selenium-demo/main.py
LICENSE: Apache-2.0
'''

from firefox import FirefoxBrowser


if __name__ == "__main__":
    firefox = FirefoxBrowser()
    firefox.open("http://www.baidu.com")
    firefox.shortcut()
    
