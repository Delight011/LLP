numero = 1500

while numero <= 2700:
    if numero % 35 == 0:  # Verifica se é divisível por 5 e 7 ao mesmo tempo
        print(f"O primeiro número divisível por 5 e 7 entre 1500 e 2700 é: {numero}")
        break  # Encerra o loop quando o número é encontrado
    numero += 1
#Identifique a operação comum dos números em que estamos interessados. 
#No caso, eles devem ser divisíveis por 5 e 7, então o menor múltiplo comum desses dois números é 35. Use este conhecimento para simplificar a condição no loop. Em vez de verificar individualmente se o número é divisível por 5 e por 7, verifique se é divisível por 35.
#Ao encontrar o número desejado, não há necessidade de continuar o loop. Então, use break para sair do loop assim que o número for encontrado.