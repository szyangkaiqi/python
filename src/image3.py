import requests
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
import uuid
import urllib.request
import threading
import time


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
class MainThread(threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self)
        self.url = url

    def run(self):
        r = requests.get(self.url, headers=headers)
        bsObj = BeautifulSoup(r.text, "html.parser")  # urllib.request不需要加`.text`
        imageList = bsObj.select(".imgList2 ul li")

        for img in imageList:
            for subPageNum in range(1, 10):
                urlPath = str(img.select("a")[0]['href'])
                subName = str(urlPath.split("/")[-1]).split(".")[0]
                sbuUrl = "/".join(urlPath.split("/")[0:-1]) + "/" + subName + "_{}.html".format(subPageNum)
                tt1 = ImageListThread(sbuUrl)
                tt1.start()


class ImageListThread(threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self)
        self.url = url

    def run(self):
        res = requests.get(self.url, headers=headers)
        # print(res.status_code)
        if res.status_code != 200:
            print("url:{}不存在".format(self.url))
            return
        else:
            print("正常url:{}".format(self.url))


        subImageList = BeautifulSoup(res.text, "html.parser").select(".arcBody p a img[src^=http]")
        for subimg in subImageList:

            if subimg['src'].find("http://pic") == -1:
                continue
            th = SubImageThread(subimg['src'], uuid.uuid1())
            th.start()

class SubImageThread(threading.Thread):
    def __init__(self, url, num):
        threading.Thread.__init__(self)
        self.url = url
        self.num = num

    def run(self):
        try:
            urlretrieve(self.url, "d:\\test\\{}.jpg".format(self.num))  # Python自带的保存多媒体文件的方法
        except:
            pass



for i in range(1, 30):
    t = MainThread("http://www.5442.com/mingxing/list_2_{}.html".format(str(i)))
    t.start()
