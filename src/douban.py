#!/usr/bin/python3
import requests
from requests.exceptions import RequestException
import re
import json


def get_one_page(url):
    try:
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36'
            ,
            'Cookie': 'bid=u6VdTrZU3ao; __utmz=30149280.1519695333.7.7.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmz=223695111.1519695333.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __yadk_uid=8sJcJyqmBstzMALrX2rS1FWq8vwDpfIK; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1519802417%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DrIzx5iOuL_VEVnavQA9cFx66Gm-hHrSr8jcy5CNR0HjsgckvCZgf-EZVju4ehq2KkveH941CVaQk-8PaXaCxMa%26wd%3D%26eqid%3De13bca5e00016e0b000000065a94b5ca%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.1781894267.1518280120.1519695333.1519802418.8; __utmb=30149280.0.10.1519802418; __utmc=30149280; __utma=223695111.363812300.1519695333.1519695333.1519802418.2; __utmb=223695111.0.10.1519802418; __utmc=223695111; ps=y; dbcl2="174723087:gZSvYgV3fdU"; ck=NLpC; push_noty_num=0; push_doumail_num=0; _pk_id.100001.4cf6=0f458a985b695c47.1519695331.2.1519803008.1519695331.; ap=1'
        }
        response = requests.get(url,headers)
        print(response.text)
        print(response.status_code)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def parse_one_page(html):
    pattern = re.compile('<table width=".*?<div class="pl2">.*?>(.*?)</a>.*?class="pl">(.*?)</p>'
                         + '.*?<span class="rating_nums">(.*?)</span>.*?class="pl">(.*?)</span>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'title': item[0].split("/")[0],
            'time': item[1].split("/")[0],
            'actor': item[1].split("/")[1:],
            'average': item[2],
            'content': item[3],
        }


def write_to_file(content):
    with open('d:\2016.txt', 'a+', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
        print(json.dumps(content, ensure_ascii=False))
        f.close()


def main(start):
    url = 'https://movie.douban.com/tag/2016?start=' + str(start) + '&type=T'
    html = get_one_page(url)
    print(html)
    for item in parse_one_page(html):
        write_to_file(item)


if __name__ == '__main__':
    for i in range(84, 194):
        main(i * 20)
