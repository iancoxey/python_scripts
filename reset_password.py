import random
import re
import string
import sys
from xml.etree import cElementTree as etree

import requests

CREDS = ("xxxxxxxx", "xxxxxxxx")

IDENTITY_URL = "https://xxxxxxxx/api/rest/v2/identities/{}"

HEADERS = {"content-type": "application/xml"}

PASSWORD_SET = string.ascii_lowercase + string.ascii_uppercase + string.digits

#This creates the users new password - a random 10 digit string
def make_password():
    return ''.join(
        random.choice(PASSWORD_SET) 
        for _ in range(10)
    )

def change_password(username, password):
    url = IDENTITY_URL.format(username)
    response = requests.get(url, auth=CREDS)
    if response.status_code != 200:
        raise Exception("Problem retrieving account: {}".format(response.content))
        
    identity_xml = etree.fromstring(response.content)

    # Remove those things that don't belong when updating:
    for attr in ["passwordHash"]:
        identity_xml.attrib.pop(attr)
    
    identity_xml.set("password", password)
    
    response = requests.put(url, auth=CREDS, data=etree.tostring(identity_xml), headers=HEADERS)    
    if response.status_code != 200:
        raise Exception("Problem changing password: {}".format(response.content))

users = [
    "ian.coxey@xxxxxxxx.com"
]

if __name__ == "__main__":
    for user in list(users):
    #user = sys.argv[1]
        password = ""
    while re.search(r"\d+", password) is None:
        password = make_password()
        
    print("Attempting to set password for {} to: '{}'".format(user, password))

    change_password(user, password)