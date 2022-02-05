import numpy as np
from numpy.linalg import norm
import cv2
from matplotlib import pyplot as plt
from os import system,name


img = cv2.imread('digiTech.jpg')
print(img.shape)

plt.imshow(cv2.cvtColor(img, 3))
plt.show()



shape = int(input("-->Please Enter the shape of your matrix: "))
matrix = np.zeros((shape,shape))



for i in range (shape):
        for j in range (shape):
            matrix[i,j] = int(input("T[%d,%d]= "%(i,j)))
        print("\n")

system('cls')

print ("The matrix is : \n",matrix)

def LowerTriangular(matrix,shape):
    for i in range (shape):
        for j in range (i+1,shape):
            if(matrix[i,i])==0 or matrix[i,j]!=0:
                return False
    return True


def UpperTriangular(matrix,shape):
    return LowerTriangular(matrix.T,shape)

def DiagonalMatrix(matrix,shape):
    return (UpperTriangular(matrix,shape) and LowerTriangular(matrix,shape))

if (LowerTriangular(matrix,shape)): print("\n\t\t[The matrix is a Lower Triangular Matrix ]")
else: print("\n\t\t[The matrix is not a Lower Triangular Matrix ]")  

if (UpperTriangular(matrix,shape)): print("\n\t\t[The matrix is a Upper Triangular Matrix ]")
else: print("\n\t\t[The matrix is not a Upper Triangular Matrix ]")  


if (DiagonalMatrix(matrix,shape)): print("\n\t\t[The matrix is a Diagonal Matrix ]")
else: print("\n\t\t[The matrix is not a Diagonal Matrix ]")  


column = int(input("-->Please choice a column from 1 to %d  : "%(shape)))
print("\tThe column chocen is",matrix.T[column-1])


print("--> The norm 1 of the vector is : %d"%(norm(matrix.T[column-1],1)))
print("--> The norm 2 of the vector is : %f"%(norm(matrix.T[column-1])))