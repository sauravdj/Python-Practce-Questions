import math
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
c = int(input("Enter value of c: "))
print("Equation is: ")
print(f"{a}x^2 + ({b})x + ({c})")
d = b**2 - 4 * a *c

if (d > 0):
    print("Equation have two positive roots ")
    x1 = (-(b) + math.sqrt(d) )/2*a
    x2 = (-(b) - math.sqrt(d) )/2*a
    print(f"first root is {x1:,.2f} and second root is {x2:,.2f}")
elif(d==0):
    print("Equation have only one real root ") 
    x1 = (-(b) + math.sqrt(d) )/2*a  
    print(f"Root of the equation is {x1:,.2f}") 
else:
    print("No real roots")    