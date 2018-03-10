from selenium import webdriver
from bs4 import BeautifulSoup
import time

browser = webdriver.Chrome("c:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe")
browser.get("https://news.baidu.com/")
bsObj = BeautifulSoup(browser.page_source, "html.parser")  # urllib.request不需要加`.text`
print(bsObj.select(".imgview"))
browser.close()
