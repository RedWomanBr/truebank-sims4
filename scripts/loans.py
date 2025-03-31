class Loan:
    def __init__(self, loan_type, amount, interest_rate):
        self.loan_type = loan_type
        self.amount = amount
        self.interest_rate = interest_rate
        self.balance = amount

    def make_payment(self, payment):
        self.balance -= payment
        print(f"Pagamento de {payment} realizado. Saldo do empréstimo: {self.balance}")

    def calculate_interest(self):
        return self.balance * self.interest_rate


# Empréstimo Consignado
class ConsignedLoan(Loan):
    def __init__(self, amount, interest_rate, employer):
        super().__init__("consignado", amount, interest_rate)
        self.employer = employer


# Exemplo de uso
emprestimo = Loan("estudantil", 500, 0.05)
emprestimo.make_payment(50)
print(f"Juros: {emprestimo.calculate_interest()}")

emprestimo_consignado = ConsignedLoan(1000, 0.03, "Empresa X")
emprestimo_consignado.make_payment(100)
print(f"Juros: {emprestimo_consignado.calculate_interest()}")
