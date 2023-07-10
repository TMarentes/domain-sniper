from scripts.checker import Checker
from scripts.emailer import Emailer

domains = ["example.com", "example.com.au"]

for i in domains:
    if Checker.check_godaddy(i):
        Emailer.send_email(i)




