import csv

def get_CSV_Data(fileName):
    rows = []
    try:
        with open(fileName, "r") as dataFile:
            reader = csv.reader(dataFile)
            next(reader)  # Skip header, if there is one
            for row in reader:
                rows.append(row)
    except Exception as e:
        print(f"Error reading file: {e}")
    return rows
