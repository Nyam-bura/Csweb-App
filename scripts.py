import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MessagingApp.settings")
django.setup()

import csv
from Messages.models import Message  # Replace 'your_app' with the actual name of your Django app

def import_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            process_and_save_record(row)

def process_and_save_record(record):
    # Assuming 'YourModel' has fields like 'field1', 'field2', etc.
    your_model_instance = Message(
        user_id=record['user_id'],  # Replace 'Column1' with the actual header in your CSV
        timestamp=record['timestamp'],
        message_body=record['message_body'],

        # Add other fields as needed
    )
    your_model_instance.save()

if __name__ == "__main__":
    csv_file_path = "listproject.csv"  # Replace with the actual path to your CSV file
    import_csv(csv_file_path)
