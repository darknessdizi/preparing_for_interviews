import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pprint


GMAIL_SMTP = "smtp.gmail.com"
GMAIL_IMAP = "imap.gmail.com"

l = 'darknessdizi@gmail.com'
passwORD = 'hbqjqlqrywruowcp'
subject = 'Subject'
recipients = ['rash-jane@mail.ru']
message = 'Message'
header = None


#send message
msg = MIMEMultipart()
msg['From'] = l
msg['To'] = ', '.join(recipients)
msg['Subject'] = subject
msg.attach(MIMEText(message))

ms = smtplib.SMTP(GMAIL_SMTP, 587)
# identify ourselves to smtp gmail client
ms.ehlo()
# secure our email with tls encryption
ms.starttls()
# re-identify ourselves as an encrypted connection
ms.ehlo()

ms.login(l, passwORD)
ms.sendmail(l, recipients[0], msg.as_string())

ms.quit()
#send end


#recieve
mail = imaplib.IMAP4_SSL(GMAIL_IMAP)
mail.login(l, passwORD)
mail.list()
mail.select("inbox")
criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
result, data = mail.uid('search', None, criterion)
assert data[0], 'There are no letters with current header'
latest_email_uid = data[0].split()[-1]
result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
pprint.pprint(result)
raw_email = str(data[0][1])
email_message = email.message_from_string(raw_email)
mail.logout()
#end recieve