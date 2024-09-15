import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#server.py
print("welcome to server")
thesender = input("sender email:")
thepassword = input("gmail password (Use an App Password if 2FA is enable):")
recipent = input("email you want to serve to:")
thesubject = input("Subject:")
eBODY = input("emails text (aka the body):")

smtp_server = 'smtp.gmail.com'
smtp_port = 587
sender = thesender  # Replace with your Gmail address
password = thepassword   # Use an App Password if 2FA is enabled
recipients = recipent

# Create the message
msg = MIMEMultipart()
msg['Subject'] = thesubject
msg['From'] = sender
msg['To'] = recipients

# Email body
body = eBODY
msg.attach(MIMEText(body, 'plain'))

# Send the email
try:
    with smtplib.SMTP(smtp_server, smtp_port) as s:
        s.set_debuglevel(1)    # Enable debug output
        s.starttls()           # Upgrade the connection to secure TLS
        s.login(sender, password)  # Login with your Gmail account credentials
        s.sendmail(sender, recipients.split(','), msg.as_string())
    print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")
