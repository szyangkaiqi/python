import requests
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
import uuid
import urllib.request


def url_open(url):

    req = urllib.request.Request(url)

    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 5.1; rv:43.0) Gecko/20100101 Firefox/43.0')

    response = urllib.request.urlopen(req)
    html = response.read()

    return html


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
for i in range(1, 2):
    url = "http://www.umei.cc/meinvtupian/xingganmeinv/{}.htm".format( str(i))
    r = requests.get(url, headers=headers)

    bsObj = BeautifulSoup(r.text, "html.parser")  # urllib.request不需要加`.text`
    imageList = bsObj.select(".TypeBigPics")
    image_num=0
    for x in imageList:
        for subPageNum in  range(1,40):
            image_num = image_num+1
            urlPath = str(x['href'])
            subName =str(urlPath.split("/")[-1]).split(".")[0]
            urlPath = "/".join(urlPath.split("/")[0:-1])+"/"+subName+"_{}.htm".format(subPageNum)

            res = requests.get(urlPath, headers=headers)
            if res.status_code != 200:
                continue
            subBs = BeautifulSoup(res.text, "html.parser")  # urllib.request不需要加`.text`
            subImageList = subBs.select(".ImageBody p img")
            for imgIndex in subImageList:
                # requests.request.urlopen(imgIndex['src']).red()
                print(imgIndex['src'])
                urlretrieve(imgIndex['src'], "d:\\test\\{}.jpg".format(uuid.uuid1()),data=)  # Python自带的保存多媒体文件的方法
                # with open("d:\\test\\{}.jpg".format(uuid.uuid1()),'wb') as f:
                #     print(requests.get(imgIndex['src'],headers=headers).text)
                #     f.write(requests.get(imgIndex['src'],headers=headers).content)




