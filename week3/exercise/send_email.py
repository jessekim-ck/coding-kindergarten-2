import smtplib
from email.mime.text import MIMEText

SENDER = "jessekim.ck.94@gmail.com"
APP_PASSWORD = "lkuqoeouiluausir"
RECEIVER = "jahyun826@gmail.com"


s = smtplib.SMTP("smtp.gmail.com", 587)
s.starttls()
s.login(SENDER, APP_PASSWORD)

msg = MIMEText("찡찡거려~~~")
msg["Subject"] = "아유~~"

s.sendmail(SENDER, RECEIVER, msg.as_string())
s.quit()