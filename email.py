class Email:
    def __init__(self, date, author, message):
        self.date = date
        self.author = author
        self.message = message

    def __repr__(self): #reproduces email json format
        return f"Email(date={self.date}, author={self.author}, message={self.message})"