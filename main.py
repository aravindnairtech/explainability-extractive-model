import torch
import json
from summarizer import Summarizer
from data_parser import parse_email_thread, read_json_from_file
def main():

    json_input = read_json_from_file('emaildata.json')
    emails = parse_email_thread(json_input)
    for email in emails:
        print(email)

    to_summarize = ""
    for element in emails: #Consolidate the data into one variable
        to_summarize += element + " "

    # json_f.close()

    print("Original text: " + to_summarize)

    model = Summarizer()
    result = model(to_summarize, num_sentences=1)

    print(result)

if __name__ == "__main__":
    main()