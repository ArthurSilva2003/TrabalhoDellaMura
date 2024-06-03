# Simulador de Automatos Finitos

## Funcionamento
<p>Este código implementa uma simulação de autômato finito, onde utiliza dados de transições, estados iniciais e finais de um arquivo JSON, e palavras de um arquivo CSV para determinar se as palavras são aceitas pelo autômato.</p>

## Instruções de Uso

<p>Para executar o código, use a linha de comando, passando dois argumentos: o caminho do arquivo JSON e o caminho do arquivo CSV.</p>

 $ python nome_do_script.py caminho_para_arquivo_json caminho_para_arquivo_csv

## Funcionamento

## Importação de Módulos Necessários

  import json
  import sys
  import csv

## Leitura da Linha de Comando
  $argvs = sys.argv
$arquivo1 = argvs[1]
$arquivo2 = argvs[2]

## Leitura do Arquivo JSON
  <p>O arquivo JSON contém a definição do autômato: estado inicial, estados finais e transições.</p>
  $with open(arquivo1, 'r') as dados:
    arq_json = json.load(dados)

##Leitura do Arquivo CSV
  <p>O arquivo CSV contém as palavras que serão verificadas pelo autômato.</p>

  $entradas = []
with open(arquivo2, "r") as csvfile:
    $arq_csv = csv.reader(csvfile, delimiter=";")
    for linha in arq_csv:
        entradas.append(linha[0])

## Conversão das Palavras em Listas
  <p>Cada palavra do CSV é transformada em uma lista de suas letras.</p>

  $lista_de_entradas = []
for palavra in entradas:
    lista_letras = list(palavra)
    lista_de_entradas.append(lista_letras)

## Simulação do Autômato
  <p>Para cada palavra, o código percorre suas letras, utilizando as transições que foram definidas no JSON para determinar o estado final.
</p>

   initial_state = arq_json["initial"]
  final_states = arq_json["final"]
transitions = arq_json["transitions"]

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

## Exemplo de Arquivo JSON

<p>Um exemplo de arquivo JSON pode ser o seguinte:</p>
 
  {
    "initial": "q0",
    "final": ["q2"],
    "transitions": [
        {"from": "q0", "read": "a", "to": "q1"},
        {"from": "q1", "read": "b", "to": "q2"},
        {"from": "q2", "read": "a", "to": "q0"}
    ]
}

## Considerações Finais

<p>Este código é útil para testar a aceitação de palavras por um autômato finito definido em um arquivo JSON. A saída do código indicará, para cada palavra, se ela é aceita ou não pelo autômato.</p>
