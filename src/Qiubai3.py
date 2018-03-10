import requests
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
import uuid
import urllib.request
import threading
import time
import threadpool



def getPage(pageIndex):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36',
                   'Cookie':'_xsrf=2|f1403dd8|a54707e41dd2c09468761034debac65d|1519789991; _ga=GA1.2.2122362483.1519789993; _gid=GA1.2.807588526.1519789993; Hm_lvt_2670efbdd59c7e3ed3749b458cafaa37=1519789995; _qqq_uuid_="2|1:0|10:1519803559|10:_qqq_uuid_|56:ZDk0MWY1MGI4MjkxMjE5ZWIwNjgzOTM4NTRiZGFhYjVmMGJjMjlhOA==|514e9aa3ae1fddcd1dc56be4760235d64a16a0a50746d91145a5fd44e68501df"; _gat=1; Hm_lpvt_2670efbdd59c7e3ed3749b458cafaa37=1519803564'}

        url = 'http://www.qiushibaike.com/hot/page/' + str(pageIndex)
        rep = requests.get(url, headers,timeout=8)
        if rep.status_code!=200:
            print("url:{}不存在".format(url))
            return
        else:
            print("正常url:{}".format(url))
        bsObj = BeautifulSoup(rep.text, "html.parser")
        with open("d:\糗百.txt", "a+", encoding='utf-8') as f:
            f.write(bsObj.select("div.typs_long a.contentHerf div.content span")[0].text.replace("<br/>", "\n"))


    except (ValueError) as Argument:
        if hasattr(Argument, "reason"):
            print(u"连接糗事百科失败,错误原因", Argument.reason)
            return None

for i in range(1,1000):
    getPage(i)
