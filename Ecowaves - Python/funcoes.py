# TODAS AS FUNÇÕES QUE DESENVOLVEMOS PARA EXECUÇÃO DO PROGRAMA PRINCIPAL

# importações
import os
import re
import webbrowser
from datetime import datetime



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
    if len(senha) < 8:
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
    
# 5° função de validação - valida se uma data está correta
def validar_data(data_str):
    try:
        data = datetime.strptime(data_str, '%d/%m/%Y')
        return data
    except ValueError:
        return None
    
# 6° função de validação - valida se o horário está correto
def validar_horario(horario_str):
    try:
        horario_inicio, horario_fim = horario_str.split(" - ")
        inicio = datetime.strptime(horario_inicio, '%H:%M').time()
        fim = datetime.strptime(horario_fim, '%H:%M').time()
        if inicio >= fim:
            print("Horário inválido. O horário de início deve ser antes do horário de fim.")
            return None
        return horario_str
    except ValueError:
        return None
    
# 7° função de validação - valida se o usuário já foi cadastrado pelo e-mail digitado
def verificar_usuario_por_email(lista_usuarios, email):
    for usuario in lista_usuarios:
        if usuario.get('email') == email:
            return True
    return False

# 8° função de validação - valida se um número é float
def isfloat(v:str) -> bool:
    numeros = "0123456789"
    sinais = "+-"
    contaPonto = 0   #flag contadora que ve quantos pontos tem na string

    retorno = True #flag que auxilia no retorno

    if v[0] in sinais or v[0] in numeros:
        for i in range(1, len(v)):
            if v[i] == ",":
               retorno = False
               break        #para sair do laço já que achou uma virgula
            if v[i] in numeros:
              if v[i] == ".":
                contaPonto= contaPonto + 1
                if contaPonto > 1:
                    retorno = False
                    break   #para sair do laço, já que existe mais de 1 ponto (.)
    else:
        retorno = False
    return retorno
    
# Listas para armazenar os diferentes tipos de usuários
voluntarios = []
ongs = []
parceiros = []

# Listas para armazenar as funcionalidades de criar (atividades e cupons) do site
atividades = []
cupons = []


# 2° função - solicita ao voluntario os dados necessários, depois os adiciona em um dicionário
def cadastrar_voluntario():
    print("\nCadastro:")
    nome = input("Nome: ")
    while not verifica_dados("nome", nome):
        print("Nome inválido. Tente novamente.")
        nome = input("Nome: ")

    email = input("E-mail: ")
    while not verifica_email(email):
        print("E-mail inválido. Tente novamente. (exemplo@domain.com)")
        email = input("E-mail: ")
    while verificar_usuario_por_email(voluntarios, email):
        print("Esse e-mail já está cadastrado em nosso sistema.")
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

    # Adicionar o nova voluntario à lista de voluntarios
    voluntarios.append(voluntario)
    
    os.system("cls")
    print(f"\nSeja bem-vindo, {nome}!!! Cadastro realizado com sucesso! Por favor, faça login para continuar.\n")

# 3° função - solicita a ONG os dados necessários, depois os adiciona em um dicionário
def cadastrar_ong():
    print("\nCadastro:")
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
    nova_ong = {
        "id": id,
        "nome": nome,
        "email": email,
        "senha": senha,
        "cnpj": cnpj,
        "descricao": descricao,
        "tipo": "ong"
    }

    # Adicionar a nova ONG à lista de ONGS
    ongs.append(nova_ong)
    
    os.system("cls")
    print(f"\nSeja bem-vindo, {nome}!!! Cadastro realizado com sucesso! Por favor, faça login para continuar.\n")

# 4° função - solicita ao parceiro (hospedagens) os dados necessários, depois os adiciona em um dicionário
def cadastrar_parceiro():
    print("\nCadastro:")

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

    id = len(parceiros) + 1

    novo_parceiro = {
        "id": id,
        "nome": nome,
        "email": email,
        "senha": senha,
        "tipo": "parceiro"
    }
    # Adicionar o novo parceiro à lista de parceiros
    parceiros.append(novo_parceiro)

    os.system("cls")
    print(f"\nSeja bem-vindo, {nome}!!! Cadastro realizado com sucesso! Por favor, faça login para continuar.\n")

