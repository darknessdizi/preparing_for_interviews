import email
import smtplib
import imaplib
import pprint
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from password import password


class Mail:
    
    GMAIL_SMTP = "smtp.gmail.com"
    GMAIL_IMAP = "imap.gmail.com"

    def __init__(self, login, password, recipients):
        self.login = login
        self.password = password
        self.recipients = recipients

    def send_message(self, subject, message):

        '''Отправка писем'''

        msg = MIMEMultipart()
        msg['From'] = self.login
        msg['To'] = ', '.join(self.recipients)
        msg['Subject'] = subject
        msg.attach(MIMEText(message))

        ms = smtplib.SMTP(Mail.GMAIL_SMTP, 587)
        ms.ehlo()
        ms.starttls()
        ms.ehlo()

        ms.login(self.login, self.password)
        ms.sendmail(self.login, self.recipients, msg.as_string())

        ms.quit()

    def get_emails(self, header=None):

        '''Получение писем'''
        
        mail = imaplib.IMAP4_SSL(Mail.GMAIL_IMAP)
        mail.login(self.login, self.password)
        mail.list()
        mail.select("inbox")

        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
        result, data = mail.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'

        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')

        raw_email = str(data[0][1])
        email_message = email.message_from_string(raw_email)
        mail.logout()
        return email_message


if __name__ == '__main__':

    login = 'darknessdizi@gmail.com'
    recipients = ['rash-jane@mail.ru']

    object = Mail(login, password, recipients)
    object.send_message(
        'Оповещение с ноутбука', 
        "Привет от Димы и Тани"
    )
    pprint.pprint(str(object.get_emails('GitHub')))