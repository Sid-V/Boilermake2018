import os
import re
from googleplaces import GooglePlaces, types, lang

API_KEY = 'AIzaSyAVGOibW9k5jOPiZL_zfR1PHCbkkqXo08s'

google_places = GooglePlaces(API_KEY)
monthAbbreviations = {'jan', 'feb', 'mar', 'apr', 'may', 'jun', 'Jul', 'aug', 'Sep', 'Oct', 'Nov', 'Dec'}

date = ''
time = ''
locations = []
titles = []

def extractWords(list):
    global time
    global location
    global date
    for i in range(0, len(list)):
        word = str(list[i])
        #checking date
        if re.match('[0-9]{1,2}/[0-9]{1,2}', word) is not None or re.match('[0-9]{1,2}\.[0-9]{1,2}', word) or re.match('[0-9]{1,2}\-[0-9]{1,2}', word):
            if list[i+1] != 'am' and list[i+1] != 'pm': # check if i+1 exists
                date = word
                continue
        if word[:3].lower() in monthAbbreviations:
            if list[i+1] is not None:
                date = list[i] + " "
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
                time = extracted_time + word[-2:]
                continue
                #time = str(list[i-1][0:list[i-1].index('-')]) + word
            elif re.match('\d{1,2}\-\d{1,2}', extracted_time) is not None:
                time = extracted_time + word[-2:]
                continue
                #time = str(list[i-1][0:list[i-1].index('-')]) + word
            elif re.match('\d{1,2}\:\d{2}', extracted_time) is not None:
                time = extracted_time + word[-2:]
                continue
                #time = str(list[i-1]) + word
            elif re.match('\d{1,2}', extracted_time) is not None:
                time = extracted_time + word[-2:]
                continue
            #else:
            #    continue

        #checking location
        query_result = google_places.nearby_search(location='West Lafayette, United States', keyword=list[i])
        if len(query_result.places) > 0:
            location = query_result.places[0].name
            if i < len(list)-1:
                locations.append(query_result.places[0].name + ' Room ' + list[i+1])
            else:
                locations.append(query_result.places[0].name)

        if(i < 6):
            titles.append(list[i])

list = ['6-7', 'am', 'LWSN', 'B160','go', 'slam', 'August', '29th']
extractWords(list)
print(date)
print(time)
print(locations)
print(titles)
