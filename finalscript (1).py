import time

grille = [[0 for x in range(7)] for y in range(6)]
def Spawntab(grille):
    for i in grille:
            print(i)

player1 = 1
player2 = 2
def partie():
    print('Bienvenue dans cette partie de puissance 4 version python, mes chers joueurs 1 et 2 !')
    time.sleep(3)
    print('Le propriétaire de ce pc sera le joueur 1, et son pion sera défini comme un "1"!')
    time.sleep(1)
    print('Le second joueur, lui, aura droit à un magnifique "2" !! ')
    time.sleep(1)
    a = str(input('Compris ?(Répondez Oui/Non)'))
    if a == "Oui":
        print('Bien, alors commençons !')
    elif a == "Non":
        print('Eh bien, tant pis pour vous, on commence !')
    else :
        print('Je ne comprends rien à se que vous dites, mais vous devez avoir compris !')
    time.sleep(4)
    print('Commençons sans plus tarder ! Joueur 1, par quelle colonne allez vous commencer ?')
    line = int(input('Alors ?'))
    column = 5
    grille[column][line] = player1
    Spawntab(grille)
    print('Bien, à toi, deuxième joueur !')
    time.sleep(1)
    column = 5
    
    while column >= 0 and column >= 5:
        line = int(input("Alors ? (Si vous avez déja placé un pion et que ce message apparait, c'est que l'emplacement du jeton est mauvais ! "))
        if line >6 or line <0:
            print("Cette ligne n'est pas correcte !")
        
        if grille[column][line] == 0 and column == 5:
            grille[column][line] = player2
            break
        
        elif grille[column][line] == 1 and grille[column-1][line] == 0 :
            grille[column-1][line] = player2
            break
        
        elif grille[column][line] == 1 and grille[column-1][line] == 1  and  grille[column-2][line] == 0 :
            grille[column-2][line] = player2
            break
        
        elif grille[column][line] == 1 and grille[column-1][line] == 1  and  grille[column-2][line] == 1 and grille[column-3][line] == 0:
            grille[column-3][line] = player2
            break
        
        elif grille[column][line] == 1 and grille[column-1][line] == 1  and  grille[column-2][line] == 1 and grille[column-3][line] ==1 and grille[column-4][line] == 0:
            grille[column-4][line] = player2
            break
        
        elif grille[column][line] == 1 and grille[column-1][line] == 1  and  grille[column-2][line] == 1 and grille[column-3][line] ==1 and grille[column-4][line] == 1 and grille[column-5][line] == 0:
            grille[column-5][line] = player2
            break
    Spawntab(grille)

    for i in range(20):
        time.sleep(2)
        column = 5
        line = int(input(" Joueur 1, sélectionnez votre colonne !(Si vous avez déja placé un pion ce tour-si et que ce message apparait, c'est que la colonne choisie est remplie ! "))
        if (grille[0][line] == 1 or grille[0][line] ==2):
            print("Cette colonne est pas correcte !")
        
        elif line >6 or line <0:
            print("Cette ligne n'est pas correcte !")
        
        elif grille[column][line] == 0 and column == 5:  #(A1 or A2) and A3
            grille[column][line] = player1
        
        elif (grille[column][line] == 1 or grille[column][line] ==2) and grille[column-1][line] == 0 :
            grille[column-1][line] = player1
        
        elif (grille[column][line] == 1 or grille[column][line] == 2) and (grille[column-1][line] == 1 or grille[column-1][line] == 2) and  grille[column-2][line] == 0 :
            grille[column-2][line] = player1
        
        elif (grille[column][line] == 1 or grille[column][line] ==2) and (grille[column-1][line] == 1 or grille[column-1][line] == 2)  and  (grille[column-2][line] == 1 or grille[column-2][line] == 2)and grille[column-3][line] == 0:
            grille[column-3][line] = player1
        
        elif (grille[column][line] == 1 or grille[column][line] ==2) and (grille[column-1][line] == 1 or grille[column-1][line] ==2)  and  (grille[column-2][line] == 1 or grille[column-2][line]==2) and (grille[column-3][line] ==1 or grille[column-3][line]==2) and grille[column-4][line] == 0:
            grille[column-4][line] = player1
        
        elif (grille[column][line] == 1 or grille[column][line] ==2) and (grille[column-1][line] == 1 or grille[column-1][line] == 2)  and  (grille[column-2][line] == 1 or grille[column-2][line] == 2) and (grille[column-3][line] ==1 or grille[column-3][line] == 2) and (grille[column-4][line] == 1 or grille[column-4][line] == 2) and grille[column-5][line] == 0:
            grille[column-5][line] = player1
        Spawntab(grille)
        winner = wincondition(grille, player1, player2)
        if winner in (win1, win2, win3, win4, win5, win6):
            print(winner)
            break
        time.sleep(2)
        column = 5
        
        line = int(input(" Quelle colonne choisissez vous, joueur 2 ?(Si vous avez déja placé un pion ce tour-si et que ce message apparait, c'est que la colonne choisie est remplie ! "))
        if (grille[0][line] == 1 or grille[0][line] ==2):
            print("Cette colonne est pas correcte !")
        
        elif line >6 or line <0:
            print("Cette ligne n'est pas correcte !")
        
        elif grille[column][line] == 0 and column == 5:  #(A1 or A2) and A3
            grille[column][line] = player2
        
        elif (grille[column][line] == 1 or grille[column][line] ==2) and grille[column-1][line] == 0 :
            grille[column-1][line] = player2
        
        elif (grille[column][line] == 1 or grille[column][line] == 2) and (grille[column-1][line] == 1 or grille[column-1][line] == 2) and  grille[column-2][line] == 0 :
            grille[column-2][line] = player2
        
        elif (grille[column][line] == 1 or grille[column][line] ==2) and (grille[column-1][line] == 1 or grille[column-1][line] == 2)  and  (grille[column-2][line] == 1 or grille[column-2][line] == 2)and grille[column-3][line] == 0:
            grille[column-3][line] = player2
        
        elif (grille[column][line] == 1 or grille[column][line] ==2) and (grille[column-1][line] == 1 or grille[column-1][line] ==2)  and  (grille[column-2][line] == 1 or grille[column-2][line]==2) and (grille[column-3][line] ==1 or grille[column-3][line]==2) and grille[column-4][line] == 0:
            grille[column-4][line] = player2
        
        elif (grille[column][line] == 1 or grille[column][line] ==2) and (grille[column-1][line] == 1 or grille[column-1][line] == 2)  and  (grille[column-2][line] == 1 or grille[column-2][line] == 2) and (grille[column-3][line] ==1 or grille[column-3][line] == 2) and (grille[column-4][line] == 1 or grille[column-4][line] == 2) and grille[column-5][line] == 0:
            grille[column-5][line] = player2
        Spawntab(grille)
        winner = wincondition(grille, player1, player2)
        if winner in (win1, win2, win3, win4, win5, win6):
            print(winner)
            break
        
    time.sleep(2)
    print("Merci d'avoir utilisé ce puissance 4 v.Python !")
    time.sleep(1)
    print("Et n'oubliez pas de faire ctrl+A et relancer le programme pour refresh le tableau !")


