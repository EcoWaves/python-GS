# participantes
# Laura (RM: 558843) | Maria Eduarda (RM: 558832) | Vínicius Saes (RM: 554456)

# importações
import os

from datetime import datetime
from funcoes import *

#----------------------------------------------------------------------- PROGRAMA PRINCIPAL

# Menu para interagir com o usuário


print("				\t\tTELA INICIAL ECOWAVES")
print("			\tQual você se encaixa -> 1 - Voluntario | 2 - ONG | 3 - Parceiros")
opcaoUser = input(" ")
while True:
    if opcaoUser == "":
        print("Você precisa digitar uma opção válida!")
        opcaoUser = input("Digite a opção desejada: ")
    elif opcaoUser == "1" or opcaoUser == "2" or opcaoUser == "3":
        break
    else:
        print("Você precisa digitar uma opção válida!")
        opcaoUser = input("Digite a opção desejada: ")

print("\nLegal! E você deseja:")
opcaoEntrada = input("[1] - cadastrar-se | [2] - Login | [3] - sair do sistema ->  ")

match(opcaoEntrada):
    case "1":
        if(opcaoUser == "1"):
            cadastrar_voluntario()
            voluntario_logado = login(opcaoUser)
            if voluntario_logado: 
                nome_usuario_logado = voluntario_logado['nome']

                os.system("cls")
                print(f"\nLogin realizado com sucesso, {nome_usuario_logado}! Você agora está logado em sua conta\n")
                id_voluntario = voluntario_logado['id']

                while True:
                    opcao = input(f"\n0 - Sair | 1- Sobre nós | 2 - EcoVoluntariado | 3- Seu Perfil | 4- Descontos dos Parceiros\n")
                    match opcao:
                        case "0":
                            print("				\t\tAgradecemos por usar nosso sistema! Até a próxima")
                            break
                        case "1":
                            while True:
                                print("\nINTEGRANTES DO TIME:\n")
                                print("Laura Cintra. RM: 558843\nMaria Eduarda. RM:558832\nVínicius Saes. RM: 554456\n")
                                print("Juntos, somos um time dedicado a resolver os problemas da poluição dos oceanos, incentivando a colaboração da sociedade e promovendo o ecovoluntariado.\n")
                                opcao = input("DESEJA ACESSAR NOSSO REPOSITÓRIO NO GITHUB? 1-sim|2-não -> ")

                                if opcao == "1":
                                    link_github = "https://github.com/EcoWaves/python-GS.git"
                                    abrir_github(link_github)
                                    break
                                elif opcao == "2":
                                    print("Okay! Então, continue navegando! :)")
                                    break
                                else:
                                    print("hmm, não existe essa opção!")
                        case "2":
                            visualizar_atividadesUsuario(atividades)
                            # aqui adicionar a função para o usuário se increver nas atividades
                        case "3":
                            exibir_perfil_voluntario(voluntarios, id_voluntario)
                        case "4":
                            print("\nNós temos parcerias com hoteis e pousadas, que fornecem descontos para nossos usuários!")
                            print("Basta copiar o código e colar o código na página de nosso parceiro. E você terá o desconto estipulado.: \n")
                            visualizar_cupons(cupons)
                        case _:
                            print("Hmm, não existe essa opção!")
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
                id_ong = ong_logada['id']

                while True:
                    opcao = input(f"\n0 - Sair | 1- Registrar uma Atividade | 2 - Ver suas Atividades | 3- Seu Perfil\n")

                    # opcao1 = input(f"\0 - Sair | 1- Registrar uma Atividade | 2 - Ver suas Atividades | 3- Seu Perfil\n")
                    match opcao:
                        case "0":
                            print("				\t\tAgradecemos por usar nosso sistema! Até a próxima")
                            break
                        case "1":  
                            print("Cadastro da atividade:")
                            cadastrar_atividade(atividades,id_ong)
                        case "2":
                            visualizar_atividade(atividades,id_ong)
                            inscrever_atividade(opcaoUser)
                        case "3":
                            exibir_perfil_ong(ongs, id_ong)
                        case _:
                            print("Hmm, não existe essa opção!")
            else:
                os.system("cls")
                print("\nLogin ou senha incorretos. Tente novamente.")
                ong_logada = login(opcaoUser)
        elif(opcaoUser == "3"):
                cadastrar_parceiro()
                parceiro_logado = login(opcaoUser)
                if parceiro_logado: 
                    nome_parceiro_logado = parceiro_logado['nome']

                os.system("cls")
                print(f"\nLogin realizado com sucesso, {nome_parceiro_logado}! Você agora está logado em sua conta\n")
                id_parceiro= parceiro_logado['id']


                while True:
                    opcao = input(f"\n0 - Sair | 1- Registrar um Desconto | 2 - Ver desconto | 3- Seu Perfil\n")
                    match opcao:
                        case "0":
                            print("				\t\tAgradecemos por usar nosso sistema! Até a próxima")
                            break
                        case "1":
                            cadastrar_cupom(cupons, id_parceiro, nome_parceiro_logado)
                        case "2":
                            visualizar_cupomParceiro(cupons, id_parceiro, nome_parceiro_logado)
                        case "3":
                            exibir_perfil_parceiro(parceiros, id_parceiro)
                        case _:
                            print("Hmm, não existe essa opção!")
    case "2":
        print("\nLogin:")
        voluntario_logado = login(opcaoUser)
        if voluntario_logado: 
            nome_usuario_logado = voluntario_logado['nome']

            os.system("cls")
            print(f"\nLogin realizado com sucesso, {nome_usuario_logado}! Você agora está logado em sua conta\n")
            id_voluntario = voluntario_logado['id']

            while True:
                opcao = input(f"\n0 - Sair | 1- Sobre nós | 2 - EcoVoluntariado | 3- Seu Perfil | 4- Descontos dos Parceiros\n")
                match opcao:
                    case "0":
                        print("				\t\tAgradecemos por usar nosso sistema! Até a próxima")
                        break
                    case "1":
                        while True:
                            print("\nINTEGRANTES DO TIME:\n")
                            print("Laura Cintra. RM: 558843\nMaria Eduarda. RM:558832\nVínicius Saes. RM: 554456\n")
                            print("Juntos, somos um time dedicado a resolver os problemas da poluição dos oceanos, incentivando a colaboração da sociedade e promovendo o ecovoluntariado.\n")
                            opcao = input("DESEJA ACESSAR NOSSO REPOSITÓRIO NO GITHUB? 1-sim|2-não -> ")

                            if opcao == "1":
                                link_github = "https://github.com/EcoWaves/python-GS.git"
                                abrir_github(link_github)
                                break
                            elif opcao == "2":
                                print("Okay! Então, continue navegando! :)")
                                break
                            else:
                                print("hmm, não existe essa opção!")
                    case "2":
                        visualizar_atividadesUsuario(atividades)
                        inscrever_atividade(opcaoUser)
                    case "3":
                        exibir_perfil_voluntario(voluntarios, id_voluntario)
                    case "4":
                        print("\nNós temos parcerias com hoteis e pousadas, que fornecem descontos para nossos usuários!")
                        print("Basta copiar o código e colar o código na página de nosso parceiro. E você terá o desconto estipulado.: \n")
                        visualizar_cupons(cupons)
                    case _:
                        print("Hmm, não existe essa opção!")
        # usuario = login(opcaoUser)
        # if usuario:
        #     print(f"Bem-vindo, {usuario['nome']}!")
        # else:
        #     print("Email ou senha inválidos.")
        #     usuario = login(opcaoUser)
    case 3:
        print("				\t\tAgradecemos por usar nosso sistema! Até a próxima")
    case _:
        print("Hmmm, não existe essa opção!")     
            