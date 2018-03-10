#!/usr/bin/python3

import urllib.request
import re
import os
import os.path


def getPage(pageIndex):
    try:
        headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
        url = 'http://www.qiushibaike.com/hot/page/' + str(pageIndex)
        # 构建请求的request
        request = urllib.request.Request(url, headers=headers)
        # 利用urlopen获取页面代码
        response = urllib.request.urlopen(request)
        # 将页面转化为UTF-8编码
        pageCode = response.read().decode('utf-8')
        print(pageCode)
        return pageCode

    except urllib.request.URLError as e:
        if hasattr(e, "reason"):
            print(u"连接糗事百科失败,错误原因", e.reason)
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


for x in range(1):
    # f.write("111")
    try:
        pageStories = getPageItems(x + 1)
        with open("d:\糗百.txt", "w+", encoding='utf-8') as f:
            for story in pageStories:
                f.write("作者:{}\n\n".format(story[0]))
                f.write("段子内容:\n{}\n".format(story[1]).replace("<br/>", "\n"))
                f.write("点赞数:{}\n\n".format(story[2]))
                f.flush()
    except (ValueError) as Argument:
        print("参数没有包含数字\n", Argument)
