import pymssql
import sys
import json
import string
from collections import namedtuple
import random
from xml.etree import ElementTree as etree

import requests

DbConn = namedtuple("DBConnection", "server username password db_name")

PXSERVER_DB = DbConn(
    server = "xxx",
    username = "xxx",
    password = "xxx",
    db_name = "xxx"
)

def make_connection_from_dbconn(dbconn):
    return pymssql.connect(
        dbconn.server, dbconn.username, dbconn.password, dbconn.db_name
    )

CREDS = ("xxx", "xxx")

IDENTITIES_URL = "xxx"
IDENTITY_URL = "xxx"

UNARCHIVE_USER = """
UPDATE IdentityVersions 
SET Archived=0 
WHERE IdentityID=%(id)s AND Version = (
    SELECT MAX([Version])FROM IdentityVersions WHERE IdentityID=%(id)s
)"""

IS_AGENT_XPATH = "./Affiliation[@type='agent_location'][@side='agent']"

def is_pxserver_user(identity_xml):
    """Check the XML to determine whether this user has a pxServer account."""
    if identity_xml.find(IS_AGENT_XPATH) is not None:
        return True
    
    return False

def unarchive(USER_ID, dry_run=True):
    # ixDirectory http requests start here
    
    identity_url = IDENTITY_URL.format(USER_ID)

    response = requests.get(identity_url, auth=CREDS)
    if response.status_code != 200:
        raise Exception("Got a {} trying to retrieve {}".format(
            response.status_code, identity_url
        ))
    
    identity = etree.fromstring(response.content)
    
    identity.set("archived", "false")
    
    if not dry_run:
        response = requests.put(identity_url, auth=CREDS, data=etree.tostring(identity), headers={"content-type": "application/xml"})
        print(response.status_code)

    # Database stuff from here on down

    if is_pxserver_user(identity):
        print("is pxServer user, unarchiving there.")
        pxserver_conn = make_connection_from_dbconn(PXSERVER_DB)
        cursor = pxserver_conn.cursor(True)
    
        cursor.execute(UNARCHIVE_USER, dict(id=USER_ID))
    
        if dry_run:
            pxserver_conn.rollback()
        else:
            pxserver_conn.commit()
        pxserver_conn.close()

if __name__ == '__main__':
    if len(sys.argv) == 2:
        unarchive(sys.argv[1], dry_run=False)