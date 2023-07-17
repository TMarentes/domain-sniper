
from scripts.logic import Logic

# Enter the domains you wish to snipe
domains = ["example.com", "example.com.au"]

# Enter your email username (must be gmail)
sender_email = ""

# Enter your gmail app-specific password
sender_password = ""

# Enter notification receiving email address
receiver_email = ""

# Enter GoDaddy API key details
godaddy_api = ""
godaddy_secret = ""


Logic.logic(domains, godaddy_api, godaddy_secret, sender_email, receiver_email, sender_password)




