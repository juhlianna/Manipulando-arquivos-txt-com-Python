#Lendo o arquivo TXT
with open('EXTRATO2023.txt', 'r') as file_entrada:
    data = file_entrada.readlines()

    #Payload de string vazia
    payload = ""

    #Leia todas as linhas do arquivo e multiplique
    payload = data * 2 

    result = "".join(payload)

#Abra o arquivo de saída em modo de escrita com o resultado
with open('EXTRATO2023Mod.txt', 'w') as file_saida:

    #Escreva o resultado no arquivo de saída
    file_saida.writelines(result)

#Resultado
print(result)
