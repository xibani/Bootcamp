# Arrocera Yum Asia Sakura

import requests
from bs4 import BeautifulSoup
import smtplib

URL_RC = "https://www.amazon.es/dp/B075WWQY2Y?tag=dap-pivot-21&th=1"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
    "Accept-Language": "es-ES,es;q=0.9,en-GB;q=0.8,en;q=0.7"
}

response = requests.get(URL_RC, headers=header)
soup = BeautifulSoup(response.text, "html.parser")

prices = soup.find(name="span", class_="a-offscreen")
# Coger el testo, eliminar el euro, cambiar , por . y transformarlo a float
price = float(prices.getText().split("€")[0].replace(",","."))



# que avise cuando el precio sea menor de 115
title = soup.find(name="h1", class_="a-size-large a-spacing-none")
mensaje = title.getText(strip=True) + " is now " + str(price) + "€" + "\n" + URL_RC

BUY_PRICE = 200

YOUR_EMAIL = "anderg8t@gmail.com"
YOUR_PASSWORD = "ukepnhlkoiurgvax"

if price < BUY_PRICE:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        msg = f"Subject:Amazon Price Alert!\n\n{mensaje}"
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs="anderg8a@gmail.com",
            msg=msg.encode('utf-8')
        )