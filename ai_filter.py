from openai import OpenAI
from config import OPENAI_MODEL

client = OpenAI()

def classify_job(job):
    prompt = f"""
You are a senior cyber security recruiter.

Is this job relevant for a senior cyber security,
security architect, or CISO-level role?

Title: {job['title']}
Location: {job['location']}
Company: {job['company']}

Answer ONLY:
RELEVANT or NOT_RELEVANT
"""

    r = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    return "RELEVANT" in r.choices[0].message.content


def score_job(job):
    prompt = f"""
Score this job from 1–10 for relevance to a senior
cyber security or CISO candidate.

Title: {job['title']}
Company: {job['company']}

Return ONLY a number.
"""

    r = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    return int(r.choices[0].message.content.strip())
