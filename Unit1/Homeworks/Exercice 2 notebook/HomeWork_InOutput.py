import os

file = open("./Unit1/Homeworks/Exercice 2 notebook/inputs/student_names.txt")

#reading all of the content of the file in one variable
print("\n\n\t1. reading all of the content of the file in one variable")
input("Press Enter to continue...")
names = file.read()
names = names.split()
print("-->The content of the file (in a list) is: \n\t",names)
names=' '.join(names)
print("\n-->The content of the file (in a string) is: \n\t",names)





#Write a list of random names to the file
def f_random_names(file,nbr):  
    file = open("./Unit1/Homeworks/Exercice 2 notebook/inputs/student_names.txt", "r+")
    file.seek(0,os.SEEK_END)
    for i in range(nbr):
        name=str(input("\t-->please enter the name to write :"))
        file.write("\n"+name)
    print("\n\t\t[Names are written successfully !!]")

print("\n\n\t2. Write a list of random names to the file")
input("Press Enter to continue...")
nbr=int(input("-->please enter the number of names to write : "))
f_random_names("./Unit1/Homeworks/Exercice 2 notebook/inputs/student_names.txt",nbr)



#Read the first n lines of the file.
def ReadFirstLines(file,lines):
    sep=""
    with open(file) as Myfile:
        head = [next(Myfile) for x in range(lines)]
    head=sep.join(head)
    print(head)

print("\n\n\t3. Reading the first n lines of the file")
input("Press Enter to continue...")
N = int(input("-->please enter the number of the first line(s) you want to read here: "))
print(" =>The first",N,"line(s) of the file are:")
ReadFirstLines("./Unit1/Homeworks/Exercice 2 notebook/inputs/student_names.txt",N)



#Read the last n lines of the file.
def ReadLastLines(file,lines):
    sep=""
    with open(file) as Myfile:
        head = [next(Myfile) for x in range(lines)]
    head=sep.join(head)
    print(head)

#N = int(input("please enter the number of the last line(s) you want to read here: "))
#print(" =>The last",N,"line(s) of the file are:")
#ReadLastLines("./First_project/inputs/student_names.txt",N)



#Checking if the name is in the file.
print("\n\n\t5. Checking if the name is in the file")
input("Press Enter to continue...")
file = open("./Unit1/Homeworks/Exercice 2 notebook/inputs/student_names.txt")
name = str(input("-->please enter the name to check if it is in the file :"))
trouv = False
nbr=0
for line in file:
    nbr=nbr+1
    if name in line:
        trouv=True
        break
if (trouv==True): print("\n\t\t[The name %s is in the file in line n°%d]"%(name,nbr))
else: print("\n\t\t[The name %s is not in the file]"%(name))    


#generating 26 text files named A.txt, B.txt ...... Z.txt.
print("\n\n\t6. Generating 26 text files named A.txt, B.txt ...... Z.txt")
input("Press Enter to continue...")
for i in range(65,91):
    name = chr(i)+ '.txt'
    name = "./newFile/" + name
    open(name, 'w')
print("\n\t\t[Files created successfully !!]")