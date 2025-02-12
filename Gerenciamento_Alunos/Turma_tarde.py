from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

engine = create_engine('sqlite:///Escola/turma_tarde.db')
_session = sessionmaker(bind=engine)
session = _session()

base = declarative_base()

def create_table():
    
    class Turma(base):
        __tablename__ = 'turma_tarde'
        turma = Column(String(10), default='CN 3002')
        id = Column(Integer, primary_key=True)
        name = Column(String(40))
        media = Column(Integer)
        status = Column(String(40))
        
    
    return Turma

clase = create_table()
base.metadata.create_all(engine)

def insert_data(nomes, medias):
    try:
        for i in range(len(nomes)):
            aluno = nomes[i]
            nota = medias[i]
            if nota >= 7:
                status = 'Aprovado'
            elif nota > 4 and nota <= 6:
                status = 'Recuperação'
            else:
                status = 'Reprovado'
            Aluno = clase(turma='CN 3001',name=aluno, media=nota, status=status)
            session.add(Aluno)
        session.commit()
        print('Dados inseridos com sucesso')
    except Exception as e:
        session.rollback() 
        print(f'Erro ao inserir os dados: {e}')
    finally:
        session.close()

def solict_02():
    nomes = []
    notas = []
    while True:
            nome = input('Digite o nome do aluno: ')
            media = int(input('Digite a média do aluno: '))
            nomes.append(nome)
            notas.append(media)
            if input('Deseja inserir um novo aluno? (s/n): ') == 'n':
                break 
    insert_data(nomes, notas)
    
def exibir_02():
    for aluno in session.query(clase).all():
        print()
        print(f'Nome: {aluno.name} | Média: {aluno.media} | Status: {aluno.status}')
        print()

def modificar_02():
    nome = input('Digite o nome do aluno que deseja modificar: ')
    aluno = session.query(clase).filter(clase.name == nome).first()
    aluno.name = input('Digite o novo nome do aluno: ')
    aluno.media = int(input('Digite a nova média do aluno: '))
    if aluno.media >= 7:
        aluno.status = 'Aprovado'
    elif aluno.media > 4 and aluno.media <= 6:
        aluno.status = 'Recuperação'
    else:
        aluno.status = 'Reprovado'
    try:
        session.commit()
    except Exception as e:
        session.rollback()
        print(f'Erro ao modificar os dados: {e}')
    finally:
        print('Dados modificados com sucesso')
        session.close()
    
def excluir_02():
    nome = input('Digite o nome do aluno que deseja excluir: ')
    aluno = session.query(clase).filter(clase.name == nome).first()
    try:
        session.delete(aluno)
        session.commit()
    except Exception as e:
        session.rollback()
        print(f'Erro ao excluir os dados: {e}')
    finally:
        print('Dados excluídos com sucesso')
        session.close()