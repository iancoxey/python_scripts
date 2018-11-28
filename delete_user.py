import requests
import string
import sys

CREDS = ("xxxxxxxx", "xxxxxxxx")

prod_directory_url = "https://xxxxxxxx/identities/"
stage_directory_url = "https://xxxxxxxx/api/rest/v2/identities/"
uat_directory_url = "https://xxxxxxxx/api/rest/v2/identities/"


def delete_user_prod(username):
    response = requests.delete(prod_directory_url + username, headers={"Content-Type": "application/xml"}, auth=CREDS)
    if response.status_code == 204:
        print("Deleted user {} in production".format(username))
    if response.status_code == 404:
        print("User {} not found or already archived in production directory".format(username))

def delete_user_stage(username):
    response = requests.delete(stage_directory_url + username, headers={"Content-Type": "application/xml"}, auth=CREDS)
    if response.status_code == 204:
        print("Deleted user {} in staging".format(username))
    if response.status_code == 404:
        print("User {} not found or already archived in staging directory".format(username))

def delete_user_uat(username):
    response = requests.delete(uat_directory_url + username, headers={"Content-Type": "application/xml"}, auth=CREDS)
    if response.status_code == 204:
        print("Deleted user {} in UAT".format(username))
    if response.status_code == 404:
        print("User {} not found or already archived in UAT directory".format(username))

if __name__ == "__main__":
    if len(sys.argv) == 2:
        username = sys.argv[1]
    delete_user_prod(username)
    delete_user_stage(username)
    delete_user_uat(username)