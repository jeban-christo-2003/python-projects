import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import schedule
import time

def send_email(subject, message, to_email, attachment=None):
    # Email configuration
    from_email = "your_email@gmail.com"
    password = "your_password"

    # Create message container
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach message body
    msg.attach(MIMEText(message, 'plain'))

    if attachment:
        # Attach file
        attachment_file = open(attachment, 'rb')
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment_file).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= " + attachment)
        msg.attach(part)

    # Connect to SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, password)

    # Send email
    server.sendmail(from_email, to_email, msg.as_string())
    server.quit()

def job():
    # Send email on specific date or event
    subject = "Automated Email"
    message = "This is an automated email sent using Python."
    to_email = "recipient_email@example.com"
    attachment = "attachment.pdf"  # Optional attachment

    send_email(subject, message, to_email, attachment)

# Schedule email to be sent every day at 8:00 AM
schedule.every().day.at("08:00").do(job)

# Main loop to keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)
