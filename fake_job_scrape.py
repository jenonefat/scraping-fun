import requests
from bs4 import BeautifulSoup


# sending HTTP GET request to site URL
base_url = "https://realpython.github.io/fake-jobs/"
page = requests.get(base_url)

# view all the HTML text scraped from the site
print(page.text)

# creating Beautiful Soup object
# page.content arg: scraped HTML content
# html.parser arg: appropriate parser for html
soup = BeautifulSoup(page.content, "html.parser")

# finding HTML element containing all job listings
results = soup.find(id="ResultsContainer")
print(results.prettify())

# printing HTML code for just the job listings
job_elements = results.find_all("div", class_="card-content")
# specifying which job features I want to see
for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_name = job_element.find("h3", class_="subtitle")
    location_element = job_element.find("p", class_="location")
    print(title_element.text.strip())
    print(company_name.text.strip())
    print(location_element.text.strip())
    print()

# filtering for specific job type(ex: jobs that require Python)
python_jobs = results.find_all(
    "h2", string=lambda text:"python" in text.lower()
)
# backtracking in DOM hierarchy to grab all listing info ONLY for job type I want
python_job_elements = [h2_element.parent.parent.parent for h2_element in python_jobs]

for job_element in python_job_elements:
    title_element = job_element.find("h2", class_="title")
    company_name = job_element.find("h3", class_="subtitle")
    location_element = job_element.find("p", class_="location")
    print(title_element.text.strip())
    print(company_name.text.strip())
    print(location_element.text.strip())
    # getting link to application for each Python job by accessing href attribute
    apply_links = job_element.find_all("a", string=lambda text: "apply" in text.lower())
    for link in apply_links:
        link_url = link["href"]
        print(f'Apply here: {link_url}')
    print()




