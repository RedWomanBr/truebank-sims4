# Este script contém as funcionalidades bancárias do mod TrueBank.

class BankAccount:
    def __init__(self, account_type, balance=0):
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Depositado: {amount}. Saldo Atual: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Retirado: {amount}. Saldo Atual: {self.balance}")
        else:
            print("Saldo Insuficiente")

# Exemplo de uso
conta = BankAccount("corrente", 100)
conta.deposit(50)
conta.withdraw(30)
