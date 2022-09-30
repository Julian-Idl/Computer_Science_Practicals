# To remove all the lines that contain the character 'a'in a file & write it into another file
print( " Write the lines in the new file that contain the character 'a' ")
print( " ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")
f = open("./output/output2.txt","r")
f1 = open("./output/output3.txt","w")
l= f.readlines()
for i in l:
 if 'a' in i:
    f1.write(i)
f.close()
f1.close()
f1 = open("./output/output2.txt","r")
b = f1.read()
print(b)
f1.close()