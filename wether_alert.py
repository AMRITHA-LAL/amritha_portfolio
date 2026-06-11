import requests
import smtplib

from email.message import EmailMessage


API_KEY = "ace415fc1ec28e56dfdde22c7526b684"

CITY = "Kollam"

url = (
    f"https://api.openweathermap.org/data/2.5/weather?"
    f"q={CITY}"
    f"&appid={API_KEY}"
    f"&units=metric"
)

response = requests.get(url)

data = response.json()

temperature = data["main"]["temp"]

condition = data["weather"][0]["main"]

if (
    temperature > 35
    or
    condition.lower() == "rain"
):

    sender = "kavyakannan2020@gmail.com"

    # Paste your Gmail App Password below
    password = "zaiy ryml zfqy ecqk"

    msg = EmailMessage()

    msg["Subject"] = "Weather Alert"

    msg["From"] = sender

    msg["To"] = sender

    msg.set_content(
f"""
Weather Alert

City: {CITY}

Temperature: {temperature}°C

Condition: {condition}
"""
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

    print("Weather Alert Sent")

else:

    print("No Weather Alert Needed")