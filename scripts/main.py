# Este é o script principal que inicializa o mod TrueBank.

from interactions import TrueBankInteraction

def main():
    print("TrueBank Mod Iniciado")

    # Inicializar interações TrueBank no celular e no computador
    celular_interaction = TrueBankInteraction("celular")
    computador_interaction = TrueBankInteraction("computador")

    # Exemplo de uso das interações
    celular_interaction.access_truebank()
    celular_interaction.show_options()
    celular_interaction.add_bank_icon()

    computador_interaction.access_truebank()
    computador_interaction.show_options()
    computador_interaction.add_computer_options()

if __name__ == "__main__":
    main()
