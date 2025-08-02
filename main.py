from fastapi import FastAPI, Request
from scrapers import fetch_product_details

app = FastAPI()

@app.get("/")
def home():
    return {"status": "Bot Backend Running"}

@app.post("/import")
def import_product(data: dict):
    url = data.get("url")
    details = fetch_product_details(url)
    return {"status": "success", "product": details}
