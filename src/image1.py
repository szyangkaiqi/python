import requests
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
import uuid
import urllib.request


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
num =0
for i in range(1, 3):

    url = "https://www.uumnt.cc/zt/rentiyishu/{}.html".format( str(i))
    r = requests.get(url, headers=headers)

    bsObj = BeautifulSoup(r.text, "html.parser")  # urllib.request不需要加`.text`
    imageList = bsObj.select(".clearfix a.taglisthtitle")

    for img in imageList:
        for subPageNum in  range(1,10):
            urlPath = str(img['href'])
            subName =str(urlPath.split("/")[-1]).split(".")[0]
            sbuUrl = "/".join(urlPath.split("/")[0:-1])+"/"+subName+"_{}.html".format(subPageNum)
            sbuUrl = "https://www.uumnt.cc{}".format(sbuUrl)
            print(sbuUrl)
            res =requests.get(sbuUrl, headers=headers)
            # print(res.status_code)
            if res.status_code != 200:
                continue

            subImageList = BeautifulSoup(res.text, "html.parser").select(".bg-white a img[src^=https]")
            for subimg in subImageList:
                if subimg['src'].find("/Pics/") ==-1:
                    continue
                num =num+1
                # print(subimg['src'])
                urlretrieve(subimg['src'], "d:\\test\\{}.jpg".format(num))  # Python自带的保存多媒体文件的方法


