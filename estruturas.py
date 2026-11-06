dados = []
tamanho = 0
tipo = 0 
inicio = 0    
fim = 0       
qtd = 0       


def criar(t):
    global dados, tamanho, tipo, inicio, fim, qtd
    n = int(input("Tamanho da estrutura: "))
    if n <= 0:
        print("Tamanho invalido.")
        return
    tamanho = n
    dados = [0] * tamanho
    tipo = t
    inicio = fim = qtd = 0
    print("Estrutura criada.")


def armazenar():
    global fim, qtd
    if qtd == tamanho or (tipo == 2 and fim == tamanho):
        print("Estrutura cheia!")
        return
    v = int(input("Valor: "))
    if tipo == 1:                      # push
        dados[qtd] = v
    elif tipo == 2:                    # enfileirar
        dados[fim] = v
        fim += 1
    else:                              # enfileirar circular
        dados[fim] = v
        fim = (fim + 1) % tamanho
    qtd += 1


def extrair():
    global inicio, qtd
    if qtd == 0:
        print("Estrutura vazia!")
        return
    if tipo == 1:                      # pop
        v = dados[qtd - 1]
    elif tipo == 2:                    # desenfileirar
        v = dados[inicio]
        inicio += 1
    else:                              # desenfileirar circular
        v = dados[inicio]
        inicio = (inicio + 1) % tamanho
    qtd -= 1
    print("Valor extraido:", v)


def imprimir():
    if qtd == 0:
        print("Estrutura vazia.")
        return
    print("Conteudo:", [dados[(inicio + i) % tamanho] for i in range(qtd)])



def bubble(v):
    n = len(v)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if v[j] > v[j + 1]:
                v[j], v[j + 1] = v[j + 1], v[j]


def selection(v):
    n = len(v)
    for i in range(n - 1):
        menor = i
        for j in range(i + 1, n):
            if v[j] < v[menor]:
                menor = j
        v[i], v[menor] = v[menor], v[i]


def insertion(v):
    for i in range(1, len(v)):
        chave = v[i]
        j = i - 1
        while j >= 0 and v[j] > chave:
            v[j + 1] = v[j]
            j -= 1
        v[j + 1] = chave


def ordenar(algoritmo):
    global inicio, fim
    if tipo == 0:
        print("Nenhuma estrutura criada! Escolha primeiro Pilha, Fila ou Fila Circular.")
        return
    
    v = [dados[(inicio + i) % tamanho] for i in range(qtd)]
    if algoritmo == 1:
        bubble(v)
    elif algoritmo == 2:
        selection(v)
    else:
        insertion(v)
    
    for i in range(qtd):
        dados[i] = v[i]
    if tipo != 1:
        inicio = 0
        fim = qtd % tamanho if tipo == 3 else qtd
    print("Ordenado!", end=" ")
    imprimir()




def menu_estrutura(t):
    nome = {1: "PILHA", 2: "FILA", 3: "FILA CIRCULAR"}[t]
    op = 0
    while op != 5:
        print("\n--- " + nome + " ---")
        print("1 - Criar estrutura\n2 - Armazenar valor\n3 - Extrair valor")
        print("4 - Imprimir conteudo\n5 - Voltar ao menu anterior")
        op = int(input("Opcao: "))
        if op == 1:
            criar(t)
        elif 2 <= op <= 4:
            if tipo != t:
                print("Crie primeiro esta estrutura (opcao 1).")
            elif op == 2:
                armazenar()
            elif op == 3:
                extrair()
            else:
                imprimir()


def menu_ordenar():
    op = 0
    while op != 4:
        print("\n--- ORDENAR ---")
        print("1 - Bubble Sort\n2 - Selection Sort\n3 - Insertion Sort\n4 - Voltar ao menu anterior")
        op = int(input("Opcao: "))
        if 1 <= op <= 3:
            ordenar(op)


op = 0
while op != 5:
    print("\n=== MENU PRINCIPAL ===")
    print("1 - PILHA\n2 - FILA\n3 - FILA CIRCULAR\n4 - ORDENAR\n5 - SAIR")
    op = int(input("Opcao: "))
    if 1 <= op <= 3:
        menu_estrutura(op)
    elif op == 4:
        menu_ordenar()
