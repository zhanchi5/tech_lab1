#tech_lab1


file1 = open('C:\\Users\\DELL\\Documents\\Visual Studio 2015\\Projects\\tech_lab1\\file1.txt','r')
file2 = open('C:\\Users\\DELL\\Documents\Visual Studio 2015\\Projects\\tech_lab1\\file2.txt','r')


lines1 = []
lines2 = []


for line in file1:
    lines1.append(line)

for line in file2:
    lines2.append(line)

print("flie1:")
for element in lines1:
    if not element in lines2:
        print (element, end="")

print("\n\nfile2:")
for element in lines2:
    if not element in lines1:
        print(element, end="")
file1.close()
file2.close()
