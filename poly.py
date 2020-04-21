from math import sqrt
import os

print("Welcome in the Polynoms solver :)")
game = input("Do you want to use it? ")

while game == "yes":
    print("First of all, enter the polynom's constants with a,b,c such as ax²+bx+c=0")
    a=int(input("enter a : "))
    b=int(input("enter b : "))
    c=int(input("enter c : "))
    print("the polynom you chose is: P(x) = "+str(a)+"x²+"+str(b)+"x+"+str(c))
    delta=b*b-4*a*c
    print("disciminant is equals to : "+ str(delta))
    if delta > 0:
        print("There are two real solutions : r1=" + str((-b-sqrt(delta))/2*a)+" et r2="+str((-b+sqrt(delta))/2*a))
    elif delta < 0:
        print("There are two complex solutions : r1=" + str(-b/2*a)+"+i"+str(sqrt(-delta)/2*a)+"et r2="+str(-b/2*a)+"-i"+str(sqrt(-delta)/2*a))
    else:
        print("There is only one real solution : r=" + str(-b/2*a))
    game=input("Do you want to solve an other equation?  ")

os.system('Pause')
