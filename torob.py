import requests
from bs4 import BeautifulSoup


def get_price_torob(keyword: str):
    url = f"https://torob.com/search/?query={keyword}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    try:
        first_product = soup.find('div', class_='jsx-ca974f9fd4e0a204')
        if first_product:
            price = first_product.find('div', class_='desktopProductCard_product-price-text__folP0').text.strip()
            return price
    except Exception as e:
        print(f"Error: {e}")

    return "Not Found"


if __name__ == '__main__':
    print(get_price_torob("samsung"))
