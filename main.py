import torch
import json
from summarizer import Summarizer
from data_parser import parse_email_thread, read_json_from_file
def main():

    json_input = read_json_from_file('emaildata.json')
    emails = parse_email_thread(json_input)

    # Combine messages for summarization
    to_summarize = " ".join(email.message for email in emails)

    print("Original text:", to_summarize)

    # Initialize and apply the summarizer
    model = Summarizer()
    result = model(to_summarize, num_sentences=2)

    # Print the summarized result
    print("Summary:", result)

if __name__ == "__main__":
    main()