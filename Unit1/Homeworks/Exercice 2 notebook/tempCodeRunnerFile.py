#generating 26 text files named A.txt, B.txt ...... Z.txt.
print("\n\n\t6. Generating 26 text files named A.txt, B.txt ...... Z.txt")
input("Press Enter to continue...")
for i in range(65,91):
    name = chr(i)+ '.txt'
    name = "./Unit1/Homeworks/Exercice 2 notebook/NewFile/" + name
    open(name, 'w')
print("\n\t\t[Files created successfully !!]")