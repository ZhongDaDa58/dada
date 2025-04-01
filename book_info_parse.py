from bs4 import BeautifulSoup
import json
import re
import sys


html_filename=sys.argv[1]

#获取HTML文档内容
with open(html_filename,"r",encoding="utf-8") as f:
    html_doc=f.read()

#使用html.parser解析HTML文档
bs=BeautifulSoup(html_doc,"html.parser")

#获取书籍id
#基于<script>中的JSON字符获取

book_info_json_str =bs.find("script",{"type":"application/ld+json"}).get_text()
book_info_json=json.loads(book_info_json_str)
book_url=book_info_json["url"]
book_id=book_url.split("/")[-2]
book_name=book_info_json["name"]

#获取文本
book_info_str=bs.find("div",{"id":"info"}).get_text()

book_price=re.search(r"定价:\s*(\S+)\n",book_info_str).group(1).strip()
book_author=re.search(r"作者:\s*(.*?)\n",book_info_str).group(1).strip()
book_isbn=re.search(r"ISBN:\s*(\S+)\n",book_info_str).group(1).strip()
book_publisher=re.search(r"出版社:\s*(\S+)\n",book_info_str).group(1).strip()
book_date=re.search(r"出版年:\s*(\S+)\n",book_info_str).group(1).strip()
book_rating=bs.find("strong",{"property":"v:average"}).text.strip()



book_info={
    "book_id":book_id,
    "book_name":book_name,
    "book_author":book_author,
    "book_isbn":book_isbn,
    "book_publisher":book_publisher,
    "book_price":book_price,
    "book_date":book_date,
    "book_rating":float(book_rating),
    }

json_filename=html_filename.replace(".html",".json")
with open(json_filename,"w",encoding="utf-8") as f:
    json.dump(book_info,f,ensure_ascii=False)

