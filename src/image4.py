import requests
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
import uuid
import urllib.request
import threading
import time
import threadpool


def open_url(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
    }
    print(url)
    r = requests.get(url, headers=headers)
    if r.status_code != 200:
        return
    bsObj = BeautifulSoup(r.text, "html.parser")  # urllib.request不需要加`.text`
    imageList = bsObj.select(".imgList2 ul li")
    img_urls = []
    for img in imageList:
        for subPageNum in range(1, 31):
            urlPath = str(img.select("a")[0]['href'])
            subName = str(urlPath.split("/")[-1]).split(".")[0]
            sbuUrl = "/".join(urlPath.split("/")[0:-1]) + "/" + subName + "_{}.html".format(subPageNum)
            img_urls.append(sbuUrl)

    impPool = threadpool.ThreadPool(1)
    bb1 = threadpool.makeRequests(getImageList, img_urls)
    [impPool.putRequest(req) for req in bb1]
    impPool.wait()


def getImageList(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
    }
    res = requests.get(url, headers=headers)
    # print(res.status_code)
    if res.status_code != 200:
        print("url:{}不存在".format(url))
        return
    else:
        print("正常url:{}".format(url))
    img_1_list = []
    subImageList = BeautifulSoup(res.text, "html.parser").select(".arcBody p a img[src^=http]")
    for subimg in subImageList:
        if subimg['src'].find("http://pic") == -1:
            continue
        img_1_list.append(subimg['src'])

    imagePool = threadpool.ThreadPool(1)
    bb2 = threadpool.makeRequests(downImage, img_1_list)
    [imagePool.putRequest(req) for req in bb2]
    imagePool.wait()


def downImage(url):
    try:
        urlretrieve(url, "d:\\test\\{}.jpg".format(uuid.uuid1()))  # Python自带的保存多媒体文件的方法
    except:
        pass


urls = []
for i in range(1, 301):
    urls.append("http://www.5442.com/mingxing/list_2_{}.html".format(str(i)))

pool = threadpool.ThreadPool(1)
bb = threadpool.makeRequests(open_url, urls)
[pool.putRequest(req) for req in bb]
pool.wait()
