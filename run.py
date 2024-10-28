import time
from time import gmtime, strftime
from digiKala import get_price_digikala
from excel import save_to_excel
from torob import get_price_torob


def fetch_prices():
    keyword = "samsung"

    # Get prices from Digikala and Torob
    price_digi = get_price_digikala(keyword)
    price_torob = get_price_torob(keyword)

    # Create a list of dictionaries to store the data
    data = [
        {"Time": strftime("%a, %d %b %Y %H:%M:%S", gmtime()), "Keyword": keyword, "Digikala Price": price_digi, "Torob Price": price_torob}
    ]

    # Save the data to an Excel file
    save_to_excel(data)


def update_prices():
    """
    Update prices every 5 minutes
    """
    while True:
        fetch_prices()

        # Wait for 5 minutes
        time.sleep(300)


if __name__ == "__main__":
    fetch_prices()
