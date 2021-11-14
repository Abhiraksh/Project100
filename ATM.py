import random

class ATM(object):
    def __init__(self, cardNumber, pinCode):
        self.cardNumbeer = cardNumber
        self.pinCode = pinCode
    
    def bankEnquiry(self, cardNumber):
        rndAmt  = random.randint(100, 100000000)
        print("For card number:", cardNumber ,", The bank balance is: Rs", rndAmt)

    def cashWithdrawal(self, cardNumber, money):
        rndAmt  = random.randint(100, 100000000)
        print("Rs" , money , "was withdrawed from the card number", cardNumber)
        print("Your current amount is", rndAmt)

def main():
    cardNumber = int(input("Enter your card number: "))
    pincode = int(input("Enter your pincode: "))
    eOw = input("Bank Enquiry(B) or Cash Withdrawal(C): ")
    result = ATM(cardNumber, pincode)

    if(eOw == "B"):
        result.bankEnquiry(cardNumber)
    elif(eOw == "C"):
        money = int(input("Enter the amount: "))
        result.cashWithdrawal(cardNumber,money)
    else:
        print("This service does not exxist, please enter B for Bank Enquiry or C for Cash WWithdrawal")

main()

      
 

    