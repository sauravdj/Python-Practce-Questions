def main():
    print("Hello! \nWelcome to our program.") #Start with a welcome message
    print()
    print("To be able to use this software you must be at least 21 years old and younger than 99")
    userAge = getAge()
    user = getAge2()
    age = ageRange(user,21,99)
    print(age)

#==============================================

def getAge():
    incorrectValue=True
    while(incorrectValue):
        try:
            result=int(input("Please enter your age: "))
            if (result > 21 and result < 99):
                incorrectValue=False
                return result
            else :
                print(result,"is not is range 21 to 99")
                
        except:
            print("Invalid value entered, please enter a valid value")
    

#=================================================
def getAge2():
    incorrectValue=True
    while(incorrectValue):
        try:
            result=int(input("ENTER IN 2 : "))
            incorrectValue=False
        except:
            print("Invalid value entered, please enter a valid value")
    return result
# ==============================================
def ageRange(value,low,high):
    while (value<low or value>high):
        print("Invalid range...value must be between "+str(low)+" and "+str(high))
        value = getAge2()
    return value    


main()