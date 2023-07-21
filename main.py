from urllib.error import HTTPError
import requests
from bs4 import BeautifulSoup
import pandas as pd


def handle_error(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
    except HTTPError as http_err:
        print('HTTP error occurred:  {}'.format(http_err))
    except ConnectionError as conn_err:
        print('Connection error occurred:  {}'.format(conn_err))
    except TimeoutError as timeout_err:
        print('Timeout error occurred:  {}'.format(timeout_err))
    except requests.exceptions as req_err:
        print('Request error occurred:  {}'.format(req_err))


def create_table(bs):
    author_book = bs.find_all(class_='bookCard_bookAuthor__bvfqi')
    title_book = bs.find_all(class_='bookCard_bookTitle__3CvxH')
    price_book = bs.find_all(class_='bookCard_toman__2WUMO')
    author_book_series = pd.Series(author_book)
    title_book_series = pd.Series(title_book)
    table = pd.DataFrame({'نام کتاب': title_book_series, 'نویسنده': author_book_series, 'قیمت': price_book})
    table.head().to_csv('taaghche.csv')
    with open(f'../taaghche.txt', 'w', encoding='utf-8') as file:
        for row in table.iterrows():
            file.write(str(row) + '\n')


def scrape(url):
    handle_error(url)
    html = requests.get(url)
    bs = BeautifulSoup(html.content, 'html.parser')
    create_table(bs)


if __name__ == "__main__":
    url = "https://taaghche.com/filter?filter-collection=3130&filter-hasPhysicalBook=0&filter-target=4&order=1"
    scrape(url)
