from fastapi import FastAPI
from digiKala import get_price_digikala
from torob import get_price_torob
app = FastAPI()

@app.get("/prices/")
def get_prices(keyword: str):
    price_digi = get_price_digikala(keyword)
    price_torob = get_price_torob(keyword)
    return {"keyword": keyword, "digikala_price": price_digi, "torob_price": price_torob}
