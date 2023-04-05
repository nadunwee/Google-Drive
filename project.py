from __future__ import print_function

import os
import sys

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload


# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/drive.file"]

arguments = ["-f", "-fs"]


def main():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    instructions()
    folder_id = "1q4_cTTVuAVFsg360c1xej1QiZw5otQ36"
    if argument_len(len(sys.argv)):
        if argument_check(sys.argv[1]):
            if directory(sys.argv[1]):
                file_name = sys.argv[2]
                upload_file(authentication(), file_name, folder_id)
            else:
                folder_path = "/workspaces/84174559/project/Saved_Pictures"
                upload_folder(authentication(), folder_path, folder_id)
        else:
            sys.exit("wrong arguments")
    else:
        sys.exit()


def argument_len(len_arg):
    if len_arg < 3:
        sys.exit('not enough command line arguments')
    elif len_arg > 3:
        sys.exit('too much command line arguments')
    return True


def argument_check(arg1):
    if arg1 in arguments:
        return True
    else:
        return False


def directory(arg1):
    if arg1 == "-f":
        return True
    else:
        return False


def authentication():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    return creds


def upload_file(authentication, file_name, folder_id):
    try:
        service = build("drive", "v3", credentials=authentication)

        # create a MediaFileUpload object for the file
        file = MediaFileUpload(file_name, mimetype="image/jpg", resumable=True)

        # create a file resource with metadata
        file_metadata = {"name": file_name, "parents": [folder_id]}

        # send a request to upload the file
        uploaded_file = (
            service.files()
            .create(body=file_metadata, media_body=file, fields="id")
            .execute()
        )

        print(
            f'File {file_name} uploaded 😎 to Google Drive with 🆔: {uploaded_file.get("id")} ✨'
        )

    except HttpError as error:
        print(f"An error occurred: {error}")


def upload_folder(authentication, folder_path, folder_id):
    try:
        service = build("drive", "v3", credentials=authentication)

        # iterate over all files in the folder
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)

            # create a MediaFileUpload object for the file
            file = MediaFileUpload(file_path, mimetype="image/jpg", resumable=True)

            # create a file resource with metadata
            file_metadata = {"name": filename, "parents": [folder_id]}

            # send a request to upload the file
            uploaded_file = (
                service.files()
                .create(body=file_metadata, media_body=file, fields="id")
                .execute()
            )

            print(
                f'File {filename} uploaded 😎 to Google Drive with 🆔: {uploaded_file.get("id")} ✨'
            )

    except HttpError as error:
        print(f"An error occurred: {error}")


if __name__ == "__main__":
    main()
