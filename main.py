# import os
# import random

import smtplib
import getpass

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def automatic_email_gmail():
    user = input("Enter Your Name >>: ")
    email_From = input("Enter Your Email >>: ")
    email_TO = input("Enter whom to send >>: ")
    password = getpass.getpass(prompt='Enter Your Password: ', stream=None)
    message = (f"Dear {user}, Welcome!")
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.starttls()
    smtpObj.login(email_From, password)
    smtpObj.sendmail(email_From, email_TO, message)
    print("Email Sent!")
    smtpObj.quit()

def automatic_email_yandex():
    addr_from = "foo@yandex.ru"
    addr_to = "bar@yandex.ru"
    password = "pass"  # пароль от почты addr_from

    msg = MIMEMultipart()  # Создаем сообщение
    msg['From'] = addr_from  # Адресат
    msg['To'] = addr_to  # Получатель
    msg['Subject'] = 'Тема сообщения'  # Тема сообщения

    body = "Текст сообщения"
    msg.attach(MIMEText(body, 'plain'))  # Добавляем в сообщение текст

    server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)  # Создаем объект SMTP
    server.starttls()             # Начинаем шифрованный обмен по TLS
    server.login(addr_from, password)  # Получаем доступ
    server.send_message(msg)  # Отправляем сообщение
    server.quit()  # Выходим

automatic_email_gmail()
#_automatic_email_yandex()