# Implementar o método de decodificação para o algoritmo de frequência de caracteres.

def compress(decodificacao):
    dict_size = 256
    dicionario = dict((chr(i), i) for i in range(dict_size))

    w = ""
    resultado = []
    for c in decodificacao:
        wc = w + c
        if wc in dicionario:
            w = wc
        else:
            resultado.append(dicionario[w])
            dicionario[wc] = dict_size
            dict_size += 1
            w = c

    if w:
        resultado.append(dicionario[w])
    return resultado

def decompress(codificacao):
    from io import StringIO
    dict_size = 256
    dicionario = dict((i, chr(i)) for i in range(dict_size))

    resultado = StringIO()
    w = chr(codificacao.pop(0))
    resultado.write(w)
    for k in codificacao:
        if k in dicionario:
            entrada = dicionario[k]
        elif k == dict_size:
            entrada = w + w[0]
        else:
            raise ValueError('Ruim codificacao k: %s' % k)
        resultado.write(entrada)

        dicionario[dict_size] = w + entrada[0]
        dict_size += 1

        w = entrada
    return resultado.getvalue()

codificacao = compress(str(input('Digite algo: ')))
print(codificacao)
print(len(codificacao))

decodificacao = decompress(codificacao)
print(decodificacao)
print(len(decodificacao))
