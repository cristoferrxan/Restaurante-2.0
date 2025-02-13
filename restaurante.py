import os
from collections import defaultdict
from fastapi import FastAPI

app = FastAPI()

# Classes de Avaliações
class Avaliacao:
    def __init__(self, cliente, nota, comentario=""):
        if 1 <= nota <= 5:
            self.cliente = cliente
            self.nota = nota
            self.comentario = comentario
        else:
            raise ValueError("A nota deve estar entre 1 e 5.")

class SistemaAvaliacoes:
    def __init__(self):
        self.avaliacoes = defaultdict(list)

    def registrar_avaliacao(self, restaurante, cliente, nota, comentario=""):
        try:
            avaliacao = Avaliacao(cliente, nota, comentario)
            self.avaliacoes[restaurante].append(avaliacao)
            return {"mensagem": "Avaliação registrada com sucesso!"}
        except ValueError as e:
            return {"erro": str(e)}

    def calcular_media(self, restaurante):
        if restaurante in self.avaliacoes and self.avaliacoes[restaurante]:
            total_notas = sum(avaliacao.nota for avaliacao in self.avaliacoes[restaurante])
            quantidade = len(self.avaliacoes[restaurante])
            return round(total_notas / quantidade, 2)
        return 0

    def listar_avaliacoes(self, restaurante):
        if restaurante in self.avaliacoes:
            return [{"cliente": av.cliente, "nota": av.nota, "comentario": av.comentario} for av in self.avaliacoes[restaurante]]
        return {"mensagem": "Nenhuma avaliação encontrada."}

# Classes de Clientes
class Cliente:
    def __init__(self, nome, idade, telefone, email):
        if idade < 0:
            raise ValueError("A idade não pode ser negativa.")
        self.nome = nome
        self.idade = idade
        self.telefone = telefone
        self.email = email

class SistemaClientes:
    def __init__(self):
        self.clientes = {}

    def cadastrar_cliente(self, nome, idade, telefone, email):
        if email in self.clientes:
            return {"erro": "Já existe um cliente cadastrado com este e-mail."}
        try:
            cliente = Cliente(nome, idade, telefone, email)
            self.clientes[email] = cliente
            return {"mensagem": "Cliente cadastrado com sucesso!"}
        except ValueError as e:
            return {"erro": str(e)}

    def listar_clientes(self):
        return [{"nome": c.nome, "idade": c.idade, "telefone": c.telefone, "email": c.email} for c in self.clientes.values()]

    def buscar_cliente(self, email):
        if email in self.clientes:
            c = self.clientes[email]
            return {"nome": c.nome, "idade": c.idade, "telefone": c.telefone, "email": c.email}
        return {"erro": "Cliente não encontrado."}

# Classe de Restaurante
class Restaurante:
    def __init__(self, nome, categoria, ativo=False):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.cardapio = {}
        self.pedidos = defaultdict(int)

    def adicionar_prato(self, nome, preco):
        self.cardapio[nome] = preco

    def registrar_pedido(self, prato):
        if prato in self.cardapio:
            self.pedidos[prato] += 1
        else:
            return "Prato não encontrado no cardápio."

restaurantes = [
    Restaurante("Praça", "Japonesa", False),
    Restaurante("Pizza Suprema", "Pizza", True),
    Restaurante("Cantina", "Italiano", False)
]

# Instanciando os sistemas de avaliações e clientes
sistema_avaliacoes = SistemaAvaliacoes()
sistema_clientes = SistemaClientes()

# Rotas da API
@app.post("/criar_restaurante/")
def criar_restaurante(nome: str, categoria: str):
    restaurante = Restaurante(nome, categoria)
    restaurantes.append(restaurante)
    return {"mensagem": "Restaurante criado com sucesso!", "nome": nome, "categoria": categoria}

@app.post("/adicionar_prato/")
def adicionar_prato(nome_restaurante: str, nome_prato: str, preco: float):
    for restaurante in restaurantes:
        if restaurante.nome == nome_restaurante:
            restaurante.adicionar_prato(nome_prato, preco)
            return {"mensagem": "Prato adicionado com sucesso!", "prato": nome_prato, "preco": preco}
    return {"erro": "Restaurante não encontrado."}

@app.post("/registrar_avaliacao/")
def registrar_avaliacao(restaurante: str, cliente: str, nota: int, comentario: str = ""):
    return sistema_avaliacoes.registrar_avaliacao(restaurante, cliente, nota, comentario)

@app.get("/listar_avaliacoes/")
def listar_avaliacoes(restaurante: str):
    return sistema_avaliacoes.listar_avaliacoes(restaurante)

@app.get("/calcular_media_avaliacoes/")
def calcular_media_avaliacoes(restaurante: str):
    media = sistema_avaliacoes.calcular_media(restaurante)
    return {"media": media}

@app.post("/cadastrar_cliente/")
def cadastrar_cliente(nome: str, idade: int, telefone: str, email: str):
    return sistema_clientes.cadastrar_cliente(nome, idade, telefone, email)

@app.get("/listar_clientes/")
def listar_clientes():
    return sistema_clientes.listar_clientes()

@app.get("/buscar_cliente/")
def buscar_cliente(email: str):
    return sistema_clientes.buscar_cliente(email)

@app.get("/listar_restaurantes/")
def listar_restaurantes():
    return [{"nome": r.nome, "categoria": r.categoria, "ativo": r.ativo} for r in restaurantes]

@app.post("/alternar_estado_restaurante/")
def alternar_estado_restaurante(nome_restaurante: str):
    for restaurante in restaurantes:
        if restaurante.nome == nome_restaurante:
            restaurante.ativo = not restaurante.ativo
            estado = "ativado" if restaurante.ativo else "desativado"
            return {"mensagem": f"O restaurante {nome_restaurante} foi {estado} com sucesso."}
    return {"erro": "Restaurante não encontrado."}

# Interface no terminal (opcional, se você quiser manter)
def exibir_nome_do_programa():
    print("Sistema de Gerenciamento de Restaurantes\n")

def exibir_opcoes():
    print("1. Cadastrar restaurante")
    print("2. Listar restaurantes")
    print("3. Alternar estado do restaurante")
    print("4. Sair\n")

def escolher_opcao():
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))
        if opcao_escolhida == 1:
            nome = input("Nome do restaurante: ")
            categoria = input("Categoria: ")
            criar_restaurante(nome, categoria)
        elif opcao_escolhida == 2:
            print(listar_restaurantes())
        elif opcao_escolhida == 3:
            nome = input("Nome do restaurante para alternar estado: ")
            print(alternar_estado_restaurante(nome))
        elif opcao_escolhida == 4:
            print("Encerrando programa...")
            exit()
        else:
            print("Opção inválida!")
    except:
        print("Opção inválida!")

def main():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        exibir_nome_do_programa()
        exibir_opcoes()
        escolher_opcao()

if __name__ == "__main__":
    main()