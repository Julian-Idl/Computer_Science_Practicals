#stack implementation using functions
#program to create a stack of employee(empno,name,sal).
def line():
 print('~'*75)
employee=[]
def push():
 empno=input("Enter empno ")
 name=input("Enter name ")
 sal=input("Enter sal ")
 emp=(empno,name,sal)
 employee.append(emp)
def pop():
 if(employee==[]):
     print("Underflow / Employee Stack in empty")
 else:
    empno,name,sal=employee.pop()
    print("poped element is ")
    print("empno ",empno," name ",name," salary ",sal)
def traverse():
 if not (employee==[]):
    n=len(employee)
    for i in range(n-1,-1,-1):
        print(employee[i])
 else:
    print("Empty , No employee to display")
while True:
 line()
 print("1. Push")
 print("2. Pop")
 print("3. Traversal")
 print("4. Exit")
 ch=int(input("Enter your choice "))
 if(ch==1):
    push()
 elif(ch==2):
    pop()
 elif(ch==3):
    traverse()
 elif(ch==4):
    print("End")
    break
 else:
    print("Invalid choice")
