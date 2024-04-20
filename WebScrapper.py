import requests
import re
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from StockReader import StockReader

class WebScrapper():

    def __init__(self, url):
        self.url = url
        self.stock_reader = StockReader()

    def validate_url(self):
        parsed_url = urlparse(self.url)
        if parsed_url.netloc == 'finance.yahoo.com':
            return True
        if 'finance.yahoo.com' in parsed_url.netloc:
            return True
        if re.search(r'finance\.yahoo\.com', parsed_url.path):
            return True
        return False

    def extract_stock_ticker(self, text):
        pattern = r'\([\w]+:\s*([A-Z]+)\)'
        match = re.search(pattern, text)
        if match:
            return match.group(1)
        else:
            return None

    def ticker_scrapper(self):
        if self.validate_url():
            page = requests.get(self.url)
            soup = BeautifulSoup(page.content, "html.parser")
            result = str(soup.find("span", class_="ticker"))
            treated_result = self.extract_stock_ticker(result)
            if self.stock_reader.stock_exists(treated_result):
                print(treated_result)
        else:
            print("Invalid URL")

    def text_scrapper(self):
        if self.validate_url():
            page = requests.get(self.url)
            soup = BeautifulSoup(page.content, "html.parser")
            paragraphs = soup.find_all("p")
            different_p = [p.get_text() for p in paragraphs]
            full_text = ""
            for p in different_p:
                full_text += p
            print(full_text)
        else:
            print("Invalid URL")

scrappinho = WebScrapper("https://finance.yahoo.com/news/buy-taiwan-semiconductor-stock-now-203609829.html")
print(scrappinho.ticker_scrapper())
print(scrappinho.text_scrapper())