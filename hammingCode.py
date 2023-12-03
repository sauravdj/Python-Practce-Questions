
# Online Python - IDE, Editor, Compiler, Interpreter

#Hamming code utility module
#complete all the function stubs. You can add other functions if you wish,
# but they will not be tested or graded separately from the functions
# already in this template. You may NOT change the names, parameters,
# parameter types, or return types of any of these functions.
#A data byte will be represented as a list of 8 integers, each integer will beeither 1 or 0
#A Hamming code will be represented as a list of 12 integers, each integer will be either 1 or 0
#NOTE: Be aware that the bits of Hamming codes are numbered two ways, by their
# position in the list (0-11) and by their Hamming position (1-12). Make sure you
# know which you are suppposed to be using in each situation
##debugging and other useful functions
def inputData(): #get input from the user to create a data byte
    dbyte = int(input("Enter integer"))
    list = []
    while(dbyte<0):
        temp = dbyte % 2
        dbyte = dbyte / 2
        list.append(temp)
    return list
    
def inputHamming(): #get input from the user to create a Hamming code
    return [0,0,0,0,0,0,0,0,0,0,0,0]
def dataToString(d8): #d8 example: [0,0,0,0,0,0,0,0]
    return "00000000"
def HammingToString(HC): #HC example: [0,0,0,0,0,0,0,0,0,0,0,0]
    return "000000000000"
def printData(d8): #d8 example: [0,0,0,0,0,0,0,0]
    return #no return value; the 8 digits of d8 are printed with no other characters, no blanks, no newline ...
def printHamming(HC): #HC example: [0,0,0,0,0,0,0,0,0,0,0,0]
    return #no return value; the 12 digits of HC are printed with no other characters, no blanks, no newline ...
##important Hamming functions
def dataToHamming(d8):#d8 example: [0,0,0,0,0,0,0,0]
    return [0,0,0,0,0,0,0,0,0,0,0,0] #The Hamming code corresponding to d8
def HammingToData(HC):#HC example: [0,0,0,0,0,0,0,0,0,0,0,0]
    return [0,0,0,0,0,0,0,0] #The data byte corresponding to HC
def isHammingCorrect(HC):#HC example: [0,0,0,0,0,0,0,0,0,0,0,0]
    return True #True if HC is a valid Hamming code and False if it is not
def checkHammingGroups(HC):#HC example: [0,0,0,0,0,0,0,0,0,0,0,0]
    return [1,2] #The return value is a list containing all the parity bits that show an error -
# [1,2] would mean that parity groups 1 and 2 each had an odd number of 1's but that
# groups 4 and 8 were correct.
#If the Hamming code is correct, the return value would be []
def makeCorrectedHamming(HC):#HC example: [0,0,0,0,0,0,0,0,0,0,0,0]
 return [0,0,0,0,0,0,0,0,0,0,0,0] #If HC can be corrected by changing one of its bits, the return value is
# the corrected Hamming Code.
# If HC is already a vaild code or if there are more errors
# than can be corrected with a 1-bit change, the return value is the same
# as the original HC
if __name__ == "__main__":
#Here is a sample driver, add to it or replace it as you need
    dByte = inputData()
    print("testing inputData",dByte)
    HCIn = inputHamming()
    print("testing inputHamming",HCIn)
    dString = dataToString(dByte)
    print("testing dataToString",dString)
    HString = HammingToString(HCIn)
    print("testing HammingToString",HString)
    print(".",end='')
    printData(dByte)
    print(".")