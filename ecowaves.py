# participantes
# Laura (RM: 558843) | Maria Eduarda (RM: 558832) | Vínicius Saes (RM: 554456)

# bibliotecas
import os
import re

# 1º função de validação - valida se o e-mail está nos conformes

def verifica_email(email):
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(regex, email):
        return True
    else:
        return False
    
# 2° função de validação - verifica se a senha está nos conformes
def verifica_senha(senha: str) -> bool:
    retorno = False
     # Verifica se a senha tem pelo menos 8 caracteres
    if len(senha) <= 8:
        print("A senha deve ter no mínimo 8 caracteres")
        return False
    
    # Verifica se a senha tem pelo menos um caractere especial
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', senha):
        print("A senha deve ter no mínimo um caractere especial")
        return False
    
    # Verifica se a senha tem pelo menos uma letra maiúscula
    if not re.search(r'[A-Z]', senha):
        print("A senha deve ter pelo menos uma letra maiúscula")
        return False
    
    # Se passou por todas as verificações, a senha é válida
    return True

# 3° função de validação - verifica se alguns dados estão corretamente (nome-> só letras | cnpj -> só n°s e 14 caracteres)
def verifica_dados(tipo, dado):
    retorno = False
    if tipo == "nome":
        regex = r'^[a-zA-Z\s]+$'  # apenas letras e espaços
    # elif tipo == "nome":
    #     regex = r'^[a-zA-Z\s]+$'  # apenas letras e espaços
    else:
        return False
    
    return re.match(regex, dado) is not None

# 4° função de validação - verifica se formato do CNPJ está correto
def validar_cnpj(cnpj):
    # Expressão regular para validar o formato do CNPJ
    cnpj_regex = r'^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$'
    
    if re.match(cnpj_regex, cnpj):
        return True
    else:
        return False
    
# Listas para armazenar os diferentes tipos de usuários
voluntarios = []
ongs = []
parceiros = []


