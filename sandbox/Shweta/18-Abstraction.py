from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def make_payment(self, amount):
        pass

class creditcard(PaymentMethod):
    def make_payment(self, amount):
        print(f"Paid ${amount} using Credit Card")

class UPI(PaymentMethod):
    def make_payment(self, amount):
        print(f"Paid ${amount} using UPI")

class Wallet(PaymentMethod):
    def make_payment(self, amount):
        print(f"Paid ${amount} using Digital Wallet")

method1 = UPI()
method1.make_payment(500)

method2=creditcard()
method2.make_payment(100)

method3 = Wallet()
method3.make_payment(90)
