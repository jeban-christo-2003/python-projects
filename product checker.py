import asyncio
import aiohttp
import time
import schedule
import smtplib 

# Receiver email ID
receiver_email_id = "EMAIL_ID_OF_USER"
gmail_username = "YOUR_GMAIL_ID"
gmail_password = "YOUR_GMAIL_PASSWORD"

async def check(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            html_content = await response.text()
            if "In stock" in html_content:
                return True
    return False

async def send_email(product):
    message = f"{product} is available now!"
    subject = f"{product} availability"
    body_of_email = f"Subject: {subject}\n\n{message}"
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(gmail_username, gmail_password)
            server.sendmail(gmail_username, receiver_email_id, body_of_email)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

async def track_product(product_url, product_name):
    if await check(product_url):
        await send_email(product_name)

async def main():
    product_url = "https://www.amazon.in/dp/B077PWK5BT"
    product_name = "Product Name"
    await track_product(product_url, product_name)

def job():
    print("Tracking....")
    asyncio.run(main())

schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
