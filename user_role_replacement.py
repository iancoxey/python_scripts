import requests
import sys
import string
import xml.etree.ElementTree as ET
import xml.dom.minidom

DIRECTORY_URL = "https://xxxxxxxx/api/rest/v2/identities/"

CREDS = ("ian.coxey@xxxxxxxx.com", "xxxxxxxx")


new_pxserver_rights = """<ApplicationSettings applicationName="pxserver" organizationId="cru" environmentName="production"><DataItem name="SecurityClearanceLevel" value="3"/><DataItem name="isPrincipal" value="false"/><DataItem name="isLicensee" value="false"/><DataItem name="licenseNumber" value=""/><DataItem name="dateAppointed" value=""/><DataItem name="isPrimaryContact" value="false"/><Roles><Role id="UWQ_AGENT"/></Roles></ApplicationSettings>"""


def change_identity_roles():
    getidentity = requests.get(DIRECTORY_URL + identity, auth=CREDS)
    getidentitycontents = getidentity.content
    tree = ET.fromstring(getidentitycontents)
    child = ET.fromstring(new_pxserver_rights)

    for setting in tree.findall("./ApplicationSettings[@applicationName='pxserver']"):
        tree.remove(setting)
    tree.append(child)
    updated_id = ET.tostring(tree)
    response = requests.put(IXDIRECTORY_URL + identity, headers={"Content-Type": "application/xml"}, auth=CREDS, data=updated_id)
    print((response.status_code), "for identity {}".format(identity))

IDENTITIES_test = [

"68215f"]    

IDENTITIES = [



"alfa588",
"w500678f",
"w500664f",
"w500648f",
"w500632f",
"w500603f",
"196436",
"193085",
"192333",
"196723",
"19254x",
"192591",
"196765",
"192518"


]

if __name__ == "__main__":
    for identity in IDENTITIES:
        change_identity_roles()
