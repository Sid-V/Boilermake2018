import requests
import string
import os
import re
from dataExtractor import InfoExtractor
from quickadd import Event

subscription_key = "19dde31a0dbb46b09ad2c6331a851bc0"
assert subscription_key

vision_base_url = "https://eastus.api.cognitive.microsoft.com/vision/v2.0/"

ocr_url = vision_base_url + "ocr"

# Set image_url to the URL of an image that you want to analyze.
<<<<<<< HEAD
image_url = "https://images.collegiatelink.net/clink/images/1f3abac2-2232-4f0a-bfa6-5d601b2f55dad87b412b-2515-48d7-8f64-82be101089d5.jpg?preset=med-w"
image_url2 = "https://calendar.purdue.edu/calendar/displaymedia.aspx?whatToDo=picture&id=100697"
image_url3 = "https://engineering.purdue.edu/AAE/events/2017/20170829-SEDS-Callout-YPAC/Fall%202017%20SEDS%20Callout%20Flyer.jpg"
=======
image_url = "https://calendar.purdue.edu/calendar/displaymedia.aspx?whatToDo=picture&id=100697"
>>>>>>> d21dc640d479d0233184d3256ef9411b9a845479

headers = {'Ocp-Apim-Subscription-Key': subscription_key}
params  = {'language': 'unk', 'detectOrientation': 'true'}
data    = {'url': image_url}
response = requests.post(ocr_url, headers=headers, params=params, json=data)
response.raise_for_status()

# Convert to json
analysis = response.json()

# Extract the word bounding boxes and text.
line_infos = [region["lines"] for region in analysis["regions"]]
word_infos = []
for line in line_infos:
    for word_metadata in line:
        for word_info in word_metadata["words"]:
            word_infos.append(word_info)
wordList = []
# Add words to list and make all lowercase
for word in word_infos:
    word = word['text']
    newWord = re.sub('[^-A-Za-z0-9:\/]+','',word)
    wordList.append(newWord.lower())
# remove punctuation

print(wordList)
# Write words into file for extraction
extractor = InfoExtractor()
extractor.extractWords(wordList)
<<<<<<< HEAD
print("Date: " + extractor.getDate())
print("Time: " + extractor.getTime())
print(extractor.getLocations())
print(extractor.getTitles())
=======

date = extractor.getDate()
time = extractor.getTime()
locations = extractor.getLocations()
titles = extractor.getLocations()
print(date)
print(time)
print(locations)
print(titles)

command = titles[0] + " at " + locations[0] + " on " + date + " at " + time
print(command)
event = Event()
event.sendEvent(command) # send command to google calender event quick add
>>>>>>> d21dc640d479d0233184d3256ef9411b9a845479
