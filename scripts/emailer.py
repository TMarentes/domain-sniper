import smtplib, ssl
from email.message import EmailMessage


class Emailer:
    def send_email(domain, sender, receiver, sender_password):
        port = 465  
        smtp_server = "smtp.gmail.com"
        sender_email = sender  
        receiver_email = receiver 
        password = sender_password
        msg = EmailMessage()
        msg.set_content(f'Alert: {domain} is now available!')

        msg['Subject'] = f'{domain} is now available!'
        msg['From'] = sender_email
        msg['To'] = receiver_email

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.send_message(msg)
            server.quit()