import os
import re
from googleplaces import GooglePlaces, types, lang

API_KEY = 'AIzaSyAVGOibW9k5jOPiZL_zfR1PHCbkkqXo08s'

google_places = GooglePlaces(API_KEY)
monthAbbreviations = {'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'}

date = ''
time = ''
location = ''

def extractWords(list):
    global time
    global location
    global date
    for i in range(0, len(list)):
        word = str(list[i])
        #checking date
        if re.match('[0-9]{1,2}/[0-9]{1,2}', word) is not None or re.match('[0-9]{1,2}\.[0-9]{1,2}', word) or re.match('[0-9]{1,2}\-[0-9]{1,2}', word):
            date = word
            continue
        if word[-3:] in monthAbbreviations:
            if list[i+1] is not None:
                date += list[i+1]
                continue
        #checking time
        if word == 'am' or word == 'pm':
            if re.match('\d{1,2}\:\d{2}\-\d{1,2}\:\d{2}', list[i-1]) is not None:
                time = str(list[i-1][0:list[i-1].index('-')]) + word
                continue
            elif re.match('\d{1,2}\-\d{1,2}', list[i-1]) is not None:
                time = str(list[i-1][0:list[i-1].index('-')]) + word
                continue
            elif re.match('\d{1,2}\:\d{2}', list[i-1]) is not None:
                time = str(list[i-1]) + word
                continue
            elif re.match('\d{1,2}', list[i-1]) is not None:
                time = str(list[i-1]) + word
                continue

        elif word[-2:] == 'am' or word[-2:] == 'pm':
            time = word
            continue
        query_result = google_places.nearby_search(location='West Lafayette, United States', keyword=list[i])
        if len(query_result.places) > 0:
            location = query_result.places[0].name
            if list[i+1] is not None:
                location += ' Room ' + list[i+1]

 
        

list = ['6', 'am', 'LWSN', 'B160']
extractWords(list)
print(time)
print(location)


