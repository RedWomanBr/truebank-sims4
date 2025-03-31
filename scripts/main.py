# Este é o script principal que inicializa o mod TrueBank.

from interactions import TrueBankInteraction

def main():
    print("TrueBank Mod Iniciado")

    # Inicializar interações TrueBank no celular e no computador
    celular_interaction = TrueBankInteraction("celular")
    computador_interaction = TrueBankInteraction("computador")

    # Configurar saldo, histórico de crédito, situação de emprego e renda fictícios
    celular_interaction.account_balance = 5000
    celular_interaction.credit_history = 650
    celular_interaction.is_employed = True
    celular_interaction.income = 200
    celular_interaction.age_group = "adult"

    computador_interaction.account_balance = 3000
    computador_interaction.credit_history = 550
    computador_interaction.is_employed = False
    computador_interaction.income = 50
    computador_interaction.age_group = "elder"

    # Exemplo de uso das interações
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

if __name__ == "__main__":
    main()
