# scrappy-scraping 

## Overview: 
I wanted to familiarize myself with web scraping and parsing HTML code using Beautiful Soup! When you look through the various python files in this repository, 
you'll probably notice the similarities in my code... yes, this was by design, as I wanted to practice basic scraping and HTML parsing using various 
free resources! 
However, you will also see that I explored different HTML sources to scrape as well as different ways to display parsed data. 
I will elaborate on these differences in my explanations of each program below. 
I studied the following page to guide me through these scrapes: https://realpython.com/beautiful-soup-web-scraper-python/#keep-practicing


### Fake Job Site Scrape
Scraped site: https://realpython.github.io/fake-jobs/
I wanted to explore the structure and features of HTML code on a website, and my code in **'fake_job_scrape.py'** reflects that. 
After sending an HTTP GET request and creating a Beautiful Soup object, I started by grabbing the *broadest* HTML element containing 
all the job listings (id=ResultsContainer). 
I then narrowed down my search to find *just* the job elements so that I could iterate through them to grab the job features I cared about:
the title of the job, the company name, and the job location. 

