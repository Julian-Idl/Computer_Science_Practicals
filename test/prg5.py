# To read & Display file content line by line with each word separated by #
print ("DISPLAY FILE CONTENT LINE BY LINE WITH EACH WORD SEPARATED BY #")
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
a = open("./output/output1.txt","r")
l = a.readlines()
for line in l:
 x = line.split()
 for y in x:
    print(y+" # ",end = " ")
 print(" ")