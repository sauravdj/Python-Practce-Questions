def function1():
    count = 0
    total = 0
    # nums = int(input ("Enter number of to be added:  "))
    # while(count < nums) :
    #     a=int(input("Enter a number"))
    #     total=total+a
    #     count += 1
    # print(total)
    while True:
         a=int(input("Enter a number "))
         total=total+a 
         ch = input("Do you want to continue: ")
         if ch == "no":
            break
    print(total)

def function2():
    
    a=int(input("Enter a number "))
    b=int(input("Enter a number "))
    print(a-b)

def function3():
    a=int(input("Enter a number "))
    b=int(input("Enter a number "))
    print(a*b)

def function4():
    a=int(input("Enter a number "))
    b=int(input("Enter a number "))
    print(a/b)

while (True):

    choice=int(input("1. add \n2. sub \n3. mult \n4. division \n5. to escape "))
    if choice==1:
        function1()
    if choice==2:
        function2()
    if choice==3:
        function3()     
    if choice==4:
        function4()             
    if choice == 5:
        break    