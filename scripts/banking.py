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

    def get_balance(self):
        return self.balance


# Conta Conjunta
class JointAccount(BankAccount):
    def __init__(self, account_type, holders, balance=0):
        super().__init__(account_type, balance)
        self.holders = holders


# Exemplo de uso
conta = BankAccount("corrente", 100)
conta.deposit(50)
conta.withdraw(30)

conta_conjunta = JointAccount("conjunta", ["Sim1", "Sim2"], 200)
conta_conjunta.deposit(100)
conta_conjunta.withdraw(50)
