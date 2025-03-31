# Este script contém as funcionalidades de empréstimo do mod TrueBank.

class Loan:
    def __init__(self, loan_type, amount, interest_rate):
        self.loan_type = loan_type
        self.amount = amount
        self.interest_rate = interest_rate
        self.balance = amount

    def make_payment(self, payment):
        self.balance -= payment
        print(f"Pagamento de {payment} realizado. Saldo do empréstimo: {self.balance}")

# Exemplo de uso
emprestimo = Loan("estudantil", 500, 0.05)
emprestimo.make_payment(50)
