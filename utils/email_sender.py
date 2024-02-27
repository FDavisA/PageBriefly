import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(subject, body, recipient_email, sender_email, sender_password):
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(sender_email, sender_password)

    email = MIMEMultipart('alternative')
    email['From'] = sender_email
    email['To'] = recipient_email
    email['Subject'] = subject
    email.attach(MIMEText(body, 'html')) 

    server.send_message(email)
    server.quit()

    print("Email sent successfully!")
