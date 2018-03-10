import requests
from urllib.request import urlretrieve
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}

url = "http://pic.sogou.com/pics/recommend?category=%B1%DA%D6%BD#%E5%85%A8%E9%83%A8%269"
r = requests.get(url, headers=headers)
print(r.text)
bsObj = BeautifulSoup(r.text, "lxml")  # urllib.request不需要加`.text`
imagesSet = bsObj.select(".TitleImage-imagePure")

print(imagesSet)
cou =0;
for image in imagesSet:
    cou = cou+1
    urlretrieve(image['src'], "d:\\test\\{}.jpg".format(cou))  # Python自带的保存多媒体文件的方法