def wincondition(grille, player1, player2):
 #horizontale
    for i in range(6):
        for j in range(4):
            if grille[i][j] == player1 and grille[i][j+1] == player1 and grille[i][j+2] == player1 and grille[i][j+3] == player1:
                return win1
            elif grille[i][j] == player2 and grille[i][j+1] == player2 and grille[i][j+2] == player2 and grille[i][j+3] == player2:
                return win2
    #verticales
    for i in range(7):
        for j in range(3):
            if grille[j][i] == player1 and grille[j+1][i] == player1 and grille[j+2][i] == player1 and grille[j+3][i] == player1:
                return win3
            elif grille[j][i] == player2 and grille[j+1][i] == player2 and grille[j+2][i] == player2 and grille[j+3][i] == player2:
                return win4
    #diagonale
    for i in range(3):
        for j in range(4):
            if grille[i][j] == player1 and grille[i+1][j+1] == player1 and grille[i+2][j+2] == player1 and grille[i+3][j+3] == player1:
                return win5
            elif grille[i][j+3] == player1 and grille[i+1][j+2] == player1 and grille[i+2][j+1] == player1 and grille[i+3][j] == player1:
                return win5
            elif grille[i][j] == player2 and grille[i+1][j+1] == player2 and grille[i+2][j+2] == player2 and grille[i+3][j+3] == player2:
                return win6
            elif grille[i][j+3] == player2 and grille[i+1][j+2] == player2 and grille[i+2][j+1] == player2 and grille[i+3][j] == player2:
                return win6
        if grille[0][0] == grille[0][1] and grille[0][1] == grille[0][2] and grille[0][2] == grille[0][3] and grille[0][3] == grille[0][4] and grille[0][4] == grille[0][5] and grille[0][5]  and grille[0][5] == grille[0][6] and grille[0][6] == 1 or grille[0][6] == 2:
            return win7
    return win0




win0 = "Aucun gagnant ce tour-si..."
win1 = 'Félicitation, le joueur 1 a remporté la partie, avec une magnifique ligne de 1 horizontale !'
win2 = 'Félicitation, le joueur 2 a remporté la partie, avec une magnifique ligne de 2 horizontale !'
win3 = 'Félicitation, le joueur 1 a remporté la partie, avec une magnifique ligne de 1 verticale !'
win4 = 'Félicitation, le joueur 2 a remporté la partie, avec une magnifique ligne de 2 verticale !'
win5 = 'Félicitation, le joueur 1 a remporté la partie, avec une magnifique ligne de 1 en diagonale !'
win6 = 'Félicitation, le joueur 2 a remporté la partie, avec une magnifique ligne de 2 en diagonale !'
win7 = 'Match nul, bravo à vous deux !'