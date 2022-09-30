stack=[ ]
def view( ):
  for x in range(len(stack)):
    print(stack[x])
def push( ):
  item=int(input("Enter integer value"))
  stack.append(item)
def pop( ):
 if(stack= =[ ]):
     print("Stack is empty")
else:
item=stack.pop(-1)
print("Deleted element:",item)
def peek( ):
item=stack[-1]
print("Peeked element:",item)
print("Stack operation")
print("************")
 print("1.view")
print("2.push")
print("3.pop")
print("4.peek)
while True:
choice=int(input("Enter your choice"))if
choice= =1:
view( )
elif choice= =2:
push( )
elif choice==3:
pop( )
elif choice= =4:
peek( )
else:
print("Wrong choice")
break