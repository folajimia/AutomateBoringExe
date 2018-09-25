import smtplib


host="smtp.gmail.com"
port=587
username="foladapoa@gmail.com"
password="Fola1520!"
from_email = username
to_list = ["folajimia@gmail.com"]


email_conn = smtplib.SMTP(host, port)
email_conn.ehlo()
email_conn.starttls()
email_conn.login(username, password)
email_conn.sendmail(from_email, to_list, "Hi, hello there this is fun")
email_conn.quit


from smtplib import SMTP

email_conn2 = SMTP(host, port)
email_conn2.ehlo()
email_conn2.starttls()
email_conn2.login(username, password)
email_conn2.sendmail(from_email, to_list, "Hi, hello there this is fun")
email_conn2.quit

from smtplib import SMTP, SMTPAuthenticationError, SMTPException

password = SMTP(host, port)
password.ehlo()
password.starttls()
try:
    password.login(username, "xcx")
    password.sendmail(from_email, to_list, "Hi, hello there this is fun")
except SMTPAuthenticationError:
    print("could not log in")
except SMTPAuthenticationError:
    print("an error occured")
password.quit

