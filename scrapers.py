import requests
from bs4 import BeautifulSoup

def fetch_product_details(url):
    try:
        resp = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(resp.text, "html.parser")

        title = soup.select_one("title").get_text().strip() if soup.select_one("title") else "No Title"
        img = soup.select_one("img")["src"] if soup.select_one("img") else ""
        price_tag = soup.find(["span", "div"], class_="price")
        price = price_tag.get_text().strip() if price_tag else "0"

        return {"title": title, "image": img, "price": price}
    except Exception as e:
        return {"error": str(e)}
