import sqlite3

def init_db():
    conn = sqlite3.connect("jobs.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            url TEXT PRIMARY KEY,
            title TEXT,
            company TEXT,
            location TEXT,
            score INTEGER
        )
    """)
    conn.commit()
    conn.close()


def save_job(job):
    conn = sqlite3.connect("jobs.db")
    c = conn.cursor()
    c.execute("""
        INSERT OR IGNORE INTO jobs
        VALUES (?, ?, ?, ?, ?)
    """, (
        job["url"],
        job["title"],
        job["company"],
        job["location"],
        job["score"]
    ))
    conn.commit()
    conn.close()
