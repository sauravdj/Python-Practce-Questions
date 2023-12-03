def main():
  #calls userMenu in main
  userMenu()
  #calls userInput in main
  
  #inputTest(firstNumber,secondNumber)
  #print('fn and sn are in main') #debug
  # uses while True statement to have a continuous loop until user enters a number < 6 which will stop the program
  while True:
   firstNumber,secondNumber,userCalc = userInput() 
   if userCalc == 1:
     answerAdd = add(firstNumber,secondNumber)
     print(firstNumber,'+',secondNumber,'=',userOutput())
   elif userCalc == 2:
    answerSub = subtract(firstNumber,secondNumber,userCalc)
   elif userCalc == 3:
    answerMult = multiply(firstNumber,secondNumber,userCalc)
   elif userCalc == 4:
    answerDiv = divide(firstNumber,secondNumber,userCalc)
   elif userCalc == 5:
    answerMod = modulo(firstNumber,secondNumber,userCalc)
   elif userCalc == 6:
    answerExp = exponent(firstNumber,secondNumber,userCalc)
   else:
     print('Program Quitting')
     break
  #calls userOutput in main
  userOutput(firstNumber,secondNumber, 
answerAdd,answerSub,answerMult,answerDiv,answerMod,answerExp,)
# Displays calculator choices
def userMenu():
  print("Select the action you'd like to take, by number:")
  print('1. Add')
  print('2. Subtract')
  print('3. Multiply')
  print('4. Divide')
  print('5. Modulo')
  print('6. Exponent')
  print('Any other number to exit the program')
#  Asks the user to select a menu option. If any menu item is selected, ask to enter two numbers
def userInput():
  userCalc = int(input('Enter the menu item you would like to run: '))
  #print('in userinput') # debug
  #asks user for input,accepts input as float
  firstNumber = float(input('Enter your first number: '))
  #asks user for input, accepts input as float
  secondNumber = float(input('Enter your second number: '))
  # returns variables to main function
  return firstNumber,secondNumber,userCalc
  #Accepts values from userInput(). Tests value to make sure it's a number. If it's not a number, it will ask for a valid number. Returns valid numbers.
#def inputTest(firstNumber,secondNumber):
  #print('in intputTest')
  #if type(firstNumber) == int() or type(firstNumber) == float():
    #print('int or float')
    #return int(firstNumber) or float(firstNumber)
  #elif type(secondNumber) == int() or type(secondNumber) == float():
    #return int(secondNumber) or float(secondNumber)
  #else:
    #print('please input a valid number')
#Accepts two numbers, returns the sum
def add(n1,n2):
  #print('in add') #debug
  answer = float(n1+n2)
  return answer
#Accepts two numbers, returns the difference of the first number minus the second number
def subtract(n1,n2):
  #print('in subtract') #debug
  answer = float(n1-n2)
  return answer
# Accepts two numbers, returns the product
def multiply(n1,n2):
  #print('in multiply') #debug
  answer = float(n1*n2)
  return answer
# Accepts two numbers, returns the quotient of the first number divided by the second number
def divide(n1,n2):
  #print('in divide') #debug
  # tries to solve n1/n2 except if n2 is zero, if n2 is zero it makes the calculation impossible and prints statement below except
  try:
    answer = float(n1/n2)
  except:
    answer = 'Divide by 0 Not Allowed'
  return answer
#Accepts two numbers, returns the modulo of the first number divided by the second number
def modulo(n1,n2):
  #print('in modulo')
  # tries to solve n1%n2 except if n2 is zero, if n2 is 0 it makes the calculation impossible and prints statement below except
  try:
    answer = float(n1%n2)
  except:
    answer = 'Divide by 0 Not Allowed'
  return answer
# Accepts two numbers, returns the first number raised to the power of the second number.
def exponent(n1,n2):
  #print('in exponent') #debug
  answer = float(n1**n2)
  #returns answer to main
  return answer
# this function shows a user friendly output of all calculations provided by this calculator, accepts passed variables like n1,n2 and all previous variables in main, plugs variables into print statement.
def userOutput(n1,n2,answerAdd,answerSub,answerMult,answerDiv,answerMod,answerExp,):
  #print('in userOutput')
  #print statements for all calculations 
   print(n1,'+',n2,'=',answerAdd)
   print(n1,'-',n2,'=',answerSub)
   print(n1,'*',n2,'=',answerMult)
   print(n1,'/',n2,'=',answerDiv)
   print(n1,'%',n2,'=',answerMod)
   print(n1,'**',n2,'=',answerExp)
