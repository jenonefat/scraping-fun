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
I further specified my results by filtering down to only those jobs that required the use of Python; I did this by grabbing only the job elements
that had "python" in the title. However, I also needed to grab other desired features of the Python jobs, so I had to backtrack in the DOM hierarchy
to access the element that contained all the other job information for *just* the Python listings : (h2_element.parent.parent.parent).
After grabbing the title, company, and location info for each Python job, I decided I also wanted to include the application link; I accomplished this
by iterating through each HTML line containing a link tag ("a"), and accessing the 'href' attribute only from those lines that had "apply" 
in the line text. 


### File Scrape 
Scraped file: home.html 
File source: jimdevops19/codesnippets  ~ this file contains information about fake courses
To practice scraping an html file (rather than a website), I referenced part of this tutorial: https://www.youtube.com/watch?v=XVv6mJpFOb0
Rather than sending an HTTP get request, I merely opened the html file and assigned the html text to the "content" variable.
I created a Beautiful Soup object, and then found the iterable element that contains info about each course.
I iterated through each of these course cards/elements to grab the course name and price. 
