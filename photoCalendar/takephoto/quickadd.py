from __future__ import print_function
import sys
import os
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import datetime

class Event:
    def sendEvent(self, eventInfo):
        SCOPES = 'https://www.googleapis.com/auth/calendar'
        store = file.Storage("C:\\Users\\aahan\\Desktop\\Boilermake2018\\photoCalendar\\takephoto\\token.json")
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets("C:\\Users\\aahan\\Desktop\\Boilermake2018\\photoCalendar\\takephoto\\credentials.json", SCOPES)
            creds = tools.run_flow(flow, store)
        service = build('calendar', 'v3', http=creds.authorize(Http()))

        created_event = service.events().quickAdd(
            calendarId='primary',
            text=eventInfo).execute()

        print(created_event['id'])