def login(tipo):
    print("\nDigite suas credenciais")
    email_login = input("E-mail: ")
    senha_login = input("Senha: ")
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
        nome_atividade = input("\nNome da atividade: ").strip()

        # Validação da data
        while True:
            data_atividade = input("Data da atividade (dd/mm/aaaa): ").strip()
            data = validar_data(data_atividade)
            if data:
                ano = data.year
                mes = data.month
                ano_atual = datetime.now().year
                mes_atual = datetime.now().month
                
                if ano < ano_atual:
                    print("Ano inválido. O ano já passou.")
                elif ano == ano_atual and mes < mes_atual:
                    print("Mês inválido. O mês já passou.")
                elif ano > ano_atual + 2:
                    print("Ano inválido. A data está muito distante. (Só estamos aceitando atividades até o ano de 2026, por enquanto)")
                else:
                    break
            else:
                print("Data inválida. Por favor, insira uma data no formato dd/mm/aaaa.")

        descricao_atividade = input("Descrição da atividade: ").strip()
        local = input("Local da atividade: ").strip()

        while True:
            vagas = input("Número de vagas: ").strip()
            if vagas.isnumeric():
                vagas = int(vagas)  # Converter para inteiro
                if vagas == 0:
                    print("0 vagas? Adicione alguma vaga, por favor")
                else:
                    break
            else:
                print("ERRO! Digite um número, por favor!")
        
        # Validação do horário
        while True:
            horario = input("Horário da atividade (hh:mm - hh:mm): ").strip()
            if validar_horario(horario):
                break
            else:
                print("Horário inválido. Por favor, insira no formato hh:mm - hh:mm.")
        
        
        # Gerar um ID único para a atividade
        id_atividade = len(atividades) + 1
        
        # Adicionar a atividade ao dicionário de atividades
        nova_atividade = {
            "id_atividade": id_atividade,
            "nome_atividade": nome_atividade,
            "data_atividade": data_atividade,
            "descricao_atividade": descricao_atividade,
            "vagas": vagas,
            "local": local,
            "horario": horario,
            "id_ong": id_ong
        }
        
         # Adicionar a nova atividade à lista de atividades
        atividades.append(nova_atividade)

        # Perguntar se deseja adicionar outra atividade
        continuar = input("Deseja cadastrar outra atividade? (s/n): ").strip().lower()
        if continuar != 's':
            print("")
            break


def visualizar_atividade(atividades, id_ong):
    # Filtrar atividades pela ID da ONG
    atividades_filtradas = [atividade for atividade in atividades if atividade["id_ong"] == id_ong]
    
    # Verificar se há atividades para a ONG especificada
    if not atividades_filtradas:
        print("Não há atividades disponíveis no momento.")
        return
    
    # Exibir as atividades filtradas
    for i, atividade in enumerate(atividades_filtradas):
        print(f"{i + 1}. Atividade: (ID: {atividade['id_atividade']}) {atividade['nome_atividade']}, "
              f"Descrição: {atividade['descricao_atividade']}, Data: {atividade['data_atividade']}, "
              f"Local: {atividade['local']}, Horário: {atividade['horario']}, Vagas: {atividade['vagas']}")

def exibir_perfil_ong(ongs, id_ong):
    # Percorrer a lista de ONGs para encontrar a ONG com o ID especificado
    for ong in ongs:
        if ong["id"] == id_ong:
            # Exibir os detalhes da ONG
            print(f"Seu perfil, {ong['nome']} (ID: {ong['id']}):")
            print(f"CNPJ: {ong['cnpj']} | Descrição: {ong['descricao']} | E-mail: {ong['email']}")
            return

    # Se nenhuma ONG for encontrada com o ID especificado
    print("ONG não encontrada.")

#FUNÇÕES DO VOLUNTÁRIO
def visualizar_atividadesUsuario(atividades):
     for i, atividade in enumerate(atividades):
        print(f"{i + 1}. Atividade: (ID: {atividade['id_atividade']}) {atividade['nome_atividade']}, (OFERECIDA PELA ONG: {atividade[id_ong]}) "
              f"Descrição: {atividade['descricao_atividade']}, Data: {atividade['data_atividade']}, "
              f"Local: {atividade['local']}, Horário: {atividade['horario']}, Vagas: {atividade['vagas']}")
        
