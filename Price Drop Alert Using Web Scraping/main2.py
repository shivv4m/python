from bs4 import BeautifulSoup
import requests
import lxml
import smtplib
import pprint
import re
import os
from dotenv import load_dotenv
load_dotenv()
MY_EMAIL=os.getenv("MY_EMAIL")
MY_PASSWORD=os.getenv("MY_PASSWORD")
SEND_EMAIL=os.getenv("SEND_EMAIL")
header = {
"Accept-Language": "en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,mr;q=0.6,hi;q=0.5",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
}
#practice_url = "https://appbrewery.github.io/instant_pot/"
live_url = "https://www.amazon.in/gp/aw/d/B00FLYWNYQ/?_encoding=UTF8&pd_rd_plhdr=t&aaxitk=737b2d0600cf26b5065f60183fdfec2b&hsa_cr_id=0&qid=1744995246&sr=1-1-e0fa1fdd-d857-4087-adda-5bd576b25987&ref_=sbx_be_s_sparkle_dlcd_asin_0_img&pd_rd_w=tATT9&content-id=amzn1.sym.df9fe057-524b-4172-ac34-9a1b3c4e647d%3Aamzn1.sym.df9fe057-524b-4172-ac34-9a1b3c4e647d&pf_rd_p=df9fe057-524b-4172-ac34-9a1b3c4e647d&pf_rd_r=K2TKS7150B0EKQ20NETN&pd_rd_wg=U1CdI&pd_rd_r=6b5c588d-4159-4ece-8e9d-460dd448534f&th=1"
response = requests.get(url=live_url, headers=header)
soup = BeautifulSoup(response.content, 'lxml')

price = soup.find(name="span", class_='a-price-whole')
price = float(price.text.replace(",", "").rstrip("."))
target_price = float(12000.00)
title = soup.find(id="productTitle").getText().strip()
if price < target_price:
    message = f"{title} is on sale for {price}"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=SEND_EMAIL,
                            msg=f"Subject:Price Drop Alert!\n\n{message}\n{live_url}".encode("utf-8"))