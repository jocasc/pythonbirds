class Pessoa:
    olhos = 2

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
    joelson.sobrenome = 'Cabral' # atributo dinâmico -> não é uma boa prática
    del joelson.filhos # excluindo um atributo -> também não é uma boa prática
    print(joelson.__dict__)  # dunder responsável por exibir os atributos de instância
    print(levi.__dict__)
    Pessoa.olhos = 3
    print(f'Valor de olhos {Pessoa.olhos}')
    print(f'Olhos de Lévi {levi.olhos}')
    print(id(Pessoa.olhos), id(levi.olhos), id(joelson.olhos))

#    for filho in joelson.filhos:
#        print(filho.nome)
