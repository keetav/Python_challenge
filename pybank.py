import csv
row_count=0
total_sum=0
with open(":Resources/budget_data)
    reader=csv.reader(mydata)
    header=next(reader)
    # print(header)

for row in reader:
    row_count+1 #row_count = row_count +1
    total_sum+=int(row[])

print(total_sum)
    monthly_change=int(row[1])-last_month_value 
    total_change += monthly_change
    largest_increase=max(largest_increase,increase,monthly_change)

    row_count+=1 #row_count

