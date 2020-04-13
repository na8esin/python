import csv

with open('data.tsv', newline='', encoding="utf-8") as csvfile:
    spamreader = csv.reader(csvfile, delimiter='\t')
    day_counter=0
    sum=0
    for row in spamreader:
        hour   = int(row[5][0:2])
        minute = int(row[5][4:6])
        #print(hour)
        #print(minute)
        if hour == 0:
            continue
        sum += (hour-8)*60 + minute
        day_counter += 1
print(sum)
print(sum-(day_counter*30))