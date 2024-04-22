class Cifra(object):
    plain_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    plain_alphanum = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

    def format_str(self, text):
        return text.replace(' ', '').upper()

    def shift_alphabet(self, alphabet, shift):
        return alphabet[shift:] + alphabet[:shift]

    def create_quadrado(self, key = '', alphanum = False, replace = ['J', 'I'], sequence = False):
        quadrado = []
        if alphanum:
            num = 6
            alfabeto = self.plain_alphanum
            replace = ['', '']
        else:
            num = 5
            alfabeto = self.plain_alphabet
        alfabeto = self.create_alphabet(key, alfabeto, replace, sequence)
        for idx in range(0, len(alfabeto), num):
            quadrado.append(alfabeto[idx:idx + num])
        return quadrado

    def create_alphabet(self, key = '', alfabeto = plain_alphabet, replace = ['', ''], sequence = False):
        if key:
            key = key.upper()
            temp = ''
            for ch in key:
                if ch not in temp:
                    temp += ch
            key = temp
            if replace[0] in key:
                key = key.replace(replace[0], replace[1])
            if sequence:
                idx = alfabeto.index(key[-1])
                alfabeto = self.shift_alphabet(alfabeto, idx)
        cifra = alfabeto.replace(replace[0], '')
        for ch_key in key:
            if ch_key in cifra:
                cifra = cifra.replace(ch_key, '')
        return key + cifra
