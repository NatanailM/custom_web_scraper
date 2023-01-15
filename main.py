from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://www.newegg.ca/p/pl?d=3080"

response = requests.get(url)

doc = BeautifulSoup(response.text, "html.parser")

names = doc.find_all(class_="item-title")
prices = doc.find_all(text="$")

names_list = []
prices_list = []

for i in range(len(prices)):
    parent_price = prices[i].parent
    price_strong = parent_price.find("strong")
    names_list.append(names[i+2].string)
    prices_list.append(f"${price_strong.string}")

gpus = {
    "Name": names_list,
    "Price": prices_list
}

df = pd.DataFrame(gpus)

df.to_csv("gpu_prices.csv")
