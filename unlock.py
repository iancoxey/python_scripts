import requests

BODY = """<PolicyChangeSet schemaVersion="2.1" username="xxxxxxxx" description="Unlocking re H4">
  <Flags>
    <Flag name="UnderwritingExceptionAutoResolveWorkflow" value="false"/>
    <Flag name="UnderwritingExceptionEffectiveDate" value="false"/>
  </Flags>
</PolicyChangeSet>"""

CREDS = ("xxxxxxxx", "xxxxxxxx")

URL = "https://xxxxxxxx/api/rest/v1/policies/cru4q-xxxxxxxx"

URL = "https://xxxxxxxx/api/rest/v1/policies/CRU4Q-xxxxxxxx"

URL_TMPL = "https://xxxxxxxx/api/rest/v1/policies/{0}"


BODY =  """<PolicyChangeSet schemaVersion="2.1" username="xxxxxxxx.xxxxxxxx@xxxxxxxx.com" description="Unlocking re H4">
  <Flags>
    <Flag name="locked" value="false"/>
  </Flags>
</PolicyChangeSet>"""




POLICIES = ["612988"]

POLICIES = ["613746"]

POLICIES = ["626585"] #H




if __name__ == "__main__":
    import sys
    if len(sys.argv) == 2:
        url = URL_TMPL.format(sys.argv[1])
        response = requests.post(url, auth=CREDS, headers={"content-type": "application/xml"}, data=BODY)
        print(response)
