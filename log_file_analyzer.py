import re
import os

class LogFileAnalyzer:
    def __init__(self, filename):
        self.filename = filename
        self.data = ""

    def load_file(self):
        try:
            if not os.path.exists(self.filename):
                return "Error:File doesn't exist"
            with open(self.filename, "r") as f:
                self.data = f.read()
            print("File loaded successfully!")
        except FileNotFoundError as e:
            print("Error:", e)
        except Exception as e:
            print("An unexpected error occurred:", e)

    def find_emails(self):
        try:
            emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", self.data)
            return emails if emails else ["No emails found."]
        except re.error as e:
            print("Regex error:", e)
            return []

    def find_phone_numbers(self):
        try:
            phones = re.findall(r"\+?\d{2,3}[-.\s]?\d{3}[-.\s]?\d{4,}", self.data)
            return phones if phones else ["No phone numbers found."]
        except re.error as e:
            print("Regex error:", e)
            return []

    def find_errors(self):
        try:
            errors = re.findall(r"ERROR:.*", self.data)
            return errors if errors else ["No error messages found."]
        except re.error as e:
            print("Regex error:", e)
            return []
        
    def find_warnings(self):
        try:
            errors = re.findall(r"WARNING .*", self.data)
            return errors if errors else ["No warning messages found."]
        except re.error as e:
            print("Regex error:", e)
            return []
        
filename = input("Enter log file name (e.g., abc.log): ")
analyzer = LogFileAnalyzer(filename)

if 'Error' in analyzer.load_file():
    print(analyzer.load_file())
    exit()
while True:
    print("\n--- Log File Analyzer ---")
    print("1. Find Emails")
    print("2. Find Phone Numbers")
    print("3. Find Error Messages")
    print("4. Find Warning Messages")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Emails found:", analyzer.find_emails())
    elif choice == "2":
        print("Phone numbers found:", analyzer.find_phone_numbers())
    elif choice == "3":
        print("Error messages found:", analyzer.find_errors())
    elif choice == '4':
        print('Warning messages found:',analyzer.find_warnings())
    elif choice == "5":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Try again!")

