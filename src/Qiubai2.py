#!/usr/bin/python3

import requests
import json
import re
import os
import os.path


def getPage(pageIndex):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36',
        'Cookie':'_xsrf=2|f1403dd8|a54707e41dd2c09468761034debac65d|1519789991; _ga=GA1.2.2122362483.1519789993; _gid=GA1.2.807588526.1519789993; Hm_lvt_2670efbdd59c7e3ed3749b458cafaa37=1519789995; _qqq_uuid_="2|1:0|10:1519803559|10:_qqq_uuid_|56:ZDk0MWY1MGI4MjkxMjE5ZWIwNjgzOTM4NTRiZGFhYjVmMGJjMjlhOA==|514e9aa3ae1fddcd1dc56be4760235d64a16a0a50746d91145a5fd44e68501df"; _gat=1; Hm_lpvt_2670efbdd59c7e3ed3749b458cafaa37=1519803564'}
        url = 'http://www.qiushibaike.com/hot/page/' + str(pageIndex)
        # 将页面转化为UTF-8编码
        pageCode =requests.get(url, headers,timeout=8).text

        return pageCode

    except (ValueError) as Argument:
        if hasattr(Argument, "reason"):
            print(u"连接糗事百科失败,错误原因", Argument.reason)
            return None


def getPageItems(pageIndex):
    pageCode = getPage(pageIndex)
    if not pageCode:
        print("页面加载失败...")
        return None
    pattern = re.compile(
        '<h2>(.*?)</h2>.*?<div class="content">.*?<span>(.*?)</span>.*?<div class="stats.*?class="number">(.*?)</i>',
        re.S)
    items = re.findall(pattern, pageCode)
    for item in items:
        yield {
            '作者': item[0].replace("</br>","").replace(r"\n",""),
            '段子内容': item[1].replace("</br>","").replace(r"\n",""),
            '点赞数': item[2].replace("<br/>","").replace(r"\n","")
        }

def write_to_file(content):
    with open('d:\糗百1.txt', 'a+', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
        f.close()

for x in range(1000):
    # f.write("111")
    try:
       for item in getPageItems(x+1):
           write_to_file(item)
    except (ValueError) as Argument:
        print("参数没有包含数字\n", Argument)
