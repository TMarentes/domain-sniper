import smtplib, ssl

class Emailer:
    def send_email(domain):
        port = 465  # For SSL
        smtp_server = "smtp.gmail.com"
        sender_email = "x@gmail.com"  # Enter your address
        receiver_email = "x@gmail.com"  # Enter receiver address
        password = "x"
        message = f"""\
        From: Python


        {domain} is now available!"""

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)