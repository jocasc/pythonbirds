class Pessoa:

    def __init__(self, *filhos, nome = None, idade = 43):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    levi = Pessoa(nome='Lévi')
    joelson  = Pessoa(levi, nome='Joelson')
    print(Pessoa.cumprimentar(joelson))
    print(id(joelson))
    print(joelson.cumprimentar())
    print(joelson.nome)
    print(joelson.idade)

    for filho in joelson.filhos:
        print(filho.nome)
