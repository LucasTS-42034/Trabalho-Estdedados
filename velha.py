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
        tabuleiro = [[0], [0], [0], 
                     [0], [0], [0], 
                     [0], [0], [0]]
        sim1 = input("X ou O? \n").upper()
        sim2 = 0
        if sim1 == "X":
            sim2 = "O"
        elif sim1 == "O":
            sim2 = "X"
        
        for i in range(9):
            print(tabuleiro[0:3]) 
            print(tabuleiro[3:6]) 
            print(tabuleiro[6:9])            
            jogada = int(input("Digite onde quer jogar: \n"))
