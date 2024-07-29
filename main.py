import requests

from bs4 import BeautifulSoup

url = "https://www.amazon.eg/s?k=anker+wireless+charger&sprefix=%2Caps%2C116&ref=nb_sb_ss_recent_1_0_recent"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(url, headers=header)

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

articles = soup.find_all(class_="a-size-base-plus a-color-base a-text-normal")
price = soup.find_all(class_="a-price-whole")
img = soup.find_all(class_="s-image")
for i in range(len(articles[i].text))
    print (articles[i].text)
    print(price[i].text)
    print (img[i])

