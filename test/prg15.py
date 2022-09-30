stack = []
top = -1

# push function
def push(ele: str):
 global top
 top += 1
 stack[top] = ele
 
# pop function
def pop():
 global top
 ele = stack[top]
 top -= 1
 return ele

def isPalindrome(string: str) -> bool:
 global stack
 length = len(string)
 stack = ['0'] * (length + 1)
 mid = length // 2
 i = 0
 while i < mid:
    push(string[i])
    i += 1
 if length % 2 != 0:
    i += 1
 while i < length:
   ele = pop()
 if ele != string[i]:
    return False
 i += 1
 return True
if __name__ == "__main__":
 print ( " Palindrome ")
 print ( " ~~~~~~~~~~ ")
 string = input ("Enter the String :")
 if isPalindrome(string):
    print("The given string '",string,"' is a palindrome")
 else:
    print("The given string '",string,"'is not a palindrome")