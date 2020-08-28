import sys
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from urllib.parse import urljoin


nums = sys.argv
url = nums[1]
count =int(nums[2])
resp = requests.get(url)
soup = BeautifulSoup(resp.text,"html.parser")   #"html.parser" 是啥
all_a_tag = soup.find_all('a')
baseURL = url

for a_tag in all_a_tag:
        href = a_tag.get("href") # 嘗試取得 <a> 裡的 href  屬性值
        resp2 = requests.get(href)
        soup2 = BeautifulSoup(resp2.text,"html.parser")
        all_a_tag2 = soup2.find_all('a')
        for a_tag2 in all_a_tag2:
                href2 = a_tag2.get("href")
                a = urljoin(baseURL, href2) 
                
print(a)