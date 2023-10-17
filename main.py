import requests
from bs4 import BeautifulSoup

url = "http://example.com"  # replace with the URL you want to scrape
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
data = soup.find_all('div')  # replace 'div' with the HTML tag you want to scrape

for item in data:
    print(item.text)
