import requests
import sys
import string

DIRECTORY_URL = "https://xxxxxx/"

CREDS = ("xxxxxxx", "xxxxxx")


# username = 'bruno.' + ALC
# password = 'xxxxxxxx'
#firstname = sys.argv[3]
#lastname = sys.argv[4]
email = "bruno.xxxxx@xxxxxxx.com"
fullname = "Bruno Marques Test"

ID_TEMPLATE = """<Identity id="bruno.{}" password="xxxxxxx">
<Name>Bruno Test</Name>
<Email>bruno.xxxxx@xxxxxxx.com</Email>
<DataItem name="phoneNumber" value="(843)111-4200"/>
<DataItem name="serviceSetName" value="CRU_NY_HO"/>
<DataItem name="DateOfBirth" value=""/>
<Affiliation target="{}" type="agent_location" side="agent" targetName=""/>
<Affiliation target="P4-CRU" type="identity_program" side="identity"/>
<ApplicationSettings applicationName="xxxxxxxx" organizationId="ics" environmentName="production"/>
<ApplicationSettings applicationName="xxxxxxxx" organizationId="cru" environmentName="production">
<DataItem name="isPrimaryContact" value="false"/>
<DataItem name="isPrincipal" value="false"/>
<DataItem name="SecurityClearanceLevel" value="3"/>
<DataItem name="isLicensee" value="true"/>
<DataItem name="licenseNumber" value="191355"/>
<DataItem name="dateAppointed" value=""/>
<Roles>
<Role id="CRU_AGENT_NY_HO"/>
<Role id="CRU_SC_HO_PRODUCTGROUP1"/>
<Role id="UWQ_AGENT"/>
<Role id="CRU_SC_SL_PRODUCTGROUP1"/>
</Roles>
</ApplicationSettings>
</Identity>""" 


ALCs = [
"E30104N",
"E30106N",
"E30035N",
"E30105N",
"E30103N"

]

if __name__ == "__main__":
    for ALC in ALCs:
        import sys
        payload = ID_TEMPLATE.format(ALC, ALC)
        response = requests.post(DIRECTORY_URL, auth=CREDS, headers={"content-type": "application/xml"}, data=payload)
        print((response), " for identity bruno.{} ".format(ALC))

   