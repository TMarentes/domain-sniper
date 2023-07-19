import smtplib, ssl

class Emailer:
    def send_email(domain, sender, receiver, sender_password):
        port = 465  
        smtp_server = "smtp.gmail.com"
        sender_email = sender  
        receiver_email = receiver 
        password = sender_password
        message = f"""
        {domain} is now available!"""

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)