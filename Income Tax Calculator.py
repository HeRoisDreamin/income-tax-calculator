# Note: This python program was made according to the rules and regulations of the Indian Income Tax Department 2022.

print("Welcome To Personal Income Tax Calculator. Made by ABHIMANYU MISHRA & HARSHIT RAJ")

print("[NOTE: Please type only numbers]")

x = int(input("ENTER YOUR TOTAL INCOME : "))
y = int(input("ENTER YOUR ALLOWANCES IF ANY : "))
print("Now we are arrived here with your Net Salary : ")
z = x - y - 50000
print(z)
print(end='\n')

p = int(input("ENTER YOUR IONCOME FROM OTHER SOURCES: \n(This includes Interest, Rental Income, Interest Earned, Capital Gains, Winnings from Lottery, etc) \n:"))
print(end='\n')

c = int(input("ENTER YOUR DEDUCTIONS UNDER SECTION 80C: \n(This includes deductions up to Rs 1.5 Lakh on Public Provident Fund (PFF), Equity Linked Saving Scheme (ELSS), Employee Provident Fund (EPF), Sukanya Samriddhi Yojana (SSY), Premium Paid For Term Insurance, Repayment Towards Principal of Home Loan, etc. Also for tax payers who are investing in the NPS there is an additional tax up to Rs 50,000 deduction you can avail under Section 80CCD(1)B which is over and above Rs 1.5 Lakh rupees limit under Section 80 C) \n:"))
print(end='\n')

d = int(input("ENTER YOUR DEDUCTIONS UNDER SECTION 80D: \n(This includes Premium Paid For Medical Insurance. Section 80D limit depends on the age of the insured and the age of family members) \n:"))
print(end='\n')

t = int(input("ENTER YOUR DEDUCTIONS UNDER SECTION 80TTA: \n(This Includes deductions up to Rs. 10,000 on the interest earned from a savings account) \n:"))
print(end='\n')

e = int(input("DEDUCTIONS FOR EDUCATION LOAN: \n(If you have an education loan you can claim deduction on interest component paid) \n:"))
print(end='\n')

f = int(input("DEDUCTIONS FOR HOME LOAN: \n(If you have a Home Loan the interest portion of the EMI paid for the financial year can be claimed as a deduction upto a maximum of Rs 2 Lakh under Section 4) \n:"))
print(end='\n')

print("Now we have arrived at your Net Taxable Income: (This is your Gross Taxable Income - All eligible deductions)")
n = z + p - c - d - t - e - f
print(n)

print(end='\n')

a = int(input("ENTER YOUR AGE NUMBER: "))

if a < 60:
    if n < 250000:
        print("You don't have to pay Personal Income Tax.")
    elif n < 500000:
            n = (n - 250000)*(5/100)
            print("Your Personal Average Income Tax is: Rs", n)
    elif n < 1000000:
            n = (n - 500000)*(20/100)
            print("Your Personal Average Income Tax is: Rs", n)
    else:
            n = (n - 1000000)*(30/100)
            n = n + 112500
            print("Your Personal Average Income Tax is: Rs", n)
elif a < 79:
        if n < 300000:
            print("You don't have to pay Personal Income Tax")
            
        elif n < 500000:
            n = (n - 300000)*(5/100)
            print("Your Personal Average Income Tax is: Rs", n)
            
        elif n < 1000000:
            n = (n - 500000)*(20/100)
            n = n + 10000
            print("Your Personal Average Income Tax is: Rs", n)
            
        else:
            n = (n - 1000000)*(30/100)
            n = n + 110000
            print("Your Personal Average Income Tax is: Rs", n)
            
else:
    if a < 100000:
        if n < 500000:
            print("You don't have to pay Personal Income Tax")
            
        elif n < 1000000:
            n = (n - 500000)*(30/100)
            print("Your Personal Average Income Tax is: Rs", n)
            
        else:
            n = (n - 100000)*(30/100)
            n = n + 100000
            print("Your Personal Average Income Tax is: Rs", n)
            
print("\nTHANK YOU FOR USING THE INCOME TAX CALCULATOR. \nPress Enter to end the Python Program.")
            
input()
