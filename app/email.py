from flask_mail import Message
from flask import render_template
from . import mail

def mail_message(subject,template,to,**mwenda):
  '''
  function that facilitates sending email to new users
  '''
  sender_email='brianmwenda255@gmail.com'
  email=Message(subject, sender=sender_email,recipients=[to])
  email.body=render_template(template+".txt",**mwenda)
  email.html=render_template(template+".html",**mwenda)
  mail.send(email)
