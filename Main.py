from Models.Aluno import Aluno

def CriaAluno(nome, matricula):
    BuscaAlunoPorMatricula(matricula)
    novoAluno = Aluno(nome,matricula)
    Salvar()


def AtualizaAluno(nome,matricula):
    result = BuscaAlunoPorMatricula(matricula)


def BuscaAlunoPorMatricula(matricula):
    #  Implementar Busca
    #  if  resultado busca:
    # deixa ou não salvar.


def Salvar():