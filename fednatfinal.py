import requests
import sys
import string
import xml.etree.ElementTree as ET
import xml.dom.minidom
import random


DIRECTORY_URL = "https://xxxxxxxx/identities/"

ASSIGNEE_LIST_URL = "https://xxxxxxxx/assignee_list.xml"

CREDS = ("xxxxxxxx", "xxxxxxxx")

PASSWORD_SET = string.ascii_lowercase + string.ascii_uppercase + string.digits

username = sys.argv[1]
firstname = sys.argv[2]
lastname = sys.argv[3]
email = sys.argv[1]
fullname = firstname + " " + lastname

new_id_line = """Assignee identity="%s" active="false" """ % (username)

ID_TEMPLATE = """<Identity id="{}" password="{}">
<Name>{}</Name>
<Email>{}</Email>
<Affiliation target="fnic" type="employee_company" side="employee" targetName="xxxxxxxx" primary="1" />
  <Affiliation target="P1-FNIC" type="identity_program" side="identity" />
  <ApplicationSettings applicationName="xxxxxxxx" organizationId="fnic" environmentName="production">
    <roles>backoffice</roles>
  </ApplicationSettings>
  <ApplicationSettings applicationName="xxxxxxxx" organizationId="ics" environmentName="production">
    <DashboardPreferences controlPanelOpen="true" helpDrawerOpen="false">
      <Widgets />
    </DashboardPreferences>
    <PoliciesModule>
      <Rights>
        <Right>MANAGE_ASSIGNEES</Right>
        <Right>ARCHIVE_POLICY</Right>
        <Right>UNBIND_POLICY</Right>
        <Right>ENTER_UW_TASK</Right>
        <Right>RESOLVE_UW_TASK</Right>
        <Right>REMOVE_FLAG</Right>
        <Right>SHOW_REPLY_BUTTON</Right>
        <Right>VIEW_ADVANCED</Right>
      </Rights>
    </PoliciesModule>
    <tentacleLink path="production-fnic-agenciesV2" />
    <tentacleLink path="production-fnic-policies_fnicfl" />
    <tentacleLink path="production-fnic-reports" />
  </ApplicationSettings>
  <ApplicationSettings applicationName="xxxxxxxx" organizationId="ics" environmentName="production">
    <roles>backoffice</roles>
  </ApplicationSettings>
  <ApplicationSettings applicationName="xxxxxxxx" organizationId="insight" environmentName="production">
    <access>
      <role>FnicUser</role>
    </access>
  </ApplicationSettings>
  <ApplicationSettings applicationName="xxxxxxxx-api" organizationId="fnic-1" environmentName="production">
    <roles>admin</roles>
  </ApplicationSettings>
  <ApplicationSettings applicationName="xxxxxxxx" organizationId="cru" environmentName="production">
    <DataItem name="isPrimaryContact" value="false" />
    <DataItem name="dateAppointed" value="" />
    <DataItem name="licenseNumber" value="" />
    <DataItem name="isLicensee" value="false" />
    <DataItem name="isPrincipal" value="false" />
    <DataItem name="SecurityClearanceLevel" value="3" />
    <Roles>
      <Role id="CRU_AGENT_FL_HO" />
      <Role id="UWQ_AGENT" />
    </Roles>
  </ApplicationSettings>
</Identity>"""

#This creates the new user in xxxxxxxx
def create_user():
    payload = ID_TEMPLATE.format(sys.argv[1], password, fullname, sys.argv[1])
    response = requests.post(DIRECTORY_URL, headers={"Content-Type": "application/xml"}, auth=CREDS, data=payload)
    print(response)

#This adds the user to the end of the assignee list xml
def add_to_list():
    getlist = requests.get(ASSIGNEE_LIST_URL, auth=CREDS)
    getlistcontents = getlist.content
    tree = ET.fromstring(getlistcontents)
    child = ET.Element(new_id_line)
    tree.append(child)
    list = ET.tostring(tree)
    #print(list)
    response = requests.put(ASSIGNEE_LIST_URL, headers={"Content-Type": "application/xml"}, auth=CREDS, data=list)
    print(response)

#This creates the users new password - a random 10 digit string
def make_password():
    return ''.join(
        random.choice(PASSWORD_SET) 
        for _ in range(10)
    )
    
if __name__ == "__main__":
    make_password()
    password=make_password()
    import sys
    if len(sys.argv) == 4:
       create_user()
    print "This is the new password: %s" % password
    add_to_list()