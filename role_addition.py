import requests
import sys
import string
import xml.etree.ElementTree as ET
import xml.dom.minidom
from time import sleep

DIRECTORY_URL = "https://xxxxxxxx/api/rest/v2/identities/"


CREDS = ("xxxxxxxx", "xxxxxxxx")

new_role_line = """<Role id="SIC_LA_HO_PRODUCTGROUP1" />"""



def change_identity_roles():
    getidentity = requests.get(DIRECTORY_URL + identity, auth=CREDS)
    getidentitycontents = getidentity.content
    tree = ET.fromstring(getidentitycontents)
    child = ET.fromstring(new_role_line)

    for setting in tree.findall("./ApplicationSettings[@applicationName='xxxxxxxx']/Roles"):
        setting.append(child)
    updated_id = ET.tostring(tree)
    response = requests.put(IXDIRECTORY_URL + identity, headers={"Content-Type": "application/xml"}, auth=CREDS, data=updated_id)
    print((response.status_code), "for identity {}".format(identity))
    sleep(2)


IDENTITIES = [

"suzannem"

]

if __name__ == "__main__":
    for identity in IDENTITIES:
        change_identity_roles()
