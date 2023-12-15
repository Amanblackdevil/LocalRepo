import getpass
import smtplib

HOST = "smtp-mail.outlook.com"
PORT = 587

FROM_EMAIL = "Raviaman.yadav@outlook.com"
TO_EMAIL = "kakkrotsongoku@gmail.com"
PASSWORD = getpass.getpass("Enter Password :")

MESSAGE = """Subject : Hello guys
Hi, Guys

message sent using python
thanks,
Test account"""

smtp = smtplib.SMTP(HOST, PORT)

status_code, response = smtp.ehlo()
print(f"[*] Echoing server : {status_code} {response}")

status_code, response = smtp.starttls()
print(f"[*] Stating TLC connection : {status_code} {response}")

status_code, response = smtp.login(FROM_EMAIL, PASSWORD)
print(f"[*] Login in : {status_code} {response}")

smtp.sendmail(FROM_EMAIL, TO_EMAIL, MESSAGE)
smtp.quit()