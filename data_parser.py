import json
from email import Email

def parse_email_thread(json_data):
    email_thread = []
    data = json.loads(json_data)

    for email_data in data['email_thread']:
        email_obj = Email(
            date=email_data['data'],
            author=email_data['author'],
            message=email_data['message']
        )
        email_thread.append(email_obj)

    return email_thread

def read_json_from_file(filename):
    with open(filename, 'r') as file:
        return file.read()
    

