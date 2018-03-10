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
        pageCode =requests.get(url, headers,timeout=8).content.decode(encoding="utf-8")

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
    pageStories = []
    for item in items:
        pageStories.append([item[0].strip(), item[1].strip(), item[2].strip()])
    return pageStories


for x in range(1000):
    # f.write("111")
    try:
        pageStories = getPageItems(x + 1)
        with open("d:\糗百.txt", "a+", encoding='utf-8') as f:
            for story in pageStories:
                f.write("作者:{}\n\n".format(story[0]))
                f.write("段子内容:\n{}\n".format(story[1]).replace("<br/>", "\n"))
                f.write("点赞数:{}\n\n".format(story[2]))
    except (ValueError) as Argument:
        print("参数没有包含数字\n", Argument)
