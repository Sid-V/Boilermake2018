import os
import re
from googleplaces import GooglePlaces, types, lang

API_KEY = 'AIzaSyAVGOibW9k5jOPiZL_zfR1PHCbkkqXo08s'

google_places = GooglePlaces(API_KEY)
monthAbbreviations = {'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'}

date = ''
time = ''
locations = []

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
            extracted_time = word[:-2]
            if re.match('\d{1,2}\:\d{2}\-\d{1,2}\:\d{2}', extracted_time) is not None:
                time = str(list[i-1][0:list[i-1].index('-')]) + word
            elif re.match('\d{1,2}\-\d{1,2}', extracted_time) is not None:
                time = str(list[i-1][0:list[i-1].index('-')]) + word
            elif re.match('\d{1,2}\:\d{2}', extracted_time) is not None:
                time = str(list[i-1]) + word
            elif re.match('\d{1,2}', extracted_time) is not None:
                time = str(list[i-1]) + word
            else:
                continue
            time = extracted_time + word[-2:]
            continue

        #checking location
        query_result = google_places.nearby_search(location='West Lafayette, United States', keyword=list[i])
        if len(query_result.places) > 0:
            location = query_result.places[0].name
            if i < len(list) or list[i+1] is not None:
                locations.append(query_result.places[0].name + ' Room ' + list[i+1])
            else:
                locations.append(query_result.places[0].name)

list = ['6', 'am', 'LWSN', 'B160','go', 'slam']
extractWords(list)
print(time)
print(locations)