# 2° função - solicita ao voluntario os dados necessários, depois os adiciona em um dicionário
def cadastrar_voluntario():
    nome = input("Nome completo: ")
    while not verifica_dados("nome", nome):
        print("Nome inválido. Tente novamente.")
        nome = input("Nome completo: ")

    email = input("E-mail: ")
    while not verifica_email(email):
        print("E-mail inválido. Tente novamente. (exemplo@domain.com)")
        email = input("E-mail: ")

    while True:
        senha = input("Senha:  ")
        if verifica_senha(senha):
            break

    id = len(voluntarios) + 1
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
    while not verifica_dados("nome", nome):
        print("Razão Social inválida. Tente novamente.")
        nome = input("Razão Social: ")

    email = input("E-mail: ")
    while not verifica_email(email):
        print("E-mail inválido. Tente novamente. (exemplo@domain.com)")
        email = input("E-mail: ")

    while True:
        senha = input("Senha:  ")
        if verifica_senha(senha):
            break

    cnpj = input("CNPJ: ")
    while not validar_cnpj(cnpj):
        print("CNPJ inválido. Tente novamente. (XX. XXX. XXX/0001-XX)")
        cnpj = input("CNPJ: ") 

    descricao = input("Descrição: ")

    id = len(ongs) + 1
    ong = {
        "id": id,
        "nome": nome,
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

    email = input("E-mail: ")
    while not verifica_email(email):
        print("E-mail inválido. Tente novamente. (exemplo@domain.com)")
        email = input("E-mail: ")

    while True:
        senha = input("Senha:  ")
        if verifica_senha(senha):
            break

    id = len(parceiros) + 1

    parceiro = {
        "id": id,
        "nome": nome,
        "email": email,
        "senha": senha,
        "tipo": "parceiro"
    }
    parceiros.append(parceiro)
    print("Parceiro cadastrado com sucesso!")

def login(tipo):
    print("\nDigite suas credenciais")
    email_login = input("Digite o seu e-mail: ")
    senha_login = input("Digite a sua senha: ")
    if not email_login == "" and not senha_login == "":
        if tipo == "1":
            for usuario in voluntarios:
                if usuario["email"] == email_login and usuario["senha"] == senha_login:
                    return usuario
        elif tipo == "2":
            for usuario in ongs:
                if usuario["email"] == email_login and usuario["senha"] == senha_login:
                    return usuario
        elif tipo == "3":
            for usuario in parceiros:
                if usuario["email"] == email_login and usuario["senha"] == senha_login:
                    return usuario
    return None

# FUNÇÕES DA ONG
def cadastrar_atividade(atividades, id_ong):
    while True:
        nome_atividade = input("Nome da atividade: ").strip()
        data_atividade = input("Data da atividade (dd/mm/aaaa): ").strip()
        descricao_atividade = input("Descrição da atividade: ").strip()
        vagas = input("Número de vagas: ").strip()
        local = input("Local da atividade: ").strip()
        horario = input("Horário da atividade (hh:mm - hh:mm): ").strip()
        
        
        # Gerar um ID único para a atividade
        id_atividade = len(atividades) + 1
        
        # Adicionar a atividade ao dicionário de atividades
        atividades[id_atividade] = {
            "ID": id_atividade,
            "Nome da Atividade": nome_atividade,
            "Data": data_atividade,
            "Descrição": descricao_atividade,
            "Vagas": vagas,
            "Local": local,
            "Horário": horario,
            "ID ONG": id_ong
        }
        
        # Perguntar se deseja adicionar outra atividade
        continuar = input("Deseja cadastrar outra atividade? (s/n): ").strip().lower()
        if continuar != 's':
            break


# Menu para interagir com o usuário
while True:

    print("				TELA INICIAL ECOWAVES")
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
                voluntario_logado = login(opcaoUser)
                if voluntario_logado: 
                    nome_usuario_logado = voluntario_logado['nome']
                    os.system("cls")
                    print(f"\nLogin realizado com sucesso, {nome_usuario_logado}! Você agora está logado em sua conta\n")
                    # opcao = input(f"\n0 - Sair | 1- Portal ou ChatBot | 2 - EcoVoluntariado | 3- Seu Perfil | 4- Descontos dos Parceiros")

                    while True:
                        opcao = input(f"\n0 - Sair | 1- Portal ou ChatBot | 2 - EcoVoluntariado | 3- Seu Perfil | 4- Descontos dos Parceiros\n")
                        match opcao:
                            case "0":
                                print("Obrigado por utilizar  EcoWaves!")
                                break
                            case "1":
                                cadastrar_atividade()
                            case "2":
                                ...
                            case "3":
                                ...
                            case 4:
                                ...
                else:
                    os.system("cls")
                    print("\nLogin ou senha incorretos. Tente novamente.")
            elif(opcaoUser == "2"):
                cadastrar_ong()
                ong_logada = login(opcaoUser)
                if ong_logada: 
                    razaosocial_ong = ong_logada['nome']
                    os.system("cls")
                    print(f"\nLogin realizado com sucesso, {razaosocial_ong}! Você agora está logado em sua conta\n")

                    while True:
                        opcao1 = input(f"\0 - Sair | 1- Registrar uma Atividade | 2 - Ver suas Atividades | 3- Seu Perfil\n")
                        match opcao1:
                            case "0":
                                print("Obrigado por utilizar  EcoWaves!")
                                break
                            case "1":
                                atividades = []
                                id_ong = ong_logada['id']
                                cadastrar_atividade(atividades,id_ong)
                            case "2":
                                ...
                            case "3":
                                ...
                            case 4:
                                ...
                else:
                    os.system("cls")
                    print("\nLogin ou senha incorretos. Tente novamente.")
                ong_logada = login(opcaoUser)
            elif(opcaoUser == "3"):
                cadastrar_parceiro()
                # print("Parceiro cadastrado")
        case "2":
            usuario = login(opcaoUser)
            if usuario:
                print(f"Bem-vindo, {usuario['nome']}!")
            else:
                print("Email ou senha inválidos.")     
            