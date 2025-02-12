from Turma_tarde import solict_02, exibir_02, modificar_02, excluir_02
from Turma_manha import solict_01, exibir_01, modificar_01, excluir_01

def main():
    print('Bem vindo ao sistema de gerenciamento de turmas')
    while True:
        print('1 - Turma da manhã\n2 - Turma da tarde\n3 - Sair')
        op = input('Digite a opção desejada: ')
        if op == '1':
            turma_manha()
        elif op == '2':
            turma_tarde()
        elif op == '3':
            break
        else:
            print('Opção inválida')

def turma_manha():
    while True:
        print('1 - Inserir aluno\n2 - Exibir alunos\n3 - modificar\n4 - Excluir\n5 - Sair')
        op = input('Digite a opção desejada: ')
        if op == '1':
            solict_01()
        elif op == '2':
            exibir_01()
        elif op == '3':
            modificar_01()
        elif op == '4':
            excluir_01()
        elif op == '5':
            break       
        else:
            print('Opção inválida')

def turma_tarde():
    while True:
        print('1 - Inserir aluno\n2 - Exibir alunos\n3 - modificar\n4 - Excluir\n5 - Sair')
        op = input('Digite a opção desejada: ')
        if op == '1':
            solict_02()
        elif op == '2':
            exibir_02()
        elif op == '3':
            modificar_02()
        elif op == '4':
            excluir_02()
        elif op == '5':
            break       
        else:
            print('Opção inválida')

if __name__ == '__main__':
    main()