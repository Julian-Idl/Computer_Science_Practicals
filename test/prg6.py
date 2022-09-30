# To input n numbers in tuple & count how many even & odd numbers are entered
def fun(t):
 e=0
 o=0
 for i in range(0,len(t)):
    if t[i] % 2 == 0:
        e+=1
    else:
        o+=1
 print("\nNumber of even numbers : ",e,"\nNumber of odd numbers : ",o)
#main
print("COUNT & DISPLAY EVEN & ODD NUMBERS")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
x=eval(input("\nEnter a tuple : "))
fun(x)
