import requests
from bs4 import BeautifulSoup
import sys
import json
import re
from datetime import datetime
headers={"user-agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:136.0) Gecko/20100101 Firefox/136.0"}
comment_data=[]
new_urls=[]
star=""

def turnToStamp(time):
    dt=datetime.strptime(time,'%Y-%m-%d %H:%M:%S')
    timestamp=int(dt.timestamp())
    return timestamp



comment_count=int(sys.argv[2])
url=sys.argv[1]
page=0
final=comment_count//20
leav=comment_count%20

while comment_count-20>-20:
    new_start="?start="+str(page)
    new_url=new_url=url+new_start+"&limit=20&status=P&sort=score"
    new_urls.append(new_url)
    page+=20
    comment_count-=20

print(new_urls)

#遍历获得的url
for new_url in new_urls:
    resp=requests.get(new_url,headers=headers)
    resp.status_code

    bs=BeautifulSoup(resp.text,"html.parser")
    comment_items=bs.find_all("li",{"class":"comment-item"})



    print(new_url)
    print(resp.status_code)
#print(bs)
#print(comment_items)
    if(new_url==new_urls[-1]  and leav!=0):
        for item in comment_items[0:leav]:
            comment_id=item["data-cid"]
            comment_time=item.find("a",{"class":"comment-time"}).get_text()
            comment_username=item.find("div",{"class":"avatar"}).find("a")["title"]
            
            #comment_rating=item.find("span",{"class":r"user-stars allstar.. rating"})["title"]
            comment_content=item.find("span",{"class":"short"}).get_text()
            comment_useful=item.find("span",{"class":"vote-count"}).get_text()

            comment={
                    "comment_id":comment_id,
                    "comment_username":comment_username,
                    "comment_time":turnToStamp(comment_time),
                   # "r":comment_rating,
                    "comment_content":comment_content,
                    "comment_useful":int(comment_useful),


                    }
            comment_data.append(comment)
            print("ok")
    else:
        for item in comment_items:

            comment_id=item["data-cid"]
            comment_time=item.find("a",{"class":"comment-time"}).get_text()
            comment_username=item.find("div",{"class":"avatar"}).find("a")["title"]

           # comment_rating=item.find("span",{"class":"user-stars allstar/* rating"})["title"]
            comment_content=item.find("span",{"class":"short"}).get_text()
            comment_useful=item.find("span",{"class":"vote-count"}).get_text()

            comment={
                    "comment_id":comment_id,
                    "comment_username":comment_username,
                    "comment_time":turnToStamp(comment_time),
                   # "r":comment_rating,
                    "comment_content":comment_content,
                    "comment_useful":int(comment_useful),


                    }
    page+=20
    comment_count-=20


with open(sys.argv[3],"w",encoding="utf-8") as f:
    json.dump(comment_data,f,ensure_ascii=False)
