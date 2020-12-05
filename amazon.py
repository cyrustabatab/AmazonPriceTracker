from bs4 import BeautifulSoup
import requests
import lxml
import smtplib
import os
import re

my_email = "ENTER SENDING EMAIL HERE" #this application assumes a gmail and you might have to authorize Google to allow third party apps to access
to_email="ENTER RECEIVING EMAIL HERE"

headers = {"Accept-Language": 'en-US,en;q=0.9','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.47'}

url_to_price_limit ={'https://www.amazon.com/GoBroBrand-Green-Archery-Suction-Arrows/dp/B07HZ55HS9/ref=sr_1_3?dchild=1&keywords=bow+and+arrow+for+kids&qid=1607148870&sr=8-3': 200.0,"https://www.amazon.com/Logitech-M525-Wireless-Mouse-Micro-Precision/dp/B005KSAHZU/ref=sxts_sxwds-bia-wc-nc-drs1_0?cv_ct_cx=logitech+mouse&dchild=1&keywords=logitech+mouse&pd_rd_i=B005KSAHZU&pd_rd_r=53e1e857-d103-4e47-9d23-07d6d6bd4d00&pd_rd_w=L5o9s&pd_rd_wg=ipPLt&pf_rd_p=84ce0865-d9ca-42e3-87ed-168be8f93162&pf_rd_r=6HTCN39RWHNH78FCABHR&psc=1&qid=1607151386&s=electronics&sr=1-1-88388c6d-14b8-4f70-90f6-05ac39e80cc0": 200.00}


connection = smtplib.SMTP('smtp.gmail.com',port=587)
connection.starttls()
connection.login(user=my_email,password=os.environ.get('PASSWORD'))
price_regex = re.compile(r'^priceblock_')
for url,price_limit in url_to_price_limit.items():

    response = requests.get(url,headers=headers)

    soup = BeautifulSoup(response.content,'lxml')
    
    title_tag = soup.find('span',id='productTitle')
    price_tag= soup.find('span',id=price_regex)

    title = title_tag.getText().strip()
    price = float(price_tag.getText()[1:])

    connection.sendmail(from_addr=my_email,to_addrs=to_email,msg=f"Subject: AMAZON PRICE ALERT!\n\n{title} is now ${price}!\n{url}".encode('utf-8'))



connection.quit()














