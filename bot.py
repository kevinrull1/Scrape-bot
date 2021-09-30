import requests
from bs4 import BeautifulSoup

URL = "https://www.klick.ee/graafikakaart-gigabyte-geforce-rtx-3090-vision-oc-24gb"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

price = soup.find("div", class_="formatted-price relative")

for pprice in price.contents[0]:

  #  if "3149" in pprice:
    #   price = pprice

    print(pprice)
