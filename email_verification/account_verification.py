import logging
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def send_email(to_email, token):
    message = Mail(
        from_email='support@billtheai.com',
        to_emails=to_email,
        subject='Verify Your Email')
    message.dynamic_template_data = {
        'email': to_email,
        'token': str(token),
    }
    message.template_id = 'd-7432bef69ede4c2d9ef378d7fd458319'
    try:
        sg = SendGridAPIClient(os.getenv('SENDGRID_API_KEY'))
        sg.send(message)
    except Exception as e:
        logging.warning(e)
