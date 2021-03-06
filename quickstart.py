from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import datetime
from gtts import gTTS
import os
import sys
import multiprocessing
import time

from pynput.keyboard import Key, Controller
keyboard = Controller()


SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
store = file.Storage('credentials.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = build('calendar', 'v3', http=creds.authorize(Http()))
now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
events_result = service.events().list(calendarId='primary', timeMin=now,
                                      maxResults=10, singleEvents=True,
                                      orderBy='startTime').execute()
events = events_result.get('items', [])
if not events:
    tmp='No upcoming events found.'
    tts = gTTS(text=tmp, lang='en')
    tts.save("tmp.mp3")
    def foo2(n):
        os.system('dlnast tmp.mp3')
    
    if __name__ == '__main__':
	    # Start foo as a process
	    p = multiprocessing.Process(target=foo2, name="Foo2", args=(10,))
	    p.start()

	    # Wait 10 seconds for foo
	    time.sleep(10)
	    #print ("q")
	    keyboard.press('q')
	    time.sleep(10)

	    # Terminate foo
	    p.terminate()

	    # Cleanup
	    p.join()
	    #os.system("mpg123 tmp.mp3")
for event in events:
    start = event['start'].get('dateTime', event['start'].get('date'))
    tmp="you have an event on"+ " "+ str(event['summary']) + " at " +str(start)
    print(tmp)
    tts = gTTS(text=tmp, lang='en')
    tts.save("tmp.mp3")
    def foo(n):
        os.system('dlnast tmp.mp3')
    if __name__ == '__main__':
	    # Start foo as a process
	    p = multiprocessing.Process(target=foo, name="Foo", args=(10,))
	    p.start()

	    # Wait 10 seconds for foo
	    time.sleep(10)
	    print ("q")
	    keyboard.press('q')
	    time.sleep(10)

	    # Terminate foo
	    p.terminate()

	    # Cleanup
	    p.join()
