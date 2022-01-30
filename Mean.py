import csv
with open("SOCR.csv",newline="")as f:
    reader=csv.reader(f)
    file_data=list(reader)

file_data.pop(0)
new_data=[]
total_weight=0

for Person in (file_data):
    total_weight+=float(Person[2])
   
    
sum=0
n=len(file_data)



    
print("mean =",total_weight/n)



