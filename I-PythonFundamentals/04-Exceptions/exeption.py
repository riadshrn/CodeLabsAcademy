a = 12
s = "Hello"
try:
	print("inside try")
	print(a + s) # will raise TypeError
	print("Printed using original data types")
except TypeError: # will handle only TypeError
	print("inside except")
	print(str(a) + s)
	print("Printed using type-casted data types")

except NameError as N_err:
	print(N_err)
	print("NameError occurred. Some variable isn't defined.")

except MemoryError as M_err :
	print(M_err)
	print("MemoryError occurred. Some variable are big.")