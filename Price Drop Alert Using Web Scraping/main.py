from bs4 import BeautifulSoup
import requests
import lxml
import smtplib
import os
from dotenv import load_dotenv
load_dotenv()

MY_EMAIL=os.getenv("MY_EMAIL")
MY_PASSWORD=os.getenv("MY_PASSWORD")
SEND_EMAIL=os.getenv("SEND_EMAIL")

header = {"User Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36", "Accept-Language": "en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,mr;q=0.6,hi;q=0.5"}
practice_url = "https://appbrewery.github.io/instant_pot/"
live_url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
response = requests.get(url=practice_url, headers=header)
soup = BeautifulSoup(response.content, 'html.parser')
price = soup.find(name="span", class_='a-price-whole')
fraction = soup.find(name="span", class_='a-price-fraction')
price_as_float = float(price.text+fraction.text)
TARGET_PRICE = float(100.00)

title = soup.find(id="productTitle").getText().strip()
if(price_as_float < TARGET_PRICE):
    message = f"{title} is on sale for {price_as_float}"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=SEND_EMAIL,
                            msg=f"Subject:Price Drop Alert!\n\n{message}\n{live_url}".encode("utf-8"))
