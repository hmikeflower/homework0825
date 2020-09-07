import sys
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def geturl(url_one):
    resp = requests.get(url_one)
    soup = BeautifulSoup(resp.text,"html.parser")   
    all_a_tag = soup.find_all('a')
    #baseURL = url_one
    clist = []
    for a_tag in all_a_tag:
        href = a_tag.get("href")
        re_url = urljoin(url_one, href)
        clist.append(re_url)

    return clist       


if __name__ == "__main__":

    nums = sys.argv
    url = nums[1]
    count =int(nums[2])

#clist = []    #這邊有的話，會出錯。
    for cot in range(count):
        url_list = geturl(url)
    