#!/usr/bin/python3
#
# Coat of arms is an email-based, CLI strategy game of conquest.
# This module is in charge of sending and receiving emails for
# inter-player communication.
#
# Copyright (c) 2015 Daniel Vedder, Christopher Borchert
# Licensed under the terms of the MIT license.
#

from smtplib import SMTP_SSL
from imaplib import IMAP4

global smtp_server
global imap_server
global email_address
global password

def send_mail(message):
    global smtp_server, email_address, password
    smtp = SMTP_SSL(smtp_server)
    smtp.login(email_address, password)
    smtp.sendmail(email_address, email_address, message)
    smtp.quit()

def fetch_mail():
    pass


if __name__ == '__main__':
    smtp_server = 'smtp.gmail.com'
    imap_server = ('imap.gmail.com', 993)
    email_address = 'coat.of.arms.server@gmail.com'
    password = input("Please enter the password: ")
    message = input("Please enter a message: ")
    print("Message is being sent.")
    send_mail(message)
    print("Done.")
