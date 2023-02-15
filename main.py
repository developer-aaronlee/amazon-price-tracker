import requests
from bs4 import BeautifulSoup
import smtplib

my_email = "pythonautomationapp@gmail.com"
password = "dxabiogqxlleamrw"

amazon_url = "https://www.amazon.com/2022-Apple-iPad-10-9-inch-Wi-Fi/dp/B09V3HN1KC/ref=sr_1_3?crid=" \
             "HFXQMWBTRAKV&keywords=iPad+Air&qid=1660613755&sprefix=ipad+air%2Caps%2C78&sr=8-3"

amazon_headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0",
    "Accept-Language": "en-US"
}

response = requests.get(url=amazon_url, headers=amazon_headers)
amazon_page = response.text

soup = BeautifulSoup(amazon_page, "html.parser")
title = soup.find(name="span", id="productTitle").getText()
only_title = title.strip()
print(only_title)
price = soup.find(name="span", class_="a-offscreen").getText()
only_price = float(price.strip("$"))
print(only_price)

buy_price = 600
if only_price < buy_price:
    message = f"{only_title} is now ${only_price}"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="automation.python@yahoo.com",
                            msg=f"Subject: Amazon Price Alert!\n\n{message}\n{amazon_url}")

