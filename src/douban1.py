import requests
from urllib.request import urlretrieve
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
for i in range(1, 51):
    url = "https://ypy.douban.com/package?page=" + str(i)
    r = requests.get(url, headers=headers)
    print(r.text)
    bsObj = BeautifulSoup(r.text, "html.parser")  # urllib.request不需要加`.text`
    imagesSet = bsObj.findAll("a", {"class": "lnk-pic-card"})
    print(imagesSet)
    for image in imagesSet:
        photoUrl = "https://ypy.douban.com" + image["href"]
        r1 = requests.get(photoUrl, headers=headers)
        bsObj1 = BeautifulSoup(r1.text, "html.parser")
        images = bsObj1.findAll("div", {"class": "pic-wrapper"})
        print(images)
        for image1 in images:
            photoName = image1.img.attrs["data-src"][28:] + ".jpg"  # 创造独一无二的文件名
            print(photoName)
            urlretrieve(image1.img.attrs["data-src"], photoName)  # Python自带的保存多媒体文件的方法
    print(i)  # 打印下载的页数信息
