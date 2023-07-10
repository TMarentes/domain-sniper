import requests
from urllib.request import Request, urlopen
import json


class Checker:
    def __init__ (self):
        pass

    def check_wix(domain):
        headers={'Authorization': "x"}
        test_domain = domain
        r = requests.get('https://www.wixapis.com/domain-search/v2/check-domain-availability?domain=' + test_domain, headers)
        return(r.json()["availability"]["available"])
    
    def check_godaddy(domain, godaddy_api, godaddy_secret):
        req = Request('https://api.godaddy.com/v1/domains/available?domain='+ domain)
        req.add_header('Authorization', 'sso-key '+godaddy_api+':'+godaddy_secret)
        content = urlopen(req).read()
        x = json.loads(content.decode('utf-8'))
        return(x["available"])
