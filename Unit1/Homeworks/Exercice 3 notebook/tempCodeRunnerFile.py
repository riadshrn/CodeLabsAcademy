#Checking if the number is prime or not
def Prime(number):
    if number == 0 or number == 1: return False
    else :
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