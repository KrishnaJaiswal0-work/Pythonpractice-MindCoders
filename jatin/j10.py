import csv
import numpy as np 

with open ("jatin/new.csv)","r") as f :
    reader = csv.reader(f)

with open ("jatin/new.csv","w") as f : 
    writer = csv.writer(f)
    writer.writerow("student","marks_1","marks_2","marks_3")

