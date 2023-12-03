def menu():
 while True:
    ch = (input("Enter a b or c "))
    if(ch == "a"):
        print("1")
    elif(ch == "b"):
        print("2") 
    elif(ch == "c"):
        print("Quitting loop")
        break       
    else:
        print("enter a/b/c")    
menu()        