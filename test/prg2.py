#Read a text file and display the number of vowels/consonants/uppercase/lowercase characters in the file

print("Display the number of vowels/Consonants/Uppercase/Lowercase letters ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

f=open(".\output\output1.txt","r")
rd=f.read()

v=0
c=0
lc=0
uc=0

for ch in rd:
 if (ch.islower()):
    lc+=1
 elif(ch.isupper()):
    uc+=1

 ch=ch.lower()

 if( ch in ['a','e','i','o','u']):
    v+=1
 elif (ch in ['b','c','d','f','g',
 'h','j','k','l','m',
 'n','p','q','r','s',
 't','v','w','x','y','z']):
    c+=1
f.close()
print("Vowels are : ",v)
print("Consonants are : ",c)
print("Lower case letters are : ",lc)
print("Upper case letters are : ",uc)