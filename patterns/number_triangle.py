# r = 5

"""

    1 
   1 2 
  1 2 3 
 1 2 3 4 
1 2 3 4 5 

"""

for r in range(6,0,-1):

    for sp in range(1,r):

        print(" ",end = "")

    for c in range(1,(6-r)+1):

        print(c,end=" ")

    print()


    

