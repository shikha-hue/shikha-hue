import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

def get_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    products = []

    # Find all product containers
    product_containers = soup.find_all('div', class_='thumbnail')

    for container in product_containers:
        title_tag = container.find('a', class_='title')
        price_tag = container.find('h4', class_='price')  # Ensure this matches the HTML structure

        title = title_tag.text.strip() if title_tag else 'No Title'
        price = price_tag.text.strip() if price_tag else 'No Price'

        products.append({'title': title, 'price': price})

    return products

def get_next_page(soup):
    next_button = soup.find('li', class_='next')
    if next_button:
        next_page_url = next_button.find('a')['href']
        return 'https://webscraper.io' + next_page_url
    return None

def save_to_csv(data, filename='products.csv'):
    keys = data[0].keys()
    with open(filename, 'w', newline='', encoding='utf-8') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)

def scrape_website(start_url):
    all_products = []
    url = start_url

    while url:
        html = get_html(url)
        if html:
            products = parse_html(html)
            all_products.extend(products)

            soup = BeautifulSoup(html, 'html.parser')
            next_page_url = get_next_page(soup)
            if next_page_url:
                url = next_page_url
            else:
                url = None
        else:
            break

    return all_products

def display_csv(filename='products.csv'):
    df = pd.read_csv(filename)
    print(df)

if __name__ == "__main__":
    start_url = 'https://webscraper.io/test-sites/e-commerce/static/computers/laptops'
    products = scrape_website(start_url)
    if products:
        save_to_csv(products)
        print(f'Scraped {len(products)} products.')
    else:
        print('No products found.')

    display_csv()
