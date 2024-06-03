import json
import sys
import csv

argvs = sys.argv
arquivo1 = argvs[1]
arquivo2 = argvs[2]
# arquivo3 = argvs[3]

# Abre o arquivo Json e lê os dados
with open(arquivo1, 'r') as dados:
    arq_json = json.load(dados)

# Lista para armazenar as strings da primeira coluna
entradas = []

# Abre o arquivo CSV e lê os dados
with open(arquivo2, "r") as csvfile:
    # Criamos o leitor CSV
    arq_csv = csv.reader(csvfile, delimiter=";")

    # Itera sobre as linhas do arquivo
    for linha in arq_csv:
        # Adiciona a primeira string da coluna à lista
        entradas.append(linha[0])

# Cria uma lista vazia que irá conter as listas de strings
lista_de_entradas = []

# Itera sobre cada palavra do vetor de strings
for palavra in entradas:
    # Separa cada letra da palavra e cria uma lista de strings
    lista_letras = list(palavra)

    # Adiciona a lista de strings à lista_de_listas
    lista_de_entradas.append(lista_letras)

# Exibe o resultado
# print(lista_de_entradas)

initial_state = arq_json["initial"]
final_states = arq_json["final"]
transitions = arq_json["transitions"]

# Agora, vamos percorrer letra por letra de cada palavra dentro das listas
for ler_lista in lista_de_entradas:
    atual_state = initial_state
    print("----------------------")

    for letra in ler_lista:

        for transition in transitions:
            from_state = transition["from"]
            read_symbol = transition["read"]
            to_state = transition["to"]

            if (from_state == atual_state):
                if (read_symbol == letra):
                    atual_state = to_state
                    print(atual_state)

    print("\n")
    valorFinal = 0
    for final in final_states:
        if (atual_state == final):
            valorFinal = 1
            print(1)
    if (valorFinal == 0):
        print(0)
