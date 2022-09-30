#CSV file reader
from csv import reader
def prg():
 f=open("output/test.csv","r")
 d = reader(f,delimiter=",")
 r = next(d)
 e = list(d)
 f.close()
 for i in e:
    for j in i:
        print(j,"\t", end = " ")
    print()
# main
print(" CSV file reader")
print(" ~~~~~~~~~~~~~~~")
prg()