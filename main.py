from urllib.error import HTTPError
import requests
from bs4 import BeautifulSoup


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
    except requests.exceptions.RequestException as req_err:
        print(req_err)


def create_table(bs):
    author_book = bs.find_all("div", class_="bookCard_bookAuthor__bvfqi")
    authors = [author.text for author in author_book]
    title_book = bs.find_all(class_='bookCard_bookTitle__3CvxH')
    titles = [title.text for title in title_book]
    price_book = bs.find_all(class_='bookCard_toman__2WUMO')
    price = [p.text for p in price_book]

    print(f'authors: {authors}\n'
          f'titles: {titles}\n'
          f'price: {price}')


def scrape(url):
    handle_error(url)
    html = requests.get(url)
    bs = BeautifulSoup(html.content, 'html.parser')
    create_table(bs)


if __name__ == "__main__":
    url = "https://taaghche.com/filter?filter-collection=3130&filter-hasPhysicalBook=0&filter-target=4&order=1"
    scrape(url)
