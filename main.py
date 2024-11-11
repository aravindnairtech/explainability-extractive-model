import torch
import json
import time
from summarizer import Summarizer
from data_parser import parse_email_thread, read_json_from_file

def main():

    json_input = read_json_from_file('threemonthseeded.json')
    emails = parse_email_thread(json_input)

    # Combine messages for summarization
    to_summarize = " ".join(email.message for email in emails)

    print("Original text:", to_summarize, "\n")

    # Initialize and apply the summarizer
    start = time.time() # Start timer
    model = Summarizer()
    result = model(to_summarize, num_sentences=4)

    # Print the summarized result
    print("Summary: ", result, "\n")
    print("Elapsed Time: ", time.time() - start) # End timer

if __name__ == "__main__":
    main()