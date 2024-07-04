import csv
import random
with open('placement.csv','w',newline='') as f:
    w=csv.writer(f)
    w.writerow(['cgpa','iq','placed'])
    i=0
    while i < 100:
        cgpa=round(random.uniform(1,10),2)
        iq=round(random.uniform(1,10),2)
        if cgpa > 6 :
            placed=1
        else:
            placed=0
        w.writerow([cgpa,iq,placed])
        i+=1