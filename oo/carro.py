import doctest

class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def velocidade_instantanea(self):
        return self.velocidade

motor = Motor(0)

motor.acelerar()

print(motor.velocidade_instantanea())


'''
Criando uma classe carro que vai prossuir dois atributos compostos por outras duas classes:
1) Motor
2) Direção

O motor terá a responsabilidade de controlar a velocidade. Ele oferece os seguintes atribuitos:
1) Atributo de dado velocidade
2) Método acelerar, que deverá incrementar a velocidade de uma unidade
3) Método frear que deverá decrementar a velocidade em duas unidades

A direção terá a responsabilidade de controlar a direção. Ela oferece os seguintes atribuitos:
1) Valores de direção com valores possíveis: Norte, Sul, Leste, Oeste.
2) Método girar_a_direita
3) Método girar_a_esquerda

Exemplo:
# testando motor
motor = Motor()
motor.velocidade
0
motor.acelerar()
motor.velocidade
1
motor.acelerar()
motor.velocidade
2
motor.frear()
motor.velocidade /decrementa 2
0

Testando Direcao
direcao = Direcao()
direcao.valor
'Norte'

direcao.girar_a_direita()
direcao.valor
'Leste'

direcao.girar_a_direita()
direcao.valor
'Sul'

direcao.girar_a_direita()
direcao.valor
'Oeste'

direcao.girar_a_direita()
direcao.valor
'Norte'

direcao.girar_a_esquerda()
direcao.valor
'Oeste'

direcao.girar_a_esquerda()
direcao.valor
'Sul'

direcao.girar_a_esquerda()
direcao.valor
'Leste'

direcao.girar_a_esquerda()
direcao.valor
'Norte'

carro = Carro(direcao, motor)
carro.calcular_velocidade()
0
carro.acelerar()
carro.calcular_velocidade()
1
carro.acelerar()
carro.calcular_velocidade()
2
carro.frear()
carro.calcular_velocidade()
0



'''