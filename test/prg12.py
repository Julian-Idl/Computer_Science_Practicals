import csv

def prg():
 with open("./output/users.csv","a",newline="") as f:
    w=csv.writer(f,delimiter=",")
    while True:
        email=input("\nEnter emailID : ")
        password = input("Enter your password : ")
        password2 = input("Retype your password : ")
        if password==password2:
            w.writerow([email,password])
            print("\nData inserted")
        else:
            print("\nPlease try again...")
        ch=input("\nDo you want to enter more record( y/n) ?")
        if ch == 'n':
            break
def login():
 password=input("\nEnter password : ")
 with open("./output/users.csv","r") as f:
    r=csv.reader(f,delimiter=",")

    for i in r:
        if password == i[1]:
            print("\nEmail : ",i[0])
            print("Password : ",i[1])
            return True
    print("\nTry again!")
    return False
# Main
print("SEARCH RESULTS IN CSV FILE")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
while True:
 print("\n1.Insert Record")
 print("2.Search")
 print("3.Exit")
 ch = int(input("\nEnter the choice : "))
 if ch == 1:
    prg()
 elif ch == 2:
    login()
 elif ch == 3:
    break
 else:
    print("\nInvalid Choice..!")
    
    break
