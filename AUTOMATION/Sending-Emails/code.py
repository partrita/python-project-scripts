import logging
import os
import smtplib
from email.message import EmailMessage

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Use environment variables for credentials
EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')  
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')  

def send_email(subject, recipient, body, html_content=None, attachment_path=None):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = recipient

    msg.set_content(body)

    if html_content:
        msg.add_alternative(html_content, subtype='html')

    if attachment_path:
        try:
            with open(attachment_path, 'rb') as f:
                file_data = f.read()
                file_name = f.name
                msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
        except FileNotFoundError:
            logger.error(f"Attachment file {attachment_path} not found.")
            return

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
            logger.info("Email Sent Successfully")
    except (smtplib.SMTPException, OSError) as e:
        logger.error(f"An error occurred: {e}")

# Usage Example
send_email('Test Subject', 'recipient@example.com', 'This is the email body',
           '<html><body><h1>HTML Content</h1></body></html>', 'testing.txt')
