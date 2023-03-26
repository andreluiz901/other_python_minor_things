from email.message import EmailMessage
from appword import password
import ssl
import smtplib

email_sender = 'your_email@gmail.com'
email_password = password  #importing the password from other doc for safety

email_receiver = 'destiny_email@gmail.com'

subejct = "subject text"

body = """

body text

"""

em = EmailMessage()
em['From'] = email_sender
em['TO'] = email_receiver
em['subject'] = subejct
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
