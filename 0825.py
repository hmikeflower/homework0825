import sys
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from urllib.parse import urljoin


nums = sys.argv
url = nums[1]
count =int(nums[2])
baseURL = url
for a in range(count):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text,"html.parser")   #"html.parser" 是啥
    all_a_tag = soup.find_all('a')
    for a_tag in all_a_tag:
        href = a_tag.get("href") # 嘗試取得 <a> 裡的 href  屬性值
        b = urljoin(baseURL, href)
        print(b)
    else:
        url = href
        baseURL = url