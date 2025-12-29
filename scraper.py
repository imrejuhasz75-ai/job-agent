import requests
from bs4 import BeautifulSoup

HEADERS = {"User-Agent": "Mozilla/5.0"}

def scrape_indeed():
    url = (
        "https://se.indeed.com/jobs"
        "?q=cyber+security+ciso"
        "&l=Stockholm"
    )

    r = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(r.text, "html.parser")

    jobs = []

    for card in soup.select(".job_seen_beacon"):
        title = card.select_one("h2").get_text(strip=True)
        company = card.select_one(".companyName").get_text(strip=True)
        location = card.select_one(".companyLocation").get_text(strip=True)
        link = "https://se.indeed.com" + card.select_one("a")["href"]

        jobs.append({
            "title": title,
            "company": company,
            "location": location,
            "description": "",
            "url": link,
            "source": "Indeed"
        })

    return jobs
