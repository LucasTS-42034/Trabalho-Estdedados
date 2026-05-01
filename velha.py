def tabu(tab):
    print(f"\n {tab[0]} | {tab[1]} | {tab[2]} ")
    print("---+---+---")
    print(f" {tab[3]} | {tab[4]} | {tab[5]} ")
    print("---+---+---")
    print(f" {tab[6]} | {tab[7]} | {tab[8]} \n")


def vitoria(tab, joga):
    for i in range(0, 9, 3):
        if tab[i] == tab[i+1] == tab[i+2] == joga:
            return True
    for i in range(3):
        if tab[i] == tab[i+3] == tab[i+6] == joga:
            return True
    if tab[0] == tab[4] == tab[8] == joga:
        return True
    if tab[2] == tab[4] == tab[6] == joga:
        return True
    return False


def pvp():
    
    tab = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    
    sim1 = input("X ou O? \n").upper()
    sim2 = 0
    if sim1 == "X":
        sim2 = "O"
    elif sim1 == "O":
        sim2 = "X"
    else:
        print("Escolha inválida! Será usado X.")
        sim1 = "X"
        sim2 = "O"
    
    print("Jogador 1: " + sim1)
    print("Jogador 2: " + sim2)
    
    joga = sim1     
    rodadas = 0     
    
    
    while rodadas < 9:
        tabu(tab)
        print(f"Vez do jogador {joga}:")
        
        try:
            vez = int(input("Digite a posição que quer jogar (de 1-9): \n")) - 1
            
            if vez < 0 or vez > 8:
                print("Posição inválida! Escolha entre 1 e 9.")
                continue
                
            if tab[vez] in ["X", "O"]:
                print("Posição já ocupada!")
                continue
            
            tab[vez] = joga
            rodadas += 1
            
            if vitoria(tab, joga):
                tabu(tab)
                print(f"Jogador {joga} venceu! 🎉")
                return
            
            if joga == sim1:
                joga = sim2
            else:
                joga = sim1
                
        except ValueError:
            print("Digite um número válido!")
    
    tabu(tab)
    print("Empate!")



print("---- Jogo da velha ----")
while True:
    print("\n Escolha: ")
    print("1 - PVP (Player vs Player)")
    print("2 - PVE (Player vs computador)")
    print("3 - Encerrar")
    
    opcao = input("Faça sua escolha: \n")
    if opcao == "3":
        print("Até logo!")
        break
    elif opcao == "1":
        pvp()
    elif opcao == "2":
        print("Modo PVE")
    else:
        print("Opção inválida!")
        
#----------------------------------------------

tabuleiro = [" " for _ in range(9)]

def mostrar_tabuleiro():
    print(f"""
 {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}
-----------
 {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}
-----------
 {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}
""")

def verificar_vencedor(jogador):
    combinacoes = [
        [0,1,2],[3,4,5],[6,7,8],  # linhas
        [0,3,6],[1,4,7],[2,5,8],  # colunas
        [0,4,8],[2,4,6]           # diagonais
    ]
    for c in combinacoes:
        if tabuleiro[c[0]] == tabuleiro[c[1]] == tabuleiro[c[2]] == jogador:
            return True
    return False

def jogadas_disponiveis():
    return [i for i in range(9) if tabuleiro[i] == " "]

import random

def jogada_maquina():
    pos = random.choice(jogadas_disponiveis())
    tabuleiro[pos] = "O"

def jogo():
    while True:
        mostrar_tabuleiro()
        
        # Jogador
        jogada = int(input("Escolha uma posição (0 a 8): "))
        if tabuleiro[jogada] != " ":
            print("Posição ocupada!")
            continue
        
        tabuleiro[jogada] = "X"
        
        if verificar_vencedor("X"):
            mostrar_tabuleiro()
            print("Você venceu!")
            break
        
        if not jogadas_disponiveis():
            mostrar_tabuleiro()
            print("Empate!")
            break
        
        # Máquina
        jogada_maquina()
        
        if verificar_vencedor("O"):
            mostrar_tabuleiro()
            print("A máquina venceu!")
            break
        
        if not jogadas_disponiveis():
            mostrar_tabuleiro()
            print("Empate!")
            break

# Iniciar jogo
jogo()
