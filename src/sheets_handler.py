from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import os
import pickle
from typing import List, Dict

class GoogleSheetsHandler:
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    
    def __init__(self, credentials_file: str, sheet_id: str):
        self.credentials_file = credentials_file
        self.sheet_id = sheet_id
        self.creds = None
        self.service = None
        self._authenticate()

    def _authenticate(self):
        """Authenticate with Google Sheets API."""
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                self.creds = pickle.load(token)

        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    self.credentials_file, self.SCOPES)
                self.creds = flow.run_local_server(port=0)

            with open('token.pickle', 'wb') as token:
                pickle.dump(self.creds, token)

        self.service = build('sheets', 'v4', credentials=self.creds)

    def read_topics(self, range_name: str) -> List[Dict]:
        """Read topics from the specified range in the Google Sheet."""
        sheet = self.service.spreadsheets()
        result = sheet.values().get(
            spreadsheetId=self.sheet_id,
            range=range_name
        ).execute()
        
        values = result.get('values', [])
        topics = []
        
        for i, row in enumerate(values):
            if not row:
                continue
                
            topic = {
                'topic': row[0] if len(row) > 0 else '',
                'status': row[1] if len(row) > 1 else '',
                'generated_post': row[2] if len(row) > 2 else '',
                'row_index': i + 2  # +2 because range starts from A2
            }
            
            # Only include rows with topics and no generated content
            if topic['topic'] and topic['status'] != 'Generated':
                topics.append(topic)
                
        return topics

    def update_post(self, row_index: int, post_content: str):
        """Update the generated post and status in the sheet."""
        range_name = f'B{row_index}:C{row_index}'
        values = [['Generated', post_content]]
        
        body = {
            'values': values
        }
        
        self.service.spreadsheets().values().update(
            spreadsheetId=self.sheet_id,
            range=range_name,
            valueInputOption='RAW',
            body=body
        ).execute()
