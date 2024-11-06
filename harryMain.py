import torch
import json
from summarizer import Summarizer

json_f = open('emaildata.json')
email_json = json.load(json_f)

to_summarize = ""
for element in email_json: #Consolidate the data into one variable
    to_summarize += element + " "

json_f.close()

print("Original text: " + to_summarize)

model = Summarizer()
result = model(to_summarize, num_sentences=1)

print(result)