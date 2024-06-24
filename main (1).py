from datetime import datetime

def read_date_pairs_from_file(file_path):
    date_pairs = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.strip() and ',' in line:
                date1_str, date2_str = line.strip().split(',')
                date_pairs.append((date1_str.strip(), date2_str.strip()))
    return date_pairs

def calculate_date_difference(date1_str, date2_str):
    date_format = "%m/%d/%Y"

    date1 = datetime.strptime(date1_str, date_format)
    date2 = datetime.strptime(date2_str, date_format)

    date_difference = abs((date2 - date1).days)

    return date_difference

file_path = 'dates.txt' 
date_pairs = read_date_pairs_from_file(file_path)

    for date1, date2 in date_pairs:
        difference = calculate_date_difference(date1, date2)
        print(f" {difference} ")
