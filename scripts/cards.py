class Card:
    def __init__(self, card_type, limit):
        self.card_type = card_type
        self.limit = limit
        self.balance = 0

    def make_purchase(self, amount):
        if self.balance + amount <= self.limit:
            self.balance += amount
            print(f"Compra de {amount} realizada. Saldo do cartão: {self.balance}")
        else:
            print("Limite do cartão excedido")

    def pay_bill(self, amount):
        self.balance -= amount
        print(f"Pagamento de {amount} realizado. Saldo do cartão: {self.balance}")


# Cartões Específicos
class CreditCard(Card):
    def __init__(self, card_type, limit):
        super().__init__(card_type, limit)


class DebitCard(Card):
    def __init__(self, account):
        super().__init__("débito", account.get_balance())
        self.account = account

    def make_purchase(self, amount):
        if self.account.get_balance() >= amount:
            self.account.withdraw(amount)
            print(f"Compra de {amount} realizada usando cartão de débito. Saldo da conta: {self.account.get_balance()}")
        else:
            print("Saldo insuficiente na conta para compra")


# Exemplo de uso
cartao_credito = CreditCard("Gold", 250000)
cartao_credito.make_purchase(50000)
cartao_credito.pay_bill(10000)

conta = BankAccount("corrente", 1000)
cartao_debito = DebitCard(conta)
cartao_debito.make_purchase(200)
