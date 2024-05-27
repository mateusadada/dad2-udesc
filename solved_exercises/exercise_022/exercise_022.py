# Desenvolver um código de lista invertida básica.

textos = [
    'To do is to be. To be is to do.',
    'To be or not to be.',
    'I think therefore I am. Do be do be do.',
    'Do do do, da da da. Let it be, let it be.'
]

def processar_texto(texto):
    pontuacoes = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    texto = texto.lower()
    for p in pontuacoes:
        texto = texto.replace(p, '')
    return texto

lista_invertida = {}

for indice, texto in enumerate(textos, 1):
    texto = processar_texto(texto)
    palavras = texto.split()
    
    # contar a frequência de cada palavra
    for palavra in palavras:
        if palavra not in lista_invertida:
            lista_invertida[palavra] = {}
        if indice not in lista_invertida[palavra]:
            lista_invertida[palavra][indice] = 0
        lista_invertida[palavra][indice] += 1

# construir a saída
saida = []
for palavra in lista_invertida:
    ocorrencias = lista_invertida[palavra]
    num_frases = len(ocorrencias)
    
    contagens_frases = []
    for k, v in sorted(ocorrencias.items()):
        contagens_frases.append(f"[{k}, {v}]")
    contagens_frases_str = ", ".join(contagens_frases)
    
    saida.append(f"{palavra} - n: {num_frases} {contagens_frases_str}")

# exibir a saída
for linha in saida:
    print(linha)
