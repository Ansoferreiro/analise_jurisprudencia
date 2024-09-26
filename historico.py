def salvar_historico(analise):
    with open('historico.txt', 'a') as f:
        f.write(analise + '\n')

def listar_historico():
    with open('historico.txt', 'r') as f:
        return f.readlines()
