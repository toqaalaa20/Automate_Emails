# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 00:49:51 2022

@author: Toqa Alaa
"""
import os
from email.message import EmailMessage
import ssl
import smtplib

def send_email(email_sender, email_password, email_reciever):
    email_sender= email_sender
    email_password= email_password
    email_reciever= email_reciever
    
    subject= 'SPAM EMAIL'
    body= """
    This is an automated message from Toqa Alaa
    """
    
    em= EmailMessage()
    em['From']= email_sender
    em['To']= email_reciever
    em['Subject']= subject
    em.set_content(body)
    
    context= ssl.create_default_context()
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context= context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_reciever, em.as_string())

send_email('abcd', 'abcd', 'abcd')