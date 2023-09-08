import smtplib
from email.message import EmailMessage

def send_email(subject, sender, receiver, body, password):
    # Create an email message object
    message = EmailMessage()

    # Set email headers
    message['Subject'] = subject
    message['From'] = sender
    message['To'] = receiver

    # Set email body text
    message.set_content(body)

    try:
        # Send the email
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender, password)
            server.send_message(message)
    except smtplib.SMTPException as e:
        click.echo(f'An error occurred while sending the email: {e}')