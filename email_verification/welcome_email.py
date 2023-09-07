import logging
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def send_email(to_email, verification_id):
    message = Mail(
        from_email='support@billtheai.com',
        to_emails=to_email,
        subject='Verify Your Email')
    message.dynamic_template_data = {
        'email': to_email,
        'id': str(verification_id),
    }
    message.template_id = 'd-f83d49604feb4a1ab58866237e464fdd'
    try:
        sg = SendGridAPIClient(os.getenv('SENDGRID_API_KEY'))
        sg.send(message)
    except Exception as e:
        logging.warning(e)
