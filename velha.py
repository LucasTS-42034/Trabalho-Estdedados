import random

# ========== FUNÇÕES BÁSICAS ==========
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


# ========== MODO PVP ==========
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


# ========== INTELIGÊNCIA DO COMPUTADOR (renomeada para jogapc) ==========
def jogapc(tab, sim_pc, sim_humano):
    """
    Estratégia:
    1. Vencer
    2. Bloquear
    3. Continuar linha própria
    4. Aleatório
    """
    linhas = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]

    # 1. Tentar vencer
    for linha in linhas:
        simpc = 0
        livre = None
        for i in linha:
            if tab[i] == sim_pc:
                simpc += 1
            elif tab[i] != "X" and tab[i] != "O":
                livre = i
        if simpc == 2 and livre != None:
            return livre

    # 2. Bloquear o jogador
    for linha in linhas:
        simjog = 0
        livre = None
        for i in linha:
            if tab[i] == sim_humano:
                simjog += 1
            elif tab[i] != "X" and tab[i] != "O":
                livre = i
        if simjog == 2 and livre != None:
            return livre

    # 3. Continuar uma linha que já tem peça do computador e nenhuma do jogador
    for linha in linhas:
        tem_pc = False
        tem_joga = False
        livre = None
        for i in linha:
            if tab[i] == sim_pc:
                tem_pc = True
            elif tab[i] == sim_humano:
                tem_joga = True
            elif tab[i] != "X" and tab[i] != "O":
                livre = i
        if tem_pc and (tem_joga == False) and livre != None:
            return livre

    # 4. Aleatório
    vazias = []
    for i in range(9):
        if tab[i] != "X" and tab[i] != "O":
            vazias.append(i)
    return random.choice(vazias)


# ========== MODO PVE ==========
def pve():
    tab = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    sim1 = input("Você quer X ou O? ").upper()
    if sim1 == "X":
        sim2 = "O"
    elif sim1 == "O":
        sim2 = "X"
    else:
        sim1 = "X"
        sim2 = "O"

    print("Você: " + sim1)
    print("Computador: " + sim2)

    joga = sim1      # Humano começa
    rodadas = 0

    while rodadas < 9:
        tabu(tab)

        if joga == sim1:
            print(f"Sua vez ({sim1}):")
            try:
                vez = int(input("Digite a posição (1-9): ")) - 1
                if vez < 0 or vez > 8:
                    print("Posição inválida!")
                    continue
                if tab[vez] == "X" or tab[vez] == "O":
                    print("Posição já ocupada!")
                    continue
            except ValueError:
                print("Digite um número!")
                continue
        else:
            print("O computador está pensando...")
            vez = jogapc(tab, sim2, sim1)   # ← chama a função renomeada

        tab[vez] = joga
        rodadas += 1

        if vitoria(tab, joga):
            tabu(tab)
            if joga == sim1:
                print("Você venceu! ")
            else:
                print("O computador venceu!")
            return

        # Alterna jogador
        if joga == sim1:
            joga = sim2
        else:
            joga = sim1

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
        pve()
    else:
        print("Opção inválida!")