from scraper import scrape_indeed
from ai_filter import classify_job, score_job
from storage import init_db, save_job
from notifier import send_email
from config import STOCKHOLM_KEYWORDS

def is_stockholm(job):
    return any(k.lower() in job["location"].lower()
               for k in STOCKHOLM_KEYWORDS)

def run():
    init_db()
    jobs = scrape_indeed()

    final_jobs = []

    for job in jobs:
        if not is_stockholm(job):
            continue

        if not classify_job(job):
            continue

        job["score"] = score_job(job)
        save_job(job)
        final_jobs.append(job)

    final_jobs.sort(key=lambda x: x["score"], reverse=True)
    send_email(final_jobs)

if __name__ == "__main__":
    run()
