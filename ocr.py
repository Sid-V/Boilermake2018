import requests
import string
import os
import re

subscription_key = "19dde31a0dbb46b09ad2c6331a851bc0"
assert subscription_key

vision_base_url = "https://eastus.api.cognitive.microsoft.com/vision/v2.0/"

ocr_url = vision_base_url + "ocr"

# Set image_url to the URL of an image that you want to analyze.
image_url = "https://images.collegiatelink.net/clink/images/1f3abac2-2232-4f0a-bfa6-5d601b2f55dad87b412b-2515-48d7-8f64-82be101089d5.jpg?preset=med-w"
image_url2 = "https://calendar.purdue.edu/calendar/displaymedia.aspx?whatToDo=picture&id=100697"
image_url3 = "https://pbs.twimg.com/media/Dl0AOOuXoAA8q0c.jpg"

headers = {'Ocp-Apim-Subscription-Key': subscription_key}
params  = {'language': 'unk', 'detectOrientation': 'true'}
data    = {'url': image_url3}
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

#wordList = [''.join(c for c in s if c is not [':','\','/'] and c not in string.punctuation) for s in wordList]

print(wordList)
# Write words into file for extraction
with open('words.txt', 'w') as f:
    for word in wordList:
        f.write("%s\n" % word)
