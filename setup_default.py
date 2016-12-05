from datetime import datetime
from src.bank.bank import Bank
from src.customer.customer import Customer
from src.card.card import Card
from src.account.account import SavingsAccount, CheckingAccount

bank = Bank(name='USBank')
bank.put()

customer = Customer(first_name='John', last_name='Doe', bank=bank.key)
customer.put()

savings_account = SavingsAccount(bank=bank.key, interest=2.0, owner=customer.key, pin=1234, nickname='Emergency Fund', total_money=15000)
savings_account.put()

checking_account = CheckingAccount(bank=bank.key, interest=0.7, owner=customer.key, pin=4567, nickname='Checkings', total_money=8000)
checking_account.put()

card = Card(account=checking_account.key, number=4111111111111111, security_code=415, expiration_date=datetime(2018, 12, 1))
card.put()
