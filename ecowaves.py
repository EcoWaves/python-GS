# participantes
# Laura (RM: 558843) | Maria Eduarda (RM: 558832) | Vínicius Saes (RM: 554456)

# bibliotecas
import os
import re

# 1º função - valida se o e-mail está nos conformes

def verifica_email(email):
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(regex, email):
        return True
    else:
        return False
    
# Listas para armazenar os diferentes tipos de usuários
voluntarios = []
ongs = []
parceiros = []

# 2° função - solicita ao voluntario os dados necessários, depois os adiciona em um dicionário
def cadastrar_voluntario():
    nome = input("Nome: ")
    email = input("Email: ")
    senha = input("Senha: ")
    voluntario = {
        "id": id,
        "nome": nome,
        "email": email,
        "senha": senha,
        "tipo": "voluntario"
    }
    voluntarios.append(voluntario)
    print("Voluntário cadastrado com sucesso!")

# 3° função - solicita a ONG os dados necessários, depois os adiciona em um dicionário
def cadastrar_ong():
    nome = input("Razão Social: ")
    email = input("Email: ")
    senha = input("Senha: ")
    cnpj = input("CNPJ: ") 
    descricao = input("Descrição: ")
    ong = {
        "id": id,
        "razao_social": nome,
        "email": email,
        "senha": senha,
        "cnpj": cnpj,
        "descricao": descricao,
        "tipo": "ong"
    }
    ongs.append(ong)
    print("ONG cadastrada com sucesso!")

# 4° função - solicita ao parceiro (hospedagens) os dados necessários, depois os adiciona em um dicionário
def cadastrar_parceiro():
    nome = input("Razão Social: ")
    email = input("Email: ")
    senha = input("Senha: ")
    parceiro = {
        "razao_social": nome,
        "email": email,
        "senha": senha,
        "tipo": "parceiro"
    }
    parceiros.append(parceiro)
    print("Parceiro cadastrado com sucesso!")

def login(tipo, email, senha):
    if tipo == "1":
        for usuario in voluntarios:
            if usuario["email"] == email and usuario["senha"] == senha:
                return usuario
    elif tipo == "2":
        for usuario in ongs:
            if usuario["email"] == email and usuario["senha"] == senha:
                return usuario
    elif tipo == "3":
        for usuario in parceiros:
            if usuario["email"] == email and usuario["senha"] == senha:
                return usuario
    return None

# Menu para interagir com o usuário
while True:

    print("				OLÁ!!! BEM-VINDO(A) AO ECOWAVES. ESCOLHA UMA OPÇÃO QUE VOCÊ SE ENCAIXE:")
    opcaoUser = input("1 - Voluntario | 2 - ONG | 3 - Parceiro (hospedagens) | ")
    opcaoEntrada = input("Legal! E você deseja (1)cadastrar-se, (2) fazer login ou (3) sair do sistema? ")
    
    # print("1. Cadastrar Voluntário")
    # print("2. Cadastrar ONG")
    # print("3. Cadastrar Parceiro")
    # print("4. Login")
    # print("5. Sair")
    
    # opcao = input("Escolha uma opção: ")

    match(opcaoEntrada):
        case "1":
            if(opcaoUser == "1"):
                cadastrar_voluntario()
                print("Voluntario cadastrado")
            elif(opcaoUser == "2"):
                cadastrar_ong()
                print("ONG cadastrada")
            elif(opcaoUser == "3"):
                cadastrar_parceiro()
                print("Parceiro cadastrado")
        case "2":
            email = input("Email: ")
            senha = input("Senha: ")
            usuario = login(opcaoUser,email, senha)
            if usuario:
                print(f"Bem-vindo, {usuario['nome']}!")
            else:
                print("Email ou senha inválidos.")     
            