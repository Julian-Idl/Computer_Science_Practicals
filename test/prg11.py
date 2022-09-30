#CSV file Writer1
from csv import writer
def prg():
 #Create Header

 f=open("output/test.csv","w",newline ="\n")
 d = writer(f)
 d.writerow(['StudentID','StudentName','Score'])
 f.close()
 #Insert data

 f=open("output/test.csv","a",newline ="\n")
 while True:
    st_id=int(input("Enter Student ID : "))
    st_name = input("Enter Student name : ")
    st_score = input("Enter Score :")
    d = writer(f)
    d.writerow([st_id,st_name,st_score])
    ch = input("Do you want to insert another record ? (y/n)")
    ch=ch.lower()
    if ch != "y":
        break
 print("\n Record has been added..")
 f.close()
#main
print("WRITE DATA INTO CSV FILE")
print("~~~~~~~~~~~~~~~~~~~~~~~~")

prg()