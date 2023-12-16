import os
import json
from datetime import datetime
from shared_data import closest_appointment

def find_or_create_document(closest_appointment):
    current_folder = os.getcwd()
    document_path = os.path.join(current_folder, "appointment.txt")

    if os.path.exists(document_path) and os.stat(document_path).st_size != 0:
        existing_info = read_document(document_path)
        if compare_dates(existing_info, closest_appointment):
            print("Date is the same or later")
            return
    create_and_open_document(document_path, closest_appointment)
    print("Updated info")

def open_document(document_path):
    os.system(f"open {document_path}")

def create_and_open_document(document_path, closest_appointment):
    with open(document_path, 'w') as file:
        json.dump(closest_appointment, file, indent=2)

    os.system(f"open {document_path}")

def read_document(document_path):
    with open(document_path, 'r') as file:
        existing_info = json.load(file)
    return existing_info

def compare_dates(existing_info, new_info):
    existing_date = datetime.strptime(existing_info['month'] + ' ' + existing_info['day'] + ' ' + existing_info['time'], "%b %d %H:%M - %H:%M")
    new_date = datetime.strptime(new_info['month'] + ' ' + new_info['day'] + ' ' + new_info['time'], "%b %d %H:%M - %H:%M")
    return new_date > existing_date

