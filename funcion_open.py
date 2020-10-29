myfile = "group1.txt"
myfile1 = "group2.txt"
myfile = open(myfile, mode="a+")
myfile1 = open(myfile1, mode="a+")   
myfile.write("Artem, 24")
myfile1.write("Petro, 24")
print(myfile.read())
import glob
for filename in glob.glob("..\\group1\\*.txt"):     
    print(filename) 
for filename in glob.glob("..\\group2\\*.txt"):     
    print(filename) 
line = myfile1.readline()
while line:
    print (line),
    line = myfile.readline()
    def numeric_compare(x, y):
        return x - y
    sorted([5, 2, 4, 1, 3], cmp=numeric_compare)
[1, 2, 3, 4, 5]
myfile.close()

