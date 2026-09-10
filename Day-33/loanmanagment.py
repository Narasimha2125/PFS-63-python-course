from abc import ABC,abstractmethod
class Customer:
    def __init__(self,customer_id,name,email,phonenumber,age,income,creadit_score,):
        self.Customer_id=customer_id
        self.name=name
        self.email=email
        self.phonenumber=phonenumber
        self.age=age
        self.income=income
        self.creadit_score=creadit_score
    def check_Eligibility(self):
        if self.age<21 or self.creadit_score<650 or self.income<25000:
            return False
        return True
    def display_customer(self):
        print("\ncustomer details")
        print("-------------------")
        print(" Customer ID :", self.Customer_id)
        print("Name         :", self.name)
        print("Email        : ", self.email)
        print("Phonenumber  : ", self.phonenumber)
        print("Age          : ", self.age)
        print("Income       : ", self.income)
        print("Creadit_score: ", self.creadit_score)

Baireddy = Customer(1, 'Baireddy','baireddy@gmail.com',8106686988,21,50000,750)
print("Eligibility:",Baireddy.check_Eligibility)
Baireddy.display_customer()

class Loan(ABC):
    def __init__(self,loan_id,customer_id,loan_amount,interest_rate,tenure):
        self.loan_id=loan_id
        self.customer=self.customer
        self.loan_amount=loan_amount
        self.interest_rate=interest_rate
        self.tenure=tenure
        self.__balance=loan_amount
        self.__total__paid=0
        self.repayment_history=[]
        self.status="Applied"

    @abstractmethod
    def calculate_emi(self):
        pass
    def check_loan_eligilibility(self):
        if not self.customer.check_eligilibility():
            self.status="Rejected"
            return False
        return True

    def sanction_loan(self):
        if self.status=="Rejected":
            print("customer is not eligible for the loan")
            return
        self.status="sanctioned"
        print("\nLoan sanctioned successfully")

    def repay(self,amount):
        if self.status !="sanctioned":
            print("Repayment is not allowed")
            print("Loan status",self.status)
            return

        if amount<=0:
            print("Invalid repayment amount")
            return

        if amount>self.__balance:
            print("Repayment amount is greater than outstanding balance")
            return

        self.__balance -=amount
        self.__total_paid +=amount
        self.repayment_history.append(amount)

        

        print("\nRepayment successfully")
        print("Amount paid        :",amount)
        print("Outstanding Balnce :",self.__balance)

        if self.__balance==0:
            self.status="Closed"
            print("Loan closed successfully")

    def get_balance(self):
        return self.__balance

    def get_loan_amount(self):
        return self.get_loan_amount

    def get_total_paid(self):
        return self.__total__paid

    def display_statement(self):

        print("\n")
        print("=" * 40)
        print("LOAN STATEMENT")
        print("=" * 40)

        print("Loan ID              :", self.loan_id)
        print(" Customer Name       :", self.Customer_name)
        print("Loan Amount          :", self.name)
        print("Interest Rate        :", self.interest_rate)
        print("tenure               :", self.tenure)
        print("Total Paid           :", self.total_paid)
        print("Outstanding Balance  :", self.balance)
        print("Loan Status          :", self.status)

        print("\nRepayment History")

        if not self.repayment_history:
            print("No repaymenet made")
        else:
            for i in range(len(self.repayment_history)):
                print(f"payment {i+1}        : {self.repayment_history[i]}")
        print("=" * 40)

    def __str__(self):
        return (
            f"Loan ID: {self.loan_id},"
            f"Customer: {self.customer.name},"
            f"Loan Amount: {self.__loan_amount},"
            f"Ouststanding: {self.__balance},"
            f"Status: {self.status}"
        )