import smtplib
import getpass

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

HOST = "smtp-mail.outlook.com"
PORT = 587

FROM_EMAIL = "Raviaman.yadav@outlook.com"
TO_EMAIL = "kakkrotsongoku@gmail.com"
PASSWORD = getpass.getpass("Enter Your passoword :")

message = MIMEMultipart("alternative")
message['Subject'] = "Mail sent using python"
message['From'] = FROM_EMAIL
message['To'] = TO_EMAIL
message['Cc'] = FROM_EMAIL
message['Bcc'] = FROM_EMAIL

html = ""
with open("html_main.html", "r") as file:
    html = file.read()

html_part = MIMEText(html, 'html')
message.attach(html_part)

smtp = smtplib.SMTP(HOST, PORT)

status_code, response = smtp.ehlo()
print(f"[*] Echoing the server : {status_code} {response}")

status_code, response = smtp.starttls()
print(f"[*] String TLS connection : {status_code} {response}")

status_code, response = smtp.login(FROM_EMAIL, PASSWORD)
print(f"[*] Loging in : {status_code} {response}")

smtp.sendmail(FROM_EMAIL, TO_EMAIL, message.as_string())
smtp.quit()