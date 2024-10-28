from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time


# Function to get the price of a product from Digikala using Selenium
def get_price_digikala(keyword: str):
    # Set up the ChromeDriver service for Selenium
    # Configure Selenium Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode for better performance
    service = Service(
        'C:/Users/fam-01/.wdm/drivers/chromedriver/win64/130.0.6723.69/chromedriver-win64/chromedriver.exe')  # Path to your ChromeDriver executable
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Open the Digikala search page with the specified keyword
    url = f"https://www.digikala.com/search/?q={keyword}"
    driver.get(url)

    # Wait for the page to fully load (may need adjustment)
    time.sleep(5)

    # Get the page source and parse it with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Find the first product in the product list and try to extract the price
    first_product = soup.find('div', class_='product-list_ProductList__item__LiiNI')
    if first_product:
        price = first_product.find('div',
                                   class_='flex items-center justify-end gap-1 text-neutral-700 text-neutral-400 text-h5 grow')
        if price:
            return price.text.strip()

    # Quit the driver after finishing
    driver.quit()
    return "Not Found"


# Main entry point for the script
if __name__ == '__main__':
    # Test the function by searching for a product with the keyword "samsung"
    print(get_price_digikala("samsung"))
