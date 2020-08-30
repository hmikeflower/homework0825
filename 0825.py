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

'''
題目的目標為考慮以下情境：

爬蟲程式的進入點為給一條 root URL 與想要抓幾層。

若指定抓１層的話，又假設 root 這個網頁裡面有三條網址
1. a
2. b
3. c
那麼期待印到螢幕上的總輸出會是４條網址：
- root
- a
- b
- c

若指定抓２層的話：
則需要爬蟲程式再分別去抓取 a、b、c 三個網頁中的超連結
故假設三個網頁裡分別各有 2 條超連結（以 .n 示意），則最後期待的輸出為：
- root
- a
- a.1
- a.2
- b
- b.1
- b.2
- c
- c.1
- c.2
------


但觀察程式碼，在抓第二層的時候，只會去抓取在第一層、最後得到的 href 值
故只會去抓 c 的網頁，最後的輸出只會剩下
- root
- a
- b
- c
- c.1
- c.2
就不滿足「貪婪的爬蟲程式」的需求囉

'''