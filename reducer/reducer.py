import math
import sys

print ("Matrix Row Reducer Version 1")

row = input ("Rows: ")
column = input ("Columns ")
x = int(row)  # parse string into an integer
y = int(column)

matrixrows = [0] * y
matrix= [matrixrows] * x


def main ():
    counter = 0
    z = x
    print ("\nEnter your matrix in the following format:")
    
    for i in range(len(matrix)):
        print()
        for j in matrix[i]:
            print("%s "%j,end="")

    print("\n\nEnter your matrix: \n")

    while (z>0):
        line = input("")
        matrix [counter]= line 
        counter+=1
        z= z-1
    
    convert ()
    
def convert ():
  for i in range (len(matrix)):
        matrix[i] = list (matrix[i])
        
        while True:
              try:
                matrix[i].remove(' ')
              except ValueError:
                break 
            
        for n in range (len(matrix[i])):
            (matrix[i])[n] = float ((matrix[i])[n])
            
  reduce(matrix)
  print ("\nReduced Echelon Form:")
  for i in range(len(matrix)):
         print()
         for j in matrix[i]:
             print("%s "%j,end="")  
  
def reduce(M):
    if not M: return 
    count = 0
    rowvar = len(M)
    colvar = len(M[0])
    for r in range(rowvar):
        if count >= colvar:
            return
        i = r
        while M[i][count] == 0:
            i += 1
            if i == rowvar:
                i = r
                count += 1
                if colvar == count:
                    return
        M[i],M[r] = M[r],M[i]
        lv = M[r][count]
        M[r] = [ matrixvar / float(lv) for matrixvar in M[r]]
        for i in range(rowvar):
            if i != r:
                lv = M[i][count]
                M[i] = [ iv - lv*rv for rv,iv in zip(M[r],M[i])]
        count += 1
      
main()
  

