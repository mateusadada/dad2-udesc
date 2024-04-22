from cifra import Cifra

class Playfair(Cifra):
    def encrypt(self, texto, key='', descriptografar=False):
        cifra_texto = ''
        texto = texto.upper()
        texto = texto.replace('J', 'I').replace(' ', '')
        texto = self.check_double(texto)
        if len(texto) % 2:
            texto += 'W'
        self.square = self.create_quadrado(key)
        for i in range(0, len(texto), 2):
            cifra_texto += self.change_par(texto[i:i + 2], descriptografar)
        return cifra_texto.upper()

    def descriptografar(self, cifra_texto, key=''):
        return self.encrypt(cifra_texto.upper(), key, True).lower()

    def check_double(self, texto):
        out = ''
        for idx in range(0, len(texto), 2):
            par = texto[idx:idx + 2]
            if len(par) > 1 and par[0] == par[1]:
                out += par[0] + 'W' + par[1]
            else:
                out += par
        return out

    def change_par(self, par, descriptografar=False):
        if descriptografar:
            retorno = 4
            limite = -1
            passo = -1
        else:
            retorno = 0
            limite = 5
            passo = 1
        coord1, coord2 = self.coordenadas(par)
        if coord1[0] == coord2[0]:
            # caso em que as duas letras estao na mesma linha
            coord1[1] += passo
            coord2[1] += passo
        elif coord1[1] == coord2[1]:
            # caso em que as duas letras estao na mesma coluna
            coord1[0] += passo
            coord2[0] += passo
        else:
            # caso em que as duas letras nao estao na mesma linha nem mesma coluna
            coord1[1], coord2[1] = coord2[1], coord1[1]
        coord1 = [retorno if x == limite else x for x in coord1]
        coord2 = [retorno if x == limite else x for x in coord2]
        return self.letter(coord1) + self.letter(coord2)

    def coordenadas(self, par):
        coordenadas = []
        for letter in par:
            for line in range(len(self.square)):
                if letter in self.square[line]:
                    coordenadas.append([line, self.square[line].index(letter)])
                    break
        return coordenadas

    def letter(self, coord):
        return self.square[coord[0]][coord[1]]
