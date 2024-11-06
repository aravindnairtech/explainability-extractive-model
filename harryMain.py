import torch
import json
from summarizer import Summarizer

to_summarize = ""
with open('emaildata.json') as f:
    for element['message'] in f: #Consolidate the data into one variable
        to_summarize += element + " "

print("Original text: " + to_summarize)

model = Summarizer()
result = model(to_summarize, num_sentences=1)

print(result)