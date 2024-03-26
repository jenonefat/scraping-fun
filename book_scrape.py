from bs4 import BeautifulSoup
import requests
import time


def find_books():
    '''
    Scrapes and parses HTML code from 'Books to Scrape' site,
    automated to run every 10 min.

    Returns: new directory containing separate '.txt' files for each book
    Each '.txt' file contains the following parsed data: title, price, rating, and a link
    to the book description
    '''
    # scraping HTML text
    url = "https://books.toscrape.com/"
    html_text = requests.get(url).content

    # creating BeautifulSoup object
    soup = BeautifulSoup(html_text, 'html.parser')
    # grabbing HTML text for each book
    books = soup.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")

    # iterate through each book element to parse data
    for index, book in enumerate(books):
        title = book.h3.a['title']
        price = book.find("p", class_="price_color").text
        rating = book.find_all("p")[0]["class"][-1]
        description = book.h3.a['href']

        # create new file in 'book_info' dir, labeled by index num
        with open(f'book_info/{index}.txt','w') as f:
            f.write(f"{title} costs {price}\n")
            f.write(f"Rating: {rating} stars\n")
            f.write(f"Book Description: {description}\n")
        # print confirmation message for each book file
        print(f"File saved: {index}")


if __name__ == "__main__":
    while True:
        find_books()
        time_wait = 10
        print(f"Waiting {time_wait} minutes . . . ")
        time.sleep(time_wait * 60)