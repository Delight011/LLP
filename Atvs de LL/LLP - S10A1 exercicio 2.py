import random

def jogo_advinhacao():
    numero_secreto = random.randint(1, 50)
    tentativas = 0 
    
    print("Bem-vindo ao jogo de adivinhação! Voçê tem 5 tentativas para adivinhar o número secreto entre 1 e 50.")
    
    while tentativas < 5:
    
     palpite = int(input("Tentativa {}: digite seu palpite: ".format(tentativas + 1)))
    
    if palpite == numero_secreto:
         print("Parabéns! Você acertou o número secreto.")
         return
    elif palpite < numero_secreto:
         print("O número secreto é maior. Tente novamente.")
    else:
         print("O número secreto é menor. Tente novamente.")
  
    tentativas += 1     

    print("Suas 5 tentativas acabaram! O numero secreto era:", numero_secreto)

jogo_advinhacao()

