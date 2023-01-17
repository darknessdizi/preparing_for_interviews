import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pprint
from password import password


class Mail:
    
    GMAIL_SMTP = "smtp.gmail.com"
    GMAIL_IMAP = "imap.gmail.com"

    def __init__(self, login, password):
        self.login = login
        self.password = password
        # self.subject = 'Subject'
        self.recipients = ['rash-jane@mail.ru']
        self.header = None

    def send_message(self, subject, message):

        '''Отправка сообщений'''

        msg = MIMEMultipart()
        msg['From'] = self.login
        msg['To'] = ', '.join(self.recipients)
        msg['Subject'] = subject
        msg.attach(MIMEText(message))

        ms = smtplib.SMTP(Mail.GMAIL_SMTP, 587)
        # identify ourselves to smtp gmail client
        ms.ehlo()
        # secure our email with tls encryption
        ms.starttls()
        # re-identify ourselves as an encrypted connection
        ms.ehlo()

        ms.login(self.login, self.password)
        ms.sendmail(self.login, self.recipients, msg.as_string())

        ms.quit()


# #recieve
# mail = imaplib.IMAP4_SSL(GMAIL_IMAP)
# mail.login(l, passwORD)
# mail.list()
# mail.select("inbox")
# criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
# result, data = mail.uid('search', None, criterion)
# assert data[0], 'There are no letters with current header'
# latest_email_uid = data[0].split()[-1]
# result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
# pprint.pprint(result)
# raw_email = str(data[0][1])
# email_message = email.message_from_string(raw_email)
# mail.logout()
# #end recieve

if __name__ == '__main__':
    login = 'darknessdizi@gmail.com'
    # password = 'hbqjqlqrywruowcp'
    object = Mail(login, password)
    object.send_message(
        'Оповещение с ноутбука', 
        "Привет от Димы и Тани"
    )