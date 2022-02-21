file = open("./I-PythonFundamentals/02-InputOutput/inputs/student_names.txt")

#Read the last n lines of the file.
names = file.read()
lines = names.splitlines()

N = int(input("please enter the number of the last line(s) you want to read here: "))

print(" =>The last",N,"line(s) of the file are:")
for i in (lines[-N:]):
    print(i)