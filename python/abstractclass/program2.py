from abc import ABC, abstractmethod

# Abstract class
class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        """Subclasses must implement this method"""
        pass

    def payment_info(self):
        print("Payment processing system.")

# Subclass for Credit Card payments
class CreditCardPayment(Payment):

    def pay(self, amount):
        print(f"Paid {amount} using Credit Card.")

# Subclass for PayPal payments
class PayPalPayment(Payment):

    def pay(self, amount):
        print(f"Paid {amount} using PayPal.")

# Subclass for Bank Transfer payments
class BankTransferPayment(Payment):

    def pay(self, amount):
        print(f"Paid {amount} via Bank Transfer.")

# Usage
c = CreditCardPayment()
c.pay(500)       # Output: Paid 500 using Credit Card.
c.payment_info() # Output: Payment processing system.

p = PayPalPayment()
p.pay(300)       # Output: Paid 300 using PayPal.

b = BankTransferPayment()
b.pay(1000)      # Output: Paid 1000 via Bank Transfer.
