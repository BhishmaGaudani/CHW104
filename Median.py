import csv
with open("SOCR.csv",newline="")as f:
    reader=csv.reader(f)
    file_data=list(reader)

file_data.pop(0)
new_data=[]
total_weight=0
sorted_data=[]
for Person in (file_data):
    total_weight+=float(Person[2])
    sorted_data.append(float(Person[2]))
    
sorted_data.sort()
n=len(sorted_data)

if n%2==0:
    median1=float(sorted_data[n//2])
    median2=float(sorted_data[n//2 -1])
    median=(median1+median2)/2
else:
    median=float(sorted_data[n//2])

print(median)
