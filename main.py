from scripts.checker import Checker
from scripts.emailer import Emailer

# Enter the domains you wish to snipe
domains = ["example.com", "example.com.au"]

# Enter your email username (must be gmail)
sender_email = "x"

# Enter your gmail app-specific password
sender_password = "x"

# Enter notification receiving email address
receiver_email = "x"

# Enter GoDaddy API key details
godaddy_api = "x"
godaddy_secret = "x"


for i in domains:
    if Checker.check_godaddy(i, godaddy_api, godaddy_secret):
        Emailer.send_email(i, sender_email, receiver_email, sender_password)




