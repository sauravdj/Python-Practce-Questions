#   Yvenet Marcelus
#   CIS261
#   Project Phase 2
class Emp():
        def __init__(self):
            self = dict()
        def GetName(self):
            empname = input("Enter employee name (END to terminate): ")
            return empname
        def GetDatesWorked(self):
            #write the code to input fromdate and todate and return the values from the function.  
            #Prompt the user for the dates in the following format: mm/dd/yyyy
            #no validations are needed for this input, we will assume the dates are entered correctly
            fromdate = input("Enter Start Date (mm/dd/yyyy): ")
            todate = input("Enter End Date (mm/dd/yyyy): ")
            return fromdate, todate
        
        def GetHoursWorked(self):
            hours = float(input('Enter amount of hours worked:  '))
            return hours
        def GetHourlyRate(self):
            hourlyrate = float(input ("Enter hourly rate: "))
            return hourlyrate
        def GetTaxRate(self):
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
        print(fromdate)
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
        hours["TotHours"] = TotHours
        grosspay["TotGrossPay"] = TotGrossPay
        incometax["TotTax"] = TotTax
        netpay["TotNetPay"] = TotNetPay
 
def PrintTotals(EmpTotals):    
    print()
    # use dictionary to print totals
    # the following line of code prints Total Employees from the dictionary
    print(f'Total Number Of Employees: {EmpTotals["TotEmp"]}')
    print(f'Total Hours Worked: {EmpTotals["TotHrs"]:,.2f}')
    # write code to print TotGrossPay, TotTax and TotNetPay from dictionary
    print(f'Total Gross Pay: {EmpTotals["TotGrossPay"]:,.2f}')
    print(f'Total Income Tax: {EmpTotals["TotTax"]:,.2f}')
    print(f'Total  Net Pay: {EmpTotals["TotNetPay"]:,.2f}')
 
 
 
if __name__ == "__main__":
 
    #create empty list and dictionary
    EmpDetailList = []
    EmpTotals = {}
    
    while True:
        e1 = Emp()
        empname = e1.GetName()
        if (empname.upper() == "END"):
            break
        fromdate, todate = e1.GetDatesWorked()
        hours = e1.GetHoursWorked()
        hourlyrate = e1.GetHourlyRate()
        taxrate = e1.GetTaxRate()
        #write code to insert fromdate, todate, empname, hours, hourlyrate, and taxrate into list EmpDetail
        EmpTotals.add(empname)
        EmpDetailList.append(e1.__dict__)

        # EmpDetail = EmpDetailList

        # if EmpDetail in range(len(EmpDetailList)):
        #     print(EmpDetailList)
            
        #the following code appends the list EmpDetail to the list EmpDetailList

print(EmpDetailList)
# printinfo(EmpDetailList)
# PrintTotals (EmpTotals)
 


