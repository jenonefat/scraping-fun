from bs4 import BeautifulSoup


def file_scraper():
    '''
    Scrapes and parses text from HTML file.

    Returns: Print statements that include the title and cost for
    each course.
    '''

    with open('home.html', 'r') as html_file:
        content = html_file.read()

    soup = BeautifulSoup(content, 'html.parser')

    # grabbing prices for each course
    course_cards = soup.find_all("div", class_='card')
    for course in course_cards:
        course_name = course.h5.text
        price = course.a.text.split()[-1]

        print(f"{course_name} costs {price}")