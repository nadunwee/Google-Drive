# Google Drive Uploder
## Video Demo:  https://youtu.be/JLcxzZgMenw
## Description:
The program is a Python script that can upload files or folders to Google Drive using the Google Drive API. It can be executed from the command line, with
various arguments and options to control its behavior. 

#### -f in command line means upload only one file followed with file name you want to upload

The first part of the script is importing various modules needed for the program to function properly. These modules include os, sys, and various Google Drive
API modules such as google-auth, google-auth-oauthlib, google-auth-httplib2, and googleapiclient. The script then defines the SCOPES variable, which contains the
OAuth2 scopes required for the program to access and upload files to Google Drive.

Next, the script defines the arguments variable, which contains the allowed command-line arguments for the program. The script also defines the main function,
which is the entry point for the program. The main function checks the command-line arguments, and based on the arguments, calls either the upload_file or
upload_folder function.

The upload_file function takes in the authentication credentials, the file name, and the folder ID as parameters. The function then creates a Google Drive API
service object using the build method, passing in the required parameters such as the API name, version, and authentication credentials. The function then
creates a MediaFileUpload object for the file, with the mimetype set to "image/jpg" and the resumable parameter set to True. A file metadata dictionary is then
created, containing the file name and the folder ID where the file should be uploaded to.

The function then sends a request to upload the file to Google Drive using the service.files().create() method, passing in the file metadata and MediaFileUpload
objects, as well as the fields parameter set to "id" to retrieve the ID of the uploaded file. If the upload is successful, the function prints a message to the
console with the file name and the file ID.

The upload_folder function works similarly to the upload_file function, but instead of uploading a single file, it uploads all the files in a specified folder.
The function takes in the authentication credentials, the folder path, and the folder ID as parameters. The function then creates a Google Drive API service
object and iterates over all the files in the specified folder using the os.listdir() method.

For each file, the function creates a MediaFileUpload object with the file path, mimetype, and resumable set to True. A file metadata dictionary is then created
with the file name and the folder ID where the file should be uploaded to. The function then sends a request to upload the file to Google Drive using the service
files().create() method, passing in the file metadata and MediaFileUpload objects, as well as the fields parameter set to "id" to retrieve the ID of the uploaded
file. If the upload is successful, the function prints a message to the console with the file name and the file ID.

The script also defines several helper functions that are used by the main function and the upload functions. The argument_len function checks the number of
command-line arguments and returns True if the number of arguments is correct. The argument_check function checks the first command-line argument and returns
True if it is one of the allowed arguments. The directory function checks the first command-line argument and returns True if it is "-f", indicating that the
user wants to upload a single file.

Finally, the script checks if it is being executed as the main program using the if name == "main" statement. If it is, the main function is called. The main
function checks the command-line arguments and calls either the upload_file or upload_folder function depending on the argument provided. If there are any errors
during the execution of the program, error messages are printed to the console to inform the user.

Let me know if there are any further questions, comments, or concerns about this final.

This is CS50P!

