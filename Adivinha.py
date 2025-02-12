#Crie um jogo, o jogo terá dois modos.
#O primeiro: o jogador devera pensar em um numero e o computador devera adivinhar ele.
#O jogador que digitar ">" se o numero for maior ou "<" se o numero for menor
import random
def init():
    print('Bem vindo ao jogo de adivinhação')
    modo = int(input('Temos dois modos de jogo, digite 1 caso você queria que o computar advinhe o seu numero ou 2 para ao contrario.\n-> '))
    while modo != 1 and modo != 2:
        modo = int(input('Desculpa, não entendi.\nDigite 1 para pensar ou 2 para adivinhar.\n-> '))   
    if modo == 1:
        game(1)
    if modo == 2:
        game(2)

def game(m):
    if m == 1:
        print('Muito bem, essa vai ser moleza ;)\nPense em um número de 1 a 99.')
        t = 1
        r = '>'
        while r != '=':
            a = t
            t = computador(a,t,r)
            r = input(f'O numero que está na sua mente é {t}?\nsim (=)\nÉ maior (>)\nÉ menor (<)\n-> ')
    if m == 2:
        r = random.randint(1,99)
        t = 0

        while t != r:
            t = humano(r)
            if t > r:
                print('Não, esse número ai é maior')
            if t < r:
                print('Não, esse número ai é menor')
        print(f'Muito bem humano, eu estava mesmo pensando no {r}')
        f = int(input('Se quiser voltar ao inicio, digite 0, se nao, digite qualquer outro numero'))
        if f == 0:
            init()

def lixeira():
    l = []
    return l

def computador(a,t,r):
    lixeira().append(a)          
    if r == '>':
        t_n = random.randint(a,100)
        while t_n in lixeira():
           t_n = random.randint(a,100)          
    
    if r == '<':
        t_n = random.randint(1,a)
        while t_n in lixeira():
           t_n = random.randint(1,a) 
    return t_n

def humano(r):
    t = int(input('Vamos lá humano, adivinhe o numero que eu estou pensando de 1 a 99.\n-> '))
    return t

init()