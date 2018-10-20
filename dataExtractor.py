import os
import re
from googleplaces import GooglePlaces, types, lang

API_KEY = 'AIzaSyAVGOibW9k5jOPiZL_zfR1PHCbkkqXo08s'

google_places = GooglePlaces(API_KEY)
monthAbbreviations = {'jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'}

class InfoExtractor:

    date = ''
    time = ''
    locations = []
    titles = []
    
    def extractWords(self, list):
        global time
        global locations
        global date
        for i in range(0, len(list)):
            word = str(list[i])
            #checking date
            if re.match('[0-9]{1,2}/[0-9]{1,2}', word) is not None or re.match('[0-9]{1,2}\.[0-9]{1,2}', word) or re.match('[0-9]{1,2}\-[0-9]{1,2}', word):
                if list[i+1] != 'am' and list[i+1] != 'pm' and list[i][-2:] != 'am'  and list[i][-2:] != 'pm': # check if i+1 exists
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
                elif re.match('\d{1,2}\-\d{1,2}', extracted_time) is not None:
                    time = extracted_time + word[-2:]
                    continue
                elif re.match('\d{1,2}\:\d{2}', extracted_time) is not None:
                    time = extracted_time + word[-2:]
                    continue
                elif re.match('\d{1,2}', extracted_time) is not None:
                    time = extracted_time + word[-2:]
                    continue
           

            #checking location
            query_result = google_places.nearby_search(location='West Lafayette, United States', keyword=list[i])
            if len(query_result.places) > 0:
                location = query_result.places[0].name
                if i < len(list)-1:
                    self.locations.append(query_result.places[0].name + ' Room ' + list[i+1])
                else:
                    self.locations.append(query_result.places[0].name)

            if(i < 6):
                self.titles.append(list[i])
    def getDate(self):
        return date
    def getTime(self):
        return time
    def getLocations(self):
        return self.locations
    def getTitles(self):
        return self.titles




words_file = open("words.txt", 'r')
words = words_file.readlines()
for i in range(len(words)):
    words[i] = words[i][:-1]
print(words)

extractor = InfoExtractor()
extractor.extractWords(words)
print("Date: " + extractor.getDate())
print("Time: " + extractor.getTime())
print(extractor.getLocations())
print(extractor.getTitles())


