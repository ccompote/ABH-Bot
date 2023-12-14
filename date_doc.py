import os

def find_or_create_document(document_name):
    current_folder = os.getcwd()
    document_path = os.path.join(current_folder, document_name)

    if os.path.exists(document_path):
        open_document(document_path)
    else:
        create_and_open_document(document_path)

def open_document(document_path):
    os.system(f"open {document_path}")

def create_and_open_document(document_path):
    with open(document_path, 'w') as file:
        file.write("Hello, this is a new document!")

    os.system(f"open {document_path}")

document_name = "appointment.txt"

find_or_create_document(document_name)
