import smtplib
from email.message import EmailMessage
from config import EMAIL_SETTINGS

def send_email(jobs):
    if not jobs:
        return

    msg = EmailMessage()
    msg["Subject"] = "New Stockholm Cyber Security / CISO Jobs"
    msg["From"] = EMAIL_SETTINGS["username"]
    msg["To"] = EMAIL_SETTINGS["to_email"]

    body = ""
    for j in jobs:
        body += f"""
{j['title']}
{j['company']} – {j['location']}
Score: {j['score']}
{j['url']}
-----------------------
"""

    msg.set_content(body)

    with smtplib.SMTP(
        EMAIL_SETTINGS["smtp_server"],
        EMAIL_SETTINGS["smtp_port"]
    ) as s:
        s.starttls()
        s.login(
            EMAIL_SETTINGS["username"],
            EMAIL_SETTINGS["password"]
        )
        s.send_message(msg)
