thonimport json
import os
from extractors.amazon_parser import parse_amazon_page
from outputs.exporters import export_to_json, export_to_csv

def main():
    # Input file containing URLs to scrape
    input_file = 'data/inputs.sample.txt'
    output_format = 'json'  # Can be 'json', 'csv', 'xml', 'excel'

    # Read input URLs
    with open(input_file, 'r') as f:
        urls = f.readlines()

    # Data extraction
    all_products = []
    for url in urls:
        url = url.strip()
        product_data = parse_amazon_page(url)
        all_products.extend(product_data)

    # Exporting results
    if output_format == 'json':
        export_to_json(all_products, 'data/scraped_data.json')
    elif output_format == 'csv':
        export_to_csv(all_products, 'data/scraped_data.csv')

if __name__ == '__main__':
    main()