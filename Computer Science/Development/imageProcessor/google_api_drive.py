from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.http import MediaFileUpload

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive']

def main():
    creds = None
    if os.path.exists('token.pickle'):                  #if directory has token
        with open('token.pickle', 'rb') as token:       #load credentials
            creds = pickle.load(token)

    drive_service = build('drive', 'v3', credentials=creds) #create drive service object
    folder_id = '1mm9iGSsvps9T8nuc5vADLsOFLWdpvXYS' #load drive folder id
    file_metadata = {                               #load metadata for image
        'name': '0.jpg',                    
        'parents': [folder_id]
    }
    media = MediaFileUpload('images/0.jpg', mimetype='image/jpeg') # tell googledrive what kind of file is to be uploaded
    file = drive_service.files().create(body=file_metadata,media_body=media,fields='id').execute()  #upload the image
    print ("Uploading Image ")
    print (file.get('name'))

if __name__ == '__main__':
    main()
