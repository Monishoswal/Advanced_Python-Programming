from abc import ABC, abstractmethod
class PaymentStrategy(ABC):
    def pay(self, amount):
        pass
class CreditCard(PaymentStrategy):
    def pay(self, amount):
        return f"Paid ${amount} using Credit Card"
class PayPal(PaymentStrategy):
    def pay(self, amount):
        return f"Paid ${amount} using PayPal"
class Crypto(PaymentStrategy):
    def pay(self, amount):
        return f"Paid ${amount} using Crypto"
class PaymentProcessor:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def process(self, amount):
        print(self.strategy.pay(amount))
        
print("Payment Methods")
print("1. Credit Card")
print("2. PayPal")
print("3. Crypto")

choice = int(input("Enter your choice (1-3): "))
amount = float(input("Enter payment amount: "))

if choice == 1:
    strategy = CreditCard()
elif choice == 2:
    strategy = PayPal()
elif choice == 3:
    strategy = Crypto()
else:
    print("Invalid payment method!")
    exit()

processor = PaymentProcessor(strategy)
processor.process(amount)
