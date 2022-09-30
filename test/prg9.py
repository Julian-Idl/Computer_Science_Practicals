# Create a binary file with roll number, name and marks , input a roll number and
#update the marks.
import pickle
def write():
 f= open("Birec.dat","wb")
 record=[]
 while True:
    rno = int(input("\nEnter roll no : "))
    name = input("Enter name : ")
    marks = int(input("Enter marks : "))
    data=[rno,name,marks]
    record.append(data)
    ch=input("\nDo you want to enter more record?( y/n)")
    if ch == 'n':
        break
 pickle.dump(record,f)
def read():
 f = open("Birec.dat","rb")
 s= pickle.load(f)
 print("Roll no\t\tName\t\tMarks")
 print("~~~~~~~\t\t~~~~\t\t~~~~~\n")
 for i in s:
    rno=i[0]
    name=i[1]
    marks=i[2]
    print(rno,"\t\t",name,"\t\t",marks)
def search():
 f=open("Birec.dat","rb")
 s=pickle.load(f)
 found = 0
 rno = int(input("\nEnter roll no : \n"))
 for i in s:
    if i[0] == rno:
        print("Record found ....\n")
        print("Roll No = ",i[0])
        print("Name = ", i[1])
        print("Marks = ", i[2])
        found = 1
 if found == 0:
        print("\nRecord not found.....")
def update():
 f=open("Birec.dat","rb+")
 s=pickle.load(f)
 final=0
 n=int(input("Enter Roll.No : "))
 for i in s:
    if n ==i[0]:
        print("Current Marks : ",i[2])
        i[2] = int(input("Enter new marks : "))
        print("\n Marks updated successfully...")
        final=1
        break
 if final == 0:
    print("No records found")
 else:
    f.seek(0)
    pickle.dump(s,f)
    print(s)
 f.close()
#main
print("WRITE, READ AND SEARCH RECORD IN A BINARY FILE")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
while True:
 print("\n1.Write a Record")
 print("2.Display")
 print("3.Search")
 print("4.Update")
 print("5.Exit")
 ch = int(input("\nEnter the choice : "))
 if ch == 1:
    write()
 elif ch == 2:
    read()
 elif ch == 3:
    search()
 elif ch == 4:
    update()
 elif ch == 5:
    break
 else:
    print("\nInvalid Choice..!")
    break
