import smtplib
import os
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

def send_email(to_email: str):
    msg = EmailMessage()
    msg.set_content(
    f"""
Hi,

🎉 Congratulations Bajjuri! 🎉

We are happy to inform you that you have been selected for the job.
Your hard work and dedication have paid off.

Wishing you great success in your new role.

Best Regards,
HR Team
"""
)

    msg["Subject"] = "🎉 Congratulations! You Got the Job"
    msg["From"] = EMAIL_USER
    msg["To"] = to_email

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(EMAIL_USER, EMAIL_PASSWORD)
    server.send_message(msg)
    server.quit()
