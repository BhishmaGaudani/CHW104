from collections import Counter
import csv

with open('SOCR.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)
total_weight=0
sorted_data=[]


for Person in (file_data):
    total_weight+=float(Person[2])
    sorted_data.append(float(Person[2]))



#Calculating Mode
data = Counter(sorted_data)
mode_data_for_range = {
                        "100-110": 0,
                        "110-120": 0,
                        "120-130": 0,
                        "130-140": 0,
                        "140-150": 0,
                        "150-160": 0,
                        "160-170": 0,
                        "170-180": 0,
                        
                    }
for weight, occurence in data.items():
    if 100 < float(weight) < 110:
        mode_data_for_range["100-110"] += occurence
    elif 110 < float(weight) < 120:
        mode_data_for_range["110-120"] += occurence
    elif 120 < float(weight) < 130:
        mode_data_for_range["120-130"] += occurence
    elif 130 < float(weight) < 140:
        mode_data_for_range["130-140"] += occurence
    elif 140 < float(weight) < 150:
        mode_data_for_range["140-150"] += occurence
    elif 150 < float(weight) < 160:
        mode_data_for_range["150-160"] += occurence
    elif 160 < float(weight) < 170:
        mode_data_for_range["160-170"] += occurence
    elif 170 < float(weight) < 180:
        mode_data_for_range["170-180"] += occurence

mode_range, mode_occurence = 0, 0
for range, occurence in mode_data_for_range.items():
    if occurence > mode_occurence:
        mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence
mode = float((mode_range[0] + mode_range[1]) / 2)
print(f"Mode is -> {mode:2f}")


