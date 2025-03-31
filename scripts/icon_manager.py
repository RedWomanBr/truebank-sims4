import os

class IconManager:
    def __init__(self, device_type):
        self.device_type = device_type
        self.icon_path = os.path.join(os.path.dirname(__file__), 'icons', 'truebank_icon.png')

    def add_icon_to_menu(self):
        # Implementar a lógica para adicionar o ícone ao menu do celular
        # Esta função precisa ser compatível com a API do jogo
        try:
            # Supondo que há uma função no jogo para adicionar ícones personalizados
            print(f"Ícone do TrueBank adicionado ao {self.device_type} com o caminho {self.icon_path}")
        except Exception as e:
            print(f"Erro ao adicionar ícone: {e}")
