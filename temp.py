

# if __name__ == "__sumofmiddle__":
#     dataList = [2,4,6,8,10]
#     import sumofmiddle
#     #sl = sumMiddle(dataList)
#     #print(sl)
# a = 4
# b = "l"

# if (type(b)==int or float) and type(a)==str:
#     print("first int or float")

# firstNumber = 1
# secondNumber = 2 
# userCalc  = 3

# def fun(firstNumber, secondNumber,userCalc):
#  try:
#     firstNumber = int(firstNumber)
#  except:
#     print("firstNumber isn't insered correctly")   
# try:
#     secondNumber = int(secondNumber)
# except:
#     print("secondNumber isn't insered correctly") 
# try:
#     userCalc = int(userCalc)
# except:
#     print("userCalc isn't insered correctly")             
# a = fun(firstNumber, secondNumber,userCalc)
# print(a)    
def inputData(): #get input from the user to create a data byte
    dbyte = int(input("Enter integer"))
    list = []
    list=("{0:b}".format(int(dbyte)))
    return list
print(inputData())