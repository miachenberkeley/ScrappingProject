import requests
from bs4 import BeautifulSoup
import time

# post url
js = "https://angel.co/company_filters/search_data"

# X-Requested-With is important
headers = {"X-Requested-With": "XMLHttpRequest",
           "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36"}


# get url
u = "https://angel.co/companies/startups?ids%5B%5D={}&total={}&page={}&sort=signal&new=false&hexdigest={}"


def get_next_pages(js, u, start_page=1):
    with requests.Session() as s:
        params = s.post(js, data={"sort": "signal","page":start_page}, headers=headers).json()
        companies = s.get(
            u.format("&ids%5B%5D=".join(map(str, params["ids"])), params["page"], params["total"], params["hexdigest"]),
            headers=headers)
        soup = BeautifulSoup(companies.json()["html"])
        comps = soup.select("div.company.column")
        yield comps
        while True:
            # increment page count from previous.
            page = params["page"] + 1
            params = s.post(js, data={"sort": "signal", "page": page}, headers=headers).json()
            # keep going until we have reached the maximum queries
            if "ids" not in params:
                break
            companies = s.get(u.format("&ids%5B%5D=".join(map(str, params["ids"])), params["page"], params["total"],
                                       params["hexdigest"]),
                              headers=headers)
            soup = BeautifulSoup(companies.json()["html"])
            comps = soup.select("div.company.column")
            # don't hammer with requests
            time.sleep(.3)
            yield comps

for comps in get_next_pages(js, u):
    print(comps)