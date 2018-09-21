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
    with open("data.csv") as csvfile:
        reader = csv.reader(csvfile)
        reader_list = list(reader)
        print(reader_list)

    return len(reader_list)

def append_data(file_path, name, email):
    fieldnames = ['id', 'name', 'email']
    next_id = get_length(file_path)
    with open(file_path, "a") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        #writer.writeheader()
        writer.writerow({
            "id" : next_id,
            "name": name,
            "email": email,
        })


#append_data("data.csv", "Torten", "polo@pat.com")


filename ="data.csv"
temp_file = NamedTemporaryFile(delete=False)


with open(filename, "rt") as csvfile, temp_file:
    reader = csv.DictReader(csvfile)

    fieldnames = ['id', 'name', 'email', 'amount', 'sent', 'date']
    writer = csv.DictWriter(temp_file, fieldnames=fieldnames)

    #writer.writeheader()
    print(reader)
    print(temp_file.name)
    for row in reader:
        if row['id'] == 4:
            writer.writerow({
                "id": row["id"],
                "name": row["name"],
                "email": row["email"],
                "amount": "1293.23".encode(),
                "sent": "True",
                "date": datetime.datetime.now(),
            })


    shutil.move(temp_file.name, filename)