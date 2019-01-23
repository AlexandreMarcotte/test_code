# import urllib.request     # import urlopen as uReq
# import urllib.parse #as parse
from bs4 import BeautifulSoup as soup
import re
from urllib.request import Request, urlopen, FancyURLopener

#
# class AppURLopener(FancyURLopener):
#     version = "Mozilla/5.0"
#
# opener = AppURLopener()
# response = opener.open('http://httpbin.org/user-agent')
#
#
# # url='https://www.bitchute.com/channel/styxhexenhammer666/'
# # req = Request(url)
# # webpage = urlopen(req).read()
# # print(webpage)


import requests
hdrs = {'User-Agent': 'Mozilla / 5.0 (X11 Linux x86_64) AppleWebKit / 537.36 (KHTML, like Gecko) Chrome / 52.0.2743.116 Safari / 537.36'}

line_in_list = ['https://www.bitchute.com/channel/styxhexenhammer666/']

for url in line_in_list:
    resp = requests.get(url, headers=hdrs)
    print(resp.text)