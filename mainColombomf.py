import nltk 
nltk.download('stopwords') 
nltk.download('punkt_tab')
import json
import time
from data_parser import parse_email_thread, read_json_from_file
from text_summarizer import text_summarizer

def main():

    json_input = read_json_from_file('threemonthseeded.json')
    emails = parse_email_thread(json_input)

    # Combine messages for summarization
    to_summarize = " ".join(email.message for email in emails)

    print("Original text:", to_summarize, "\n")

    # Initialize and apply the summarizer
    start = time.time() # Start timer
    result = text_summarizer(to_summarize, num_sentences=3)

    # Print the summarized result
    print("Summary: ", result, "\n")
    print("Elapsed Time: ", round(time.time() - start, 2)) # End timer

if __name__ == "__main__":
    main()