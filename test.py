import sys
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from urllib.parse import urljoin

nums = sys.argv
url = nums[1]
count =int(nums[2])

clist = [url]
resp = requests.get(url)
soup = BeautifulSoup(resp.text,"html.parser")   #"html.parser" 是啥
all_a_tag = soup.find_all('a')

for a_tag in all_a_tag:
    baseURL = url
    href = a_tag.get("href")
    b_url = urljoin(baseURL, href)
    clist.append(b_url)
    print("111111",b_url)
    #~~~~~~~~~~~~~~~~~~~~~~~~~ 
    baseURL2 = b_url
    resp2 =requests.get(b_url)
    soup2 = BeautifulSoup(resp2.text,"html.parser")
    all_a_tag2 = soup2.find_all('a')
    for a_tag2 in all_a_tag2:
        href2 = a_tag2.get("href")
        b_url2 = urljoin(baseURL2, href2)
        print("22222222",b_url2)
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        baseURL3 = b_url2
        resp3 =requests.get(b_url2)
        soup3 = BeautifulSoup(resp3.text,"html.parser")
        all_a_tag3 = soup3.find_all('a') 
        