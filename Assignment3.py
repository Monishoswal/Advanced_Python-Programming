from datetime import datetime
import uuid


class PaymentProcessor:
    def __init__(self):
        self.history = []
        self.transaction_counter = 0

    def process_credit_card(self, card, cvv, amount):
        if not card or not cvv or amount <= 0:
            return {"status": "failed", "message": "Invalid card details"}
        if len(str(card)) != 16 or len(str(cvv)) != 3:
            return {"status": "failed", "message": "Invalid card details"}
        return self.create_transaction("credit_card", amount, "CC")

    def process_paypal(self, email, amount):
        if not email or "@" not in email or amount <= 0:
            return {"status": "failed", "message": "Invalid PayPal email"}
        return self.create_transaction("paypal", amount, "PP")

    def process_crypto(self, wallet, currency, amount):
        if not wallet or len(wallet) <= 10 or amount <= 0:
            return {"status": "failed", "message": "Invalid wallet address"}
        return self.create_transaction("cryptocurrency", amount, "CR")

    def process_bank(self, account, routing, amount):
        if not account or not routing or amount <= 0:
            return {"status": "failed", "message": "Invalid bank details"}
        if len(str(account)) < 8 or len(str(routing)) != 9:
            return {"status": "failed", "message": "Invalid bank details"}
        return self.create_transaction("bank_transfer", amount, "BT")

    def create_transaction(self, method, amount, prefix):
        self.transaction_counter += 1
        result = {
            "status": "success",
            "method": method,
            "amount": amount,
            "timestamp": datetime.now().isoformat(),
            "transaction_id": f"{prefix}{self.transaction_counter}{uuid.uuid4().hex[:8]}"
        }
        self.history.append(result)
        return result

    def get_history(self):
        return self.history

    def clear_history(self):
        self.history = []


if __name__ == "__main__":
    processor = PaymentProcessor()

    result1 = processor.process_credit_card("1234567890123456", "123", 99.99)
    print("Credit Card Transaction:", result1)

    result2 = processor.process_paypal("user@paypal.com", 50.00)
    print("PayPal Transaction:", result2)

    result3 = processor.process_crypto("1A1z7agoat2gwc2f2gG5z", "Bitcoin", 0.5)
    print("Crypto Transaction:", result3)

    result4 = processor.process_bank("123456789", "987654321", 250.00)
    print("Bank Transfer Transaction:", result4)

    print("\nTransaction History:")
    for transaction in processor.get_history():
        print(transaction)
