print('')
import requests
from lxml import etree
#to whom(发送给谁)
url=('http://www.loying.cc/book/douluo/15237.html')
while True:
     #pretend self（伪装自己）
     headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'}
     #send request（发送请求）
     resp=requests.get(url,headers=headers)
     #set encodeing（设置编码）
     resp.encoding='utf-8'
     #respondse information（响应信息）
     e=etree.HTML(resp.text)
     #(处理格式)
     info='\n'.join(e.xpath('//div/p/text()'))
     title=e.xpath('//h3/text()')[0]
     url=f'http://www.loying.cc{e.xpath("//article/nav/ul/li[2]/a/@href")[0]}'
     #(输出)
     #print(title)
     #print(info)
     #reserve（保存）
     with (open('斗罗大陆.text','a',encoding='utf-8') as f):
          f.write(title+'\n\n'+info+'\n\n')