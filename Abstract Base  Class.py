from abc import ABCMeta, abstractmethod

class PaymentGateway(metaclass=ABCMeta):

    @abstractmethod
    def process_payment(self, amount):
        pass

class paypal(PaymentGateway):
    def process_payment(self, amount):
        print(f"Processing {amount} $ through PayPal securely.....")

class creditcard(PaymentGateway):
    def process_payment(self, amount):
        print(f"Processing {amount} $ through Credit Card network.....")

# Pay = PaymentGateway

p = paypal()
p.process_payment(500)

c = creditcard()
c.process_payment(1200)
