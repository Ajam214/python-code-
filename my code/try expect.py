import keyword
from logging import exception


print("Enter a num1")
s = (input())
print("Ener a num2")
s2 = (input())

try:
    print("The sum of number these ",
    int(s) + int(s2))  

    
     
except Exception as e:
    print(e)    

print("this is a important")

#try is keyword  to use the skip program 