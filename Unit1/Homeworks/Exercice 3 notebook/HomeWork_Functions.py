
#Checking whether a passed string is palindrome or not 
def Palindrom(phrase):
    Inf = 0
    phrase=phrase.replace(" ","")
    phrase=phrase.upper()
    Sup = len(phrase) - 1
    while Inf <= Sup :
        if not phrase[Inf] == phrase[Sup]: return False
        Inf += 1
        Sup -= 1
    return True

print ("\t1. Checking whether a passed string is palindrome or not :")
input("Press Enter to continue...")
phrase = str(input("-->Please Enter your string: "))
if Palindrom(phrase): print ("\n\t\t[The string '%s' is a palindrome]"%(phrase))
else : print ("\n\t\t[The string '%s' is note a palindrome]"%(phrase))

#Checking if the number is prime or not
def Prime(number):
    for i in range(2,number):
        if (number % i) ==0 :
            return False
            break
    return True

print ("\n\t2. Checking if the number is prime or not :")
input("Press Enter to continue...")
number = int(input("-->Please Enter the number: "))
if Prime(number): print ("\n\t\t[The number '%d' is a prime]"%(number))
else : print ("\n\t\t[The number '%d' is not a prime]"%(number))
    

#Checking whether a number is in a given range
def number_in(num,inf,sup):
    if (num>=inf and num<=sup): return True
    else: return False

print ("\n\t3. Checking whether a number is in a given range :")
input("Press Enter to continue...")
number = int(input("-->Please Enter the number: "))
Inf = int(input("-->Please Enter the Lower bound: "))
Sup = int(input("-->Please Enter the Upper bound: "))
if number_in(number,Inf,Sup): print ("\n\t\t[The number '%d' is in the range [%d,%d] ]"%(number,Inf,Sup))
else : print ("\n\t\t[The number '%d' is not in the range [%d,%d] ]"%(number,Inf,Sup))

#Calculate the factorial of a number
def facto(number):
    x=1
    if number < 0:
        print("\n\t\t[Factorial does not exist for negative numbers]")
    elif number == 0:
        print("\n\t\t[The factorial of '0' is '1' : 0! = 1 ]")
    else:
        for i in range(1,number + 1):
            x = x*i
        return x

print ("\n\t4. Calculate the factorial of a number :")
input("Press Enter to continue...")
number = int(input("-->Please Enter the number: "))
if number>0: print ("\n\t\t[The factorial of '%d' is '%d']"%(number,facto(number)))
else: facto(number)


#reverse a string
def reverse(phrase):
    return phrase[len(phrase): :-1]   #x[start:end:step] slice

print ("\n\t5. reverse a string :")
input("Press Enter to continue...")
phrase = str(input("-->Please Enter the string : "))
print ("\n\t\t[The reverse of '%s' is '%s']"%(phrase,reverse(phrase)))


#sum all the numbers in a list
def sum_list(list):
    sum=0
    for i in range(len(list)):
        sum += list[i]
    return sum

list = []
print ("\n\t6. Sum all the numbers in a list :")
input("Press Enter to continue...")
lenght = int(input("-->Please Enter the lenght of the list : "))
for i in range(lenght):
    num = int(input("-->Please Enter the number n°%d : "%(i+1)))
    list.append(num)
print ("\n\t\tThe list : ",list)
print ("\t\t[The sum of all the number in the list is '%d']"%(sum_list(list)))


#Find the Max of three numbers
def max_3numbers(num1,num2,num3):
    if (num1-num2)<0 : 
        if (num2-num3)>0 : return num2
    else: 
        if(num1-num3)>0 :return num1
        else: return num3

print ("\n\t7. Find the Max of three numbers :")
input("Press Enter to continue...")
num1 = int(input("-->Please Enter the number n°1: "))
num2 = int(input("-->Please Enter the number n°2: "))
num3 = int(input("-->Please Enter the number n°3: "))
print ("\n\t\t[The max of {%d,%d,%d} is '%d']"%(num1,num2,num3,max_3numbers(num1,num2,num3)))
