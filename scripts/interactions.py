# Este script define as interações do mod TrueBank no celular e no computador.

class TrueBankInteraction:
    def __init__(self, device_type):
        self.device_type = device_type
        self.credit_history = 0  # Valor fictício para histórico de crédito
        self.account_balance = 0  # Valor fictício para saldo da conta
        self.is_employed = False  # Situação de emprego do Sim
        self.income = 0  # Renda do Sim
        self.age_group = "adult"  # Grupo etário do Sim (pode ser 'child', 'teen', 'adult', 'elder')

    def access_truebank(self):
        self.show_message("Bem-vindo(a) ao TrueBank!", "Acesse todas as suas contas e serviços diretamente de qualquer dispositivo.")
        print(f"Acessando TrueBank via {self.device_type}...")

    def show_message(self, title, message):
        # Código para exibir uma mensagem personalizada através de um pop-up
        print(f"{title}\n{message}\n")

    def create_account(self):
        self.show_message("Sua conta foi criada com sucesso!", "Agora você pode gerenciar suas finanças de forma fácil e rápida.")
        print("Conta criada")

    def delete_account(self):
        self.show_message("Conta excluída!", "A sua conta foi excluída com sucesso.")
        print("Conta excluída")

    def join_account(self):
        self.show_message("Deseja juntar a sua conta com a de outro Sim?", "Contas conjuntas permitem que mais de um Sim administre as finanças.")
        print("Solicitação de conta conjunta")

    def create_youth_savings(self):
        self.show_message("Poupança Jovem Sim criada!", 
            "É maravilhoso ver nossas crianças crescendo, não é? No Poupança Jovem, você poderá ver sua criança crescer com o futuro garantido! "
            "Podendo ser criada desde o nascimento, a Poupança Jovem fica habilitada com a função de transferência até o Sim chegar à adolescência, quando ele poderá sacar os simoleons guardados por toda a vida!"
        )
        print("Poupança Jovem Sim criada")

    def request_loan(self, amount):
        if self.is_loan_approved(amount):
            self.show_message("Empréstimo Aprovado!", 
                f"Parabéns! Seu empréstimo de {amount} simoleons foi aprovado. Utilize o dinheiro com sabedoria."
            )
            self.account_balance += amount  # Adiciona o valor do empréstimo ao saldo da conta
        else:
            self.show_message("Empréstimo Negado", 
                "Infelizmente, seu empréstimo não foi aprovado. Tente novamente mais tarde ou entre em contato com o banco para mais informações."
            )
        print("Solicitação de empréstimo processada")

    def is_loan_approved(self, amount):
        # Regras fictícias de aprovação de empréstimo
        min_credit_history = 600  # Pontuação mínima de crédito
        max_loan_amount = self.account_balance * 2  # Pode pegar até 2x o saldo da conta
        min_income = 100  # Renda mínima para solicitar empréstimo

        if (self.credit_history >= min_credit_history and 
            amount <= max_loan_amount and 
            self.is_employed and 
            self.income > min_income and 
            self.age_group != "child"):
            return True
        return False

    def request_aposim_loan(self, amount):
        if self.is_aposim_loan_approved(amount):
            self.show_message("Empréstimo AposSim Aprovado!", 
                f"Parabéns! Seu empréstimo AposSim de {amount} simoleons foi aprovado. Utilize o dinheiro com sabedoria."
            )
            self.account_balance += amount  # Adiciona o valor do empréstimo ao saldo da conta
        else:
            self.show_message("Empréstimo AposSim Negado", 
                "Infelizmente, seu empréstimo AposSim não foi aprovado. Tente novamente mais tarde ou entre em contato com o banco para mais informações."
            )
        print("Solicitação de empréstimo AposSim processada")

    def is_aposim_loan_approved(self, amount):
        # Regras fictícias de aprovação de empréstimo AposSim
        min_credit_history = 600  # Pontuação mínima de crédito
        max_loan_amount = self.account_balance * 2  # Pode pegar até 2x o saldo da conta

        if (self.credit_history >= min_credit_history and 
            amount <= max_loan_amount and 
            self.age_group == "elder"):
            return True
        return False

    def invest(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            self.show_message("Investimento Realizado!", 
                f"Você investiu {amount} simoleons. Boa sorte com seus investimentos!"
            )
        else:
            self.show_message("Investimento Falhou", 
                "Saldo insuficiente para realizar o investimento."
            )

    def transfer_money(self, amount, target_account):
        if self.account_balance >= amount:
            self.account_balance -= amount
            self.show_message("Transferência Realizada!", 
                f"Você transferiu {amount} simoleons para a conta {target_account}."
            )
        else:
            self.show_message("Transferência Falhou", 
                "Saldo insuficiente para realizar a transferência."
            )

    def buy_crypto(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            self.show_message("Compra de Criptomoeda Realizada!", 
                f"Você comprou criptomoedas no valor de {amount} simoleons. Boa sorte com seus investimentos!"
            )
        else:
            self.show_message("Compra de Criptomoeda Falhou", 
                "Saldo insuficiente para realizar a compra de criptomoedas."
            )

    def check_balance(self):
        self.show_message("Saldo Atual", f"Seu saldo atual é de {self.account_balance} simoleons.")

    def show_options(self):
        options = ["Ver Saldo", "Transferir Dinheiro", "Solicitar Empréstimo", "Solicitar Empréstimo AposSim", "Investimentos", "Criar Conta", "Excluir Conta", "Comprar Criptomoeda"]
        print(f"Opções disponíveis no TrueBank ({self.device_type}):")
        for option in options:
            print(f"- {option}")

    def add_bank_icon(self):
        # Código para adicionar o ícone do banco no menu do celular
        print(f"Ícone do TrueBank adicionado ao {self.device_type}")

    def add_computer_options(self):
        # Código para adicionar opções no menu do computador
        print("Opções do TrueBank adicionadas ao computador")


# Exemplo de uso
celular_interaction = TrueBankInteraction("celular")
celular_interaction.account_balance = 5000  # Saldo fictício
celular_interaction.credit_history = 650  # Histórico de crédito fictício
celular_interaction.is_employed = True  # Sim empregado
celular_interaction.income = 200  # Renda fictícia
celular_interaction.age_group = "adult"  # Grupo etário

celular_interaction.access_truebank()
celular_interaction.create_account()
celular_interaction.join_account()
celular_interaction.create_youth_savings()
celular_interaction.request_loan(5000)  # Tentar pegar um empréstimo de 5000 simoleons
celular_interaction.request_loan(15000)  # Tentar pegar um empréstimo de 15000 simoleons
celular_interaction.request_aposim_loan(3000)  # Tentar pegar um empréstimo AposSim de 3000 simoleons
celular_interaction.request_aposim_loan(10000)  # Tentar pegar um empréstimo AposSim de 10000 simoleons
celular_interaction.invest(2000)  # Investir 2000 simoleons
celular_interaction.transfer_money(500, "Conta123")  # Transferir 500 simoleons para Conta123
celular_interaction.buy_crypto(1000)  # Comprar criptomoedas no valor de 1000 simoleons
celular_interaction.check_balance()  # Verificar saldo
celular_interaction.delete_account()  # Excluir conta
celular_interaction.show_options()
celular_interaction.add_bank_icon()

computador_interaction = TrueBankInteraction("computador")
computador_interaction.account_balance = 3000  # Saldo fictício
computador_interaction.credit_history = 550  # Histórico de crédito fictício
computador_interaction.is_employed = False  # Sim desempregado
computador_interaction.income = 50  # Renda fictícia
computador_interaction.age_group = "elder"  # Grupo etário

computador_interaction.access_truebank()
computador_interaction.create_account()
computador_interaction.join_account()
computador_interaction.create_youth_savings()
computador_interaction.request_loan(2000)  # Tentar pegar um empréstimo de 2000 simoleons
computador_interaction.request_loan(7000)  # Tentar pegar um empréstimo de 7000 simoleons
computador_interaction.request_aposim_loan(3000)  # Tentar pegar um empréstimo AposSim de 3000 simoleons
computador_interaction.request_aposim_loan(10000)  # Tentar pegar um empréstimo AposSim de 10000 simoleons
computador_interaction.invest(1000)  # Investir 1000 simoleons
computador_interaction.transfer_money(300, "Conta456")  # Transferir 300 simoleons para Conta456
computador_interaction.buy_crypto(500)  # Comprar criptomoedas no valor de 500 simoleons
computador_interaction.check_balance()  # Verificar saldo
computador_interaction.delete_account()  # Excluir conta
computador_interaction.show_options()
computador_interaction.add_computer_options()
