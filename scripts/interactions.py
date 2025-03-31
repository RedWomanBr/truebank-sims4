# Este script define as interações do mod TrueBank no celular e no computador.

class TrueBankInteraction:
    def __init__(self, device_type):
        self.device_type = device_type

    def access_truebank(self):
        print(f"Acessando TrueBank via {self.device_type}...")
        # Código para abrir a interface TrueBank no jogo

    def show_options(self):
        options = ["Ver Saldo", "Transferir Dinheiro", "Solicitar Empréstimo", "Investimentos"]
        print(f"Opções disponíveis no TrueBank ({self.device_type}):")
        for option in options:
            print(f"- {option}")

# Exemplo de uso
celular_interaction = TrueBankInteraction("celular")
celular_interaction.access_truebank()
celular_interaction.show_options()

computador_interaction = TrueBankInteraction("computador")
computador_interaction.access_truebank()
computador_interaction.show_options()
