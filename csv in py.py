import csv 
fields=['Name','Branch','Year','CGPA']

row=[['Nikhil','CEO','2','9.0'],
     ['Prayag','CEO','2','9.1'],
     ['Aditya','IT','2','9.3'],
     ['Sagar','SE','1','9.5'],
     ['Prateek','MCE','3','7.8'],
     ['Sahil','EP','2','9.1']]

with open("data3.csv","w") as csvwriter:
    write=csv.writer(csvwriter)
    write.writerow(fields)
    write.writerows(row)