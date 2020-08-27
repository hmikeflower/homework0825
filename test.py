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
print(resp)


