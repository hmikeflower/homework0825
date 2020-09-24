import sys
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def geturl(url_one):
    clist = []
    resp = requests.get(url_one)
    soup = BeautifulSoup(resp.text,"html.parser")   
    all_a_tag = soup.find_all('a')
   
    for a_tag in all_a_tag:
        href = a_tag.get("href")
        re_url = urljoin(url_one, href)
        clist.append(re_url)

    return clist       

def cheackURl(cheacklist): #檢查URL 是否重複
    newURL= []
    for cheack in cheacklist :
        if cheack  not in newURL :
            newURL.append(cheack)
       
    return newURL 


if __name__ == "__main__":

    nums = sys.argv
    url = nums[1]
    count =int(nums[2])
    a = 0
    
    allset = set()
    cotlist = [url]
    tmp_urls = []
    
     
    
    for i in range(count):
        print("level:", i+1)
        tmpJobs = []
        
        for cot in cotlist: 
            if cot in cotlist :                     #檢查重複? 
                print("get ", cot, "'s hyperlinks") #執行第一次時cotlist 裡面是外部輸入的URL
                hyperlinks = geturl(cot)            #運行函式得到一個或多個新的網址
                tmpJobs.extend(hyperlinks)          #更新tmpJobs 
                allset.update(hyperlinks)              #更新alllist
        cotlist = tmpJobs                       #更新cotlist 運行第二次時 就會跑新的URL


alllist =list(allset)
for pr in alllist:
    a +=1
    print(a,pr)

print(len(allset))
