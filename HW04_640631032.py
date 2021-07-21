# -*- coding: utf-8 -*-
"""

@author: Nattapat Tangniyom 640631032
"""
def sorte(x,y):
   z = x
   x = y
   y = z
   return x,y

#For example (input) : 50 2 1 9
a = list(input("Enter the numbers : ").split())
for i in range(len(a)):
    for x in range(len(a)-1):
        if len(a[x]) > len(a[x+1]):
            min = len(a[x+1])
        else:
            min = len(a[x])
        sort = False
        for y in range(min):
            if int(a[x][y]) > int(a[x+1][y]) and sort == False:
                a[x],a[x+1] = sorte(a[x],a[x+1])
                sort = True
            elif int(a[x][y]) < int(a[x+1][y]) and sort == False:
                sort = True
            else:
                if len(a[x]) < len(a[x+1]):
                    a[x],a[x+1] = sorte(a[x],a[x+1])
result = ""  
s = len(a)-1  
for j in range(s, 0, -1):
    result = result + a[j]
print(result)