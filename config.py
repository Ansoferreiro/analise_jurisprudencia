import json

class Configuracoes:
    def __init__(self, arquivo='config.json'):
        self.arquivo = arquivo
        self.carregar_configuracoes()

    def carregar_configuracoes(self):
        try:
            with open(self.arquivo, 'r') as f:
                self.configuracoes = json.load(f)
        except FileNotFoundError:
            self.configuracoes = {}

    def salvar_configuracoes(self):
        with open(self.arquivo, 'w') as f:
            json.dump(self.configuracoes, f, indent=4)

    def atualizar_configuracao(self, chave, valor):
        self.configuracoes[chave] = valor
        self.salvar_configuracoes()

if __name__ == "__main__":
    config = Configuracoes()
    config.atualizar_configuracao('linguagem', 'português')
def carregar_configuracao():
    # Lógica para carregar configurações do usuário
    pass

def salvar_configuracao(config):
    # Lógica para salvar configurações do usuário
    pass
