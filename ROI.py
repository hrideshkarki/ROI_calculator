
class ROI():
    def __init__(self):
        pass
    

    def income(self):
        print("Please enter your montly property incomes for following titles:")
        while True:
            rental = input("Rental: ").strip()
            if rental.isdigit():
                break
            else:
                print("Invalid input! Please enter a digit.")
                
        while True:    
            laundry = input("Laundry: ").strip()
            if laundry.isdigit():
                break
            else:
                print("Invalid input! Please enter a digit.")
                
        while True:
            storage = input("Storage: ").strip()
            if storage.isdigit():
                break
            else:
                print("Invalid input! Please enter a digit.")          
                
        while True:
            miscellaneous = input("Miscellaneous: ").strip()
            if miscellaneous.isdigit():
                break
            else:
                print("Invalid input! Please enter a digit.")

        total_income = int(rental) + int(laundry) + int(storage) + int(miscellaneous)

        print(f'Total monthly income from your property is ${total_income}.  ')
        return total_income
        
        
        
    def expenses(self):
        print("Please enter your monthly property expenses for following titles:")
        
        
        while True:
            tax = input("Tax: ").strip()
            if tax.isdigit():
                break
            else:
                print("Invalid input! Please enter a digit.")

                
        while True:
            insurance = input("Insurance: ").strip()
            if insurance.isdigit():
                break
            else:
                print("Invalid input! Please enter a digit.")
        
        print("Please enter your all your utilities expenses:")
        
        while True:
            electricity = input("Electricity: ").strip()
            if electricity.isdigit():
                break
            else:
                print("Invalid input! Please enter a digit.")
                
                
        while True:
            water = input("Water: ").strip()
            if water.isdigit():
                break
            else:
                print("Invalid input! Please enter a digit.")
                
        while True:
            sewer = input("Sewer: ").strip()
            if sewer.isdigit():
                break
            else:
                print("Invalid input! Please enter a digit.")
                
        while True:
            garbage = input("Garbage: ").strip()
            if garbage.isdigit():
                break
            else:
                print("Invalid input! Please enter a digit.")
                
        while True:
            gas = input("Gas: ").strip()
            if gas.isdigit():
                break
            else:
                print("Invalid input! Please enter a digit.")
        utilities = int(electricity) + int(water) + int(sewer) + int(garbage) + int(gas)
        
        
        while True:
            HOA = input("Home Owner Assocition Fee(HOA): ").strip()
            if HOA.isdigit():
                break
            else:
                print("Invalid input! Please enter a digit.")
                
        while True:
            lawn = input("Lawn/snow:").strip()
            if lawn.isdigit():
                break
            else:
                print("Invalid input! Please enter a digit.")
                
        while True:
            vacancy = input("Vacancy (Enter 0 if occupied)): ").strip()
            if vacancy.isdigit():
                break
            else:
                print("Invalid input! Please enter a digit.")
                
        while True:
            repairs = input("Repairs: ").strip()
            if repairs.isdigit():
                break
            else:
                print("Invalid input! Please enter a digit.")
                
        while True:
            capex = input("Capital Expenditure (Savings for things like roof for long term change): ").strip()
            if capex.isdigit():
                break
            else:
                print("Invalid input! Please enter a digit.")
                
        while True:
            management = input("Property management").strip()
            if management.isdigit():
                break
            else:
                print("Invalid input! Please enter a digit.")
                
        while True:
            mortgage = input("Mortgage: ").strip()
            if mortgage.isdigit():
                break
            else:
                print("Invalid input! Please enter a digit.")
        

        total_expenses = int(tax) + int(insurance) + (utilities) + int(HOA) + int(lawn) + int(vacancy) + int(repairs) + int(capex) + int(management) + int(mortgage)
        
        print(f'Total monthly expense for your property is ${total_expenses}.')
        return total_expenses
        
        
        
    def cash_flow(self):
        total_income = self.income()
        total_expenses = self.expenses()
        cash_flow = total_income + total_expenses
        print(f"Your total monthly cash flow of your property is ${cash_flow}.")
        return cash_flow
    
    def cash_on_cash_ROI(self):
        annual_cash_flow = self.cash_flow()
        
        while True:
            down_payment = input("How much did put on down payment: ")
            if down_payment.isdigit():
                break
            else:
                print("Invalid input! Please enter a digit.")
                
        while True:
            closing_cost = input("Enter your closing cost (Attorney/Appraisal etc. fees): ").strip()
            if closing_cost.isdigit():
                break
            else:
                print("Invalid input! Please enter a digit.")
        
        while True:
            rehab_budget = input("Mortgage: ").strip()
            if rehab_budget.isdigit():
                break
            else:
                print("Invalid input! Please enter a digit.")
                
        while True:
            misc = input("Miscellaneous/Others: ").strip()
            if misc.isdigit():
                break
            else:
                print("Invalid input! Please enter a digit.")
                
        total_investment = int(down_payment) + int(closing_cost) + int(rehab_budget) + int(misc)
        
        cash_on_cash_ROI = (annual_cash_flow/total_investment)*100
        
        
        return print(f'Your ROI is {cash_on_cash_ROI}%.')
         

roi_calculator = ROI()
roi_calculator.cash_on_cash_ROI()


