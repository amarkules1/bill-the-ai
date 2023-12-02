import logging
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def send_email(to_email, token):
    message = Mail(
        from_email='support@billtheai.com',
        to_emails=to_email,
        subject='Reset Password')
    message.dynamic_template_data = {
        'email': to_email,
        'token': str(token),
    }
    message.template_id = 'd-31f5e6c5fc704f1a8cf519e2342eadb4'
    try:
        sg = SendGridAPIClient(os.getenv('SENDGRID_API_KEY'))
        sg.send(message)
    except Exception as e:
        logging.warning(e)
