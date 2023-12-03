#   Student Name 
#   CIS261 
#   Project Phase 2 
class EMP():
        def GetEmpName(): 
            empname = input("Enter employee name (END to terminate): ") 
            return empname 
        def GetDatesWorked(): 
            #write the code to input from date and todate and return the values from the function.   
            #Prompt the user for the dates in the following format: mm/dd/yyyy 
            #no validations are needed for this input, we will assume the dates are entered correctly 
            fromdate = input("Enter Start Date: ")
            todate = input("Enter End Date: ")
            return fromdate, todate
        def GetHoursWorked(): 
            hours = float(input('Enter amount of hours worked:  ')) 
            return hours 
        def GetHourlyRate(): 
            hourlyrate = float(input ("Enter hourly rate: ")) 
            return hourlyrate 
        def GetTaxRate(): 
            taxrate = float(input ("Enter tax rate: ")) 
            return taxrate 
        def CalcTaxAndNetPay(hours, hourlyrate, taxrate): 
            grosspay = hours * hourlyrate 
            incometax = grosspay * taxrate 
            netpay = grosspay - incometax 
            return grosspay, incometax, netpay 
  
def printinfo(EmpDetailList): 
    TotEmployees = 0 
    TotHours = 0.00 
    TotGrossPay = 0.00 
    TotTax = 0.00 
    TotNetPay = 0.00 
    # the following code creates a for loop to read through EmpDetailList and assign values in list to variables 
    for EmpList in EmpDetailList: 
        fromdate = EmpList[0] 
        #write code to assign values to todate, empname, hours, hourlyrate, and taxrate from EmpLst 
  
  
  
  
        grosspay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyrate, taxrate) 
        print() 
        print("Name:  ", empname) 
        print("From Date:  ", fromdate) 
        print("To Date:  ", todate) 
        print("Hours Worked: ", f"{hours:,.2f}") 
        print("Hourly Rate: ",  f"{hourlyrate:,.2f}") 
        print("Gross Pay : ",f"{grosspay:,.2f}") 
        print("Tax Rate: ", f"{taxrate:,.1%}") 
        print("Income Tax: ",  f"{incometax:,.2f}") 
        print("Net Pay: ",  f"{netpay:,.2f}") 
        print()         
        TotEmployees += 1 
        TotHours += hours 
        TotGrossPay += grosspay 
        TotTax += incometax 
        TotNetPay += netpay 
        # the following line of code assigns TotEmployees totals to dictionary  
        EmpTotals["TotEmp"] = TotEmployees 
        # write code to assign TotHours, TotGrossPay, TotTax, and TotNetPay to corresponding dictionary item 
  
def PrintTotals(EmpTotals):     
    print() 
    # use dictionary to print totals 
    # the following line of code prints Total Employees from the dictionary 
    print(f'Total Number Of Employees: {EmpTotals["TotEmp"]}') 
    print(f'Total Hours Worked: {EmpTotals["TotHrs"]:,.2f}') 
    # write code to print TotGrossPay, TotTax and TotNetPay from dictionary 
     
  
  
  
if __name__ == "__main__": 
  
    #create empty list and dictionary 
    EmpDetailList = [] 
    EmpTotals = {} 
    while True: 
        empname = GetEmpName() 
        if (empname.upper() == "END"): 
            break 
        fromdate, todate = GetDatesWorked() 
        hours = GetHoursWorked() 
        hourlyrate = GetHourlyRate() 
        taxrate = GetTaxRate() 
        #write code to insert fromdate, todate, empname, hours, hourlyrate, and taxrate into list EmpDetail 
        
  
        #the following code appends the list EmpDetail to the list EmpDetailList 
        EmpDetailList.append(EmpDetail) 
  
    printinfo(EmpDetailList) 
    PrintTotals (EmpTotals) 
  
 
 

