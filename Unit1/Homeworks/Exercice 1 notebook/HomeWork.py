even_numbers = []
#creation of the list of even numbers between 2 and 299
for i in range (2,300,2):
    even_numbers.append(i)
print("even_numbers = ",even_numbers)

#the length of the list
print("02-the length of the list is :",len(even_numbers))

#All the squared values of the list
for i in range (0,len(even_numbers)):
    print("  ",[i+1],"the squared of ",even_numbers[i],"is :",even_numbers[i]**2)

#checking if 57 is in the list 
print("03-The proposition (57 is in the list) is :",57 in even_numbers)


#if 57 in even_numbers : print("57 is in the list") 
#else : print("57 is not in the list")