thonimport requests
from bs4 import BeautifulSoup

def parse_amazon_page(url):
    """Parse an Amazon Best Seller page and return product details."""
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch the URL: {url}")

    soup = BeautifulSoup(response.text, 'html.parser')
    products = []

    # Extract product details (this is an example, adjust the selectors based on actual page structure)
    for product in soup.find_all('div', class_='zg_itemWrapper'):
        product_data = {
            'position': product.find('span', class_='zg_rankNumber').text.strip(),
            'category': product.find('a', class_='zg_title').text.strip(),
            'categoryUrl': product.find('a', class_='zg_title')['href'],
            'name': product.find('div', class_='p13n-sc-truncate').text.strip(),
            'price': product.find('span', class_='p13n-sc-price').text.strip(),
            'currency': '$',  # Example, may need to extract from the price
            'numberOfOffers': product.find('span', class_='a-size-small').text.strip(),
            'url': product.find('a', class_='a-link-normal')['href'],
            'thumbnail': product.find('img', class_='s-image')['src']
        }
        products.append(product_data)

    return products