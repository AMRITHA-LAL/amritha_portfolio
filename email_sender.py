import json
import smtplib

from email.message import EmailMessage

sender = "kavyakannan2020@gmail.com"

password = "zaiy ryml zfqy ecqk"

with open(
    "news.json",
    "r",
    encoding="utf-8"
) as file:

    news = json.load(file)

html = """
<h2>
Morning News Digest
</h2>
<ul>
"""

for item in news:

    html += f"<li>{item}</li>"

html += "</ul>"

msg = EmailMessage()

msg["Subject"] = (
    "Morning News Digest"
)

msg["From"] = sender

msg["To"] = sender

msg.add_alternative(
    html,
    subtype="html"
)

with smtplib.SMTP_SSL(
    "smtp.gmail.com",
    465
) as smtp:

    smtp.login(
        sender,
        password
    )

    smtp.send_message(msg)

print("News Email Sent")