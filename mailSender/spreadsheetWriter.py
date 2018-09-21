import csv
import shutil
import datetime
from tempfile import NamedTemporaryFile

"""
#Reference
with open("data.csv", "w+") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Col1", "Col 2"])
    writer.writerow(["Data 1", "Data 2"])


with open("data.csv", "a") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Data 3", "Data 4"])



with open("data.csv", "w+") as csvfile:
    fieldnames = ["id", "title"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"id": 123, "title": "New title"})

with open("data.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)
"""


def get_length(file_path):
    with open(file_path) as csvfile:
        reader = csv.reader(csvfile)
        reader_list = list(reader)
        print(reader_list)

    return len(reader_list)

def append_data(file_path, name, email, amount):
    fieldnames = ['id', 'name', 'email', 'amount', 'sent', 'date']
    next_id = get_length(file_path)
    with open(file_path, "a") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({
            "id": next_id,
            "name": name,
            "email": email,
            "amount": amount,
            "sent": "",
            "date":datetime.datetime.now(),

        })


#append_data("data.csv", "Torten", "polo@pat.com", 123.22)


def edit_data(edit_id=None, email=None, sent=None, amount=None):
    filename ="data.csv"
    temp_file = NamedTemporaryFile(delete=False)

    with open(filename, "r") as csvfile, open(temp_file.name, 'w', newline = '') as temp_file:
        reader = csv.DictReader(csvfile)
        fieldnames = ['id', 'name', 'email', 'amount', 'sent', 'date']
        writer = csv.DictWriter(temp_file, fieldnames=fieldnames)
        #writer.writeheader()
        #print(reader)
        #print(temp_file.name)
        for row in reader:
            #print(row)
            if edit_id is not None:
                if int(row['id']) == int(edit_id):
                    row['amount'] = amount
                    row['sent'] = sent
            elif email is not None and edit_id is None:
                if str(row['email']) == str(email):
                    row['amount'] = amount
                    row['sent'] = sent
            else:
                pass

            writer.writerow(row)

        shutil.move(temp_file.name, filename)
        return True
    return False


edit_data(email="polo@pat.com", sent="True", amount=77777)
