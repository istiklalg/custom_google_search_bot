"""
encoding:utf-8
@author : istiklal
mailing service file
"""

import smtplib
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from passcodes import EMAIL_HOST, EMAIL_PORT, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD

# Function to read the contacts from a given contact file and return a
# list of names and email addresses

def get_contacts(filename):
    """
    Return two lists names, emails containing names and email addresses
    read from a file specified by filename.
    """
    names = []
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])
    return names, emails

def read_template(filename):
    """
    Returns a Template object comprising the contents of the 
    file specified by filename.
    """
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

def read_content(filename):
    """
    Returns a content object comprising the contents of the 
    file specified by filename.
    """
    with open(filename, 'r', encoding='utf-8') as content_file:
        result_file_content = content_file.read()
    return result_file_content

def connect_email_account(_host, _port, _address, _password):
    """
    set up the SMTP server
    """
    _s = smtplib.SMTP(host=_host, port=_port)
    _s.starttls()
    _s.login(_address, _password)
    return _s

def despatch_rider(
    _host=EMAIL_HOST, 
    _port=EMAIL_PORT, 
    _address=EMAIL_HOST_USER,
    _password=EMAIL_HOST_PASSWORD, 
    _receipents_file="mail_receipents.txt",
    _template_file="message.txt",
    _content_file="results.txt"):

    """
    It sends emails to receipents in receipents_file
    """

    names, emails = get_contacts(_receipents_file)
    message_template = read_template(_template_file)
    content = read_content(_content_file)
    
    s = connect_email_account(_host, _port, _address, _password)

    # For each contact, send the email:
    for name, email in zip(names, emails):
        msg = MIMEMultipart()       # create a message

        # add in the actual person name to the message template
        message = message_template.substitute(PERSON_NAME=name.title(), MAIL_CONTENT=content.title().lower())


        # Prints out the message body for our sake
        # print(message)

        # setup the parameters of the message
        msg['From']=_address
        msg['To']=email
        msg['Subject']="Today's search results..."
        
        # add in the message body
        msg.attach(MIMEText(message, 'plain'))
        
        # send the message via the server set up earlier.
        s.send_message(msg)
        # del msg
        
    # Terminate the SMTP session and close the connection
    s.quit()
    print("Emails sent successfully...")
    with open('exceptions.txt', 'a', encoding='utf-8') as exception:
        exception.write(f"\n** Emails sent successfully by dispatch_rider ...\n")


# despatch_rider(_content_file="keywords.txt")


def despatch_rider_HTML(
    _host=EMAIL_HOST, 
    _port=EMAIL_PORT, 
    _address=EMAIL_HOST_USER,
    _password=EMAIL_HOST_PASSWORD, 
    _receipents_file="mail_receipents.txt",
    _template_file="message.html",
    _content_file="results.txt"):

    """
    It sends emails to receipents in receipents_file
    """

    names, emails = get_contacts(_receipents_file)
    message_template = read_template(_template_file)
    content = read_content(_content_file)
    
    s = connect_email_account(_host, _port, _address, _password)

    # For each contact, send the email:
    for name, email in zip(names, emails):
        msg = MIMEMultipart()       # create a message

        # add in the actual person name to the message template
        message = message_template.substitute(PERSON_NAME=name.title(), MAIL_CONTENT=content)


        # Prints out the message body for our sake
        # print(message)

        # setup the parameters of the message
        msg['From']=_address
        msg['To']=email
        msg['Subject']="Today's search results..."
        
        # add in the message body
        msg.attach(MIMEText(message, 'html'))
        
        # send the message via the server set up earlier.
        s.send_message(msg)
        # del msg
        
    # Terminate the SMTP session and close the connection
    s.quit()
    print("Emails sent successfully in html format...")
    with open('exceptions.txt', 'a', encoding='utf-8') as exception:
        exception.write(f"\n** Emails sent successfully by dispatch_rider_html ...\n")