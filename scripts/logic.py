from scripts.checker import Checker
from scripts.emailer import Emailer


class Logic:
    def logic(domains, godaddy_api, godaddy_secret, sender_email, receiver_email, sender_password):
        for i in domains:
            if Checker.check_godaddy(i, godaddy_api, godaddy_secret):
                Emailer.send_email(i, sender_email, receiver_email, sender_password)