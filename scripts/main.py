import logging
from interactions import TrueBankInteraction

logging.basicConfig(level=logging.INFO)

def initialize_interaction(device_type: str, balance: int, credit: int, employed: bool, income: int, age_group: str) -> TrueBankInteraction:
    interaction = TrueBankInteraction(device_type)
    interaction.account_balance = balance
    interaction.credit_history = credit
    interaction.is_employed = employed
    interaction.income = income
    interaction.age_group = age_group
    return interaction

def perform_interactions(interaction: TrueBankInteraction):
    try:
        interaction.access_truebank()
        interaction.create_account()
        interaction.join_account()
        interaction.create_youth_savings()
        interaction.request_loan(5000)
        interaction.request_loan(15000)
        interaction.request_aposim_loan(3000)
        interaction.request_aposim_loan(10000)
        interaction.invest(2000)
        interaction.transfer_money(500, "Conta123")
        interaction.buy_crypto(1000)
        interaction.check_balance()
        interaction.delete_account()
        interaction.show_options()
    except Exception as e:
        logging.error(f"An error occurred during interactions: {e}")

def main():
    logging.info("TrueBank Mod Iniciado")

    celular_interaction = initialize_interaction("celular", 5000, 650, True, 200, "adult")
    computador_interaction = initialize_interaction("computador", 3000, 550, False, 50, "elder")

    perform_interactions(celular_interaction)
    perform_interactions(computador_interaction)

if __name__ == "__main__":
    main()
