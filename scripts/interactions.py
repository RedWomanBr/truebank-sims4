# Este script define as interações do mod TrueBank no celular e no computador.

class TrueBankInteraction:
    def __init__(self, device_type):
        self.device_type = device_type

    def access_truebank(self):
        print(f"Acessando TrueBank via {self.device_type}...")
        self.show_popup("Bem-vindo ao TrueBank!")

    def show_popup(self, message):
        # Código para exibir um pop-up com a mensagem fornecida
        print(f"Pop-up: {message}")

    def show_options(self):
        options = ["Ver Saldo", "Transferir Dinheiro", "Solicitar Empréstimo", "Investimentos"]
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
celular_interaction.access_truebank()
celular_interaction.show_options()
celular_interaction.add_bank_icon()

computador_interaction = TrueBankInteraction("computador")
computador_interaction.access_truebank()
computador_interaction.show_options()
computador_interaction.add_computer_options()
