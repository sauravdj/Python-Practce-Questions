 
from breezypythongui import EasyFrame
 
class TaxCalculator(EasyFrame):
    """Application window for the tax calculator."""
 
    def __init__(self):
        """Sets up the window and the widgets."""
        EasyFrame.__init__(self, title = "Tax Calculator")
 
        # Label and field for the income
        self.addLabel(text = "Income",
                     row = 0, column = 0)
        self.incomeField = self.addFloatField(value = 0.0,
                                             row = 0,
                                             column = 1)
 
        # Label and field for the number of dependents
        self.addLabel(text = "Dependents",
                      row = 1, column = 0)
        self.depField = self.addIntegerField(value = 0,
                                             row = 1,
                                             column = 1)
 
        # Radio buttons for filing status
        self.statusGroup = self.addRadiobuttonGroup(row = 0, column = 2, 
                                                    rowspan = 3)
        self.single = self.statusGroup.addRadiobutton(text = "Single")
        self.married = self.statusGroup.addRadiobutton(text = "Married")
        self.divorced = self.statusGroup.addRadiobutton(text = "Divorced")
        self.statusGroup.setSelectedButton(self.single)
 
        # The command button
        self.addButton(text = "Compute", row = 2, column = 0,
                      columnspan = 2,
                      command = self.computeTax)
 
        # Label and field for the tax
        self.addLabel(text = "Total tax",
                     row = 3, column = 0)
        self.taxField = self.addFloatField(value = 0.0,
                                          row = 3,
                                          column = 1,
                                          precision = 2,
                                          state = "readonly")
 
# The event handler method for the button
    def computeTax(self):
        """Obtains the data from the input field and uses them to compute the tax, which is sent to the     output field."""
        rate = 0
        status = self.statusGroup.getSelectedButton()
        if status == self.single:
            rate = .20
        elif status == self.married:
            rate = .15
        elif status == self.divorced:
            rate = .10
        income = self.incomeField.getNumber()
        numDependents = self.depField.getNumber()
        exemptionAmount = 3000.0
        standardDeduction = 10000.0
        tax = (income - numDependents * exemptionAmount - standardDeduction) * rate
        self.taxField.setNumber(max(tax, 0))
 
def main():
    TaxCalculator().mainloop()
 
if __name__ == "__main__":
    main()
