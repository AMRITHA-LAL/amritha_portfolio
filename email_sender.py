import smtplib
from email.message import EmailMessage

sender = "kavyakannan2020@gmail.com"

receiver = "kimjeonkavya@gmail.com"

app_password = "ngpo tusp icdg jqan"

msg = EmailMessage()

msg["Subject"] = "Portfolio Automation Test"

msg["From"] = sender

msg["To"] = receiver

msg.set_content(
"""
Hello Kavya,

This email was sent automatically using Python.

Project:
Smart Portfolio Automation

Features:
- GitHub Automation
- News Fetching
- Email Automation

Regards,
Python Bot
"""
)

with smtplib.SMTP_SSL(
    "smtp.gmail.com",
    465
) as smtp:

    smtp.login(
        sender,
        app_password
    )

    smtp.send_message(
        msg
    )

print(
    "Email sent successfully"
)