def exibir_perfil_voluntario(voluntario, id_voluntario):
    # Percorrer a lista de Parceiros para encontrar o parceiro com o ID especificado
    for voluntarios in voluntario:
        if voluntarios["id"] == id_voluntario:
            # Exibir os detalhes do voluntario
            print(f"Seu perfil, {voluntarios['nome']} (ID: {voluntarios['id']}) | E-mail: {voluntarios['email']}")
            return

    # Se nenhum voluntario for encontrado com o ID especificado
    print("Voluntário não encontrada.") 

def visualizar_cupons(cupons):
    if not cupons:
        print("*********Nenhum cupom disponível no momento.*********")
        return
    print("Cupons disponiveis no momento: \n")
    # Exibir o cupom
    for i, cupom in enumerate(cupons):
        print(f"\nDesconto oferecido por: {cupom['nome']}, {cupom['porcentagem_desconto']}% -> Cupom: (codigo: {cupom['codigo']}), "
              f"Valor mínimo para ter o desconto: {cupom['valor_minimo']}, Desconto em reais: R${cupom['desconto']}, ")

def abrir_github(link):
    if "github.com" in link:
        webbrowser.open(link)
    else:
        print("O link fornecido não é um link do GitHub.")

#FUNÇÕES DOS PARCEIROS
def cadastrar_cupom(cupons, id_parceiro, razao_parceiro):
    # Filtrar cupons pelo id_parceiro
    existe_cupom = [cupom for cupom in cupons if cupom["id_parceiro"] == id_parceiro]
    
    # Verificar se já existe cupom para esse Parceiro
    # lembrando, que o parceiro só pode cadastrar 1 cupom em nosso sistema, por isso a validação
    if existe_cupom:
        print(f"{razao_parceiro}, vocês já cadastraram um cupom, e segundo nossas diretrizes, só aceitamos um cupom de cada parceiro.")
        return

    print("\nCadastro do cupom:")
    while True:
        desconto = input("Digite o valor do desconto em reais (XX0.XX/100.50): ")
        if(isfloat(desconto)):
            desconto = float(desconto)
            break
        else:
            print("Valor inválido. Tente novamente.")

    while True:
        valor_minimo = input("Digite o valor mínimo da compra para aplicar o cupom (XX0.XX/100.50): ")
        if(isfloat(valor_minimo)):
            valor_minimo = float(valor_minimo)
            break
        else:
            print("Valor inválido. Tente novamente.")
            
    # Calcular a porcentagem de desconto
    porcentagem_desconto = (desconto / valor_minimo) * 100
    porcentagem_desconto = round(porcentagem_desconto)

    codigo ="{}{}%OFF".format(razao_parceiro.upper(), porcentagem_desconto)
            
    novo_cupom = {
        'codigo': codigo,
        'desconto': desconto,
        'valor_minimo': valor_minimo,
        'porcentagem_desconto': porcentagem_desconto,
        'id_parceiro': id_parceiro
    }
            
    cupons.append(novo_cupom)

    print(f"Cupom: {codigo} cadastrado com sucesso!!")
    # return novo_cupom  # Retorna o novo cupom cadastrado

def visualizar_cupomParceiro(cupons, id_parceiro, razao_social):
     # Filtrar cupom
    existe_cupom = [cupom for cupom in cupons if cupom["id_parceiro"] == id_parceiro]
    
    # Verificar se há atividades para a ONG especificada
    if not existe_cupom:
        print("Não há cupom, no momento.")
        return
    
    # Exibir o cupom
    for i, cupom in enumerate(existe_cupom):
        print(f"\nDesconto oferecido por: {razao_social}, {cupom['porcentagem_desconto']}% -> Cupom: (codigo: {cupom['codigo']}), "
              f"Valor mínimo: {cupom['valor_minimo']}, Desconto em reais: R${cupom['desconto']}, ")

def exibir_perfil_parceiro(parceiro, id_parceiro):
    # Percorrer a lista de Parceiros para encontrar o parceiro com o ID especificado
    for parceiros in parceiro:
        if parceiros["id"] == id_parceiro:
            # Exibir os detalhes do parceiro
            print(f"Seu perfil, {parceiros['nome']} (ID: {parceiros['id']}) | E-mail: {parceiros['email']}")
            return

    # Se nenhum parceiro for encontrado com o ID especificado
    print("Parceiro não encontrado.")     