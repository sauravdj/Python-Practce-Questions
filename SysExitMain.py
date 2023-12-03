import sys
def getEmpName():
		EmpName = input("Enter employee name: ")
		return EmpName

def getHoursWorked():
				WorkedHours = float(input("Enter hours: "))
				return WorkedHours
		
def getHourlyRate():
				HourlyRate = float(input("Enter hourly rate: "))
				return HourlyRate

def getIncomeTaxRate():
				IncomeTaxRate = float(input("Enter tax rate: "))
				return IncomeTaxRate

def CalcTaxAndNetPay(WorkedHours, HourlyRate, IncomeTaxRate):
				GrossPay = WorkedHours * HourlyRate
				incomeTax = GrossPay * IncomeTaxRate
				netPay = GrossPay - incomeTax
				return GrossPay, incomeTax, netPay

	# def printinfo(EmpName, WorkedHours, HourlyRate, grossPay, IncomeTaxRate, incomeTax, netPay):
	# 		print(EmpName, f"{WorkedHours:, .2f}", f"{IncomeTaxRate:, .1%}", f"{incomeTax:, .2f}", f"{netPay:, .2f}")

def printtotals(totalEmployees, totalWorkedHours, totalGrossPay, totalincometax, totalnetpay):
				print(f'\n Total number of employees: {totalEmployees}')
				print (f'Total hours: {totalWorkedHours:.2f}')
				print(f'Total grosspay: {totalGrossPay:.2f}')
				print(f'Total tax: {totalincometax: .2f}')
				print(f'Total net pay: {totalnetpay:.2f}')
	
def main():

	totalEmployees = 0
	totalWorkedHours = 0.00
	totalGrossPay = 0.00	
	totalincometax = 0.00
	totalNetPay = 0.00			
				
	while True:
		EmpName = getEmpName()
		if EmpName.upper() == "END":
			print("Breaking..")
			break
		WorkedHours = getHoursWorked()
		HourlyRate = getHourlyRate()
		IncomeRate = getIncomeTaxRate()
		GrossPay, incomeTax, netPay = CalcTaxAndNetPay(WorkedHours, HourlyRate, IncomeRate)
		totalWorkedHours += WorkedHours
		totalGrossPay += GrossPay
		totalincometax += incomeTax
	printtotals(totalEmployees, totalWorkedHours, totalGrossPay, totalincometax, totalNetPay)	
	return 0			
if __name__ == "__main__":
	
		sys.exit(main())


				

			