def cadastro():
    aluno = input('Digite o nome do aluno: ')
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    nota3 = float(input('Digite a terceira nota: '))
    nota4 = float(input('Digite a quarta nota: '))
    def calcularMedia(n1,n2,n3,n4):
        media=(n1+n2+n3+n4)/4
        return media
    return {'Aluno': aluno,'Notas': [nota1,nota2,nota3,nota4],'Media': calcularMedia(nota1, nota2, nota3, nota4)}
def selecionarAluno():
    def escreverLinha():
        print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    i = 0
    for dado in alunos:
        print(i,':',dado)
        i = i + 1
    aluno = int(input('Escolha um aluno (em número): '))
    escreverLinha()
    print('Aluno: ', alunos[aluno])
    print('Prova 1: ', notas[aluno][0])
    print('Prova 2: ', notas[aluno][1])
    print('Atividade: ', notas[aluno][2])
    print('Trabalho: ', notas[aluno][3])
    escreverLinha()
    print('Média: ', medias[aluno])
    choice2 = input('\n\nDeseja escolher um aluno novamente? S/N\n')
    while choice2=='S':
        selecionarAluno()
alunos=[]
notas=[]
medias=[]
lista_de_cadastros=[]
choice = 'S'
while choice=='S':
    lista_de_cadastros.append(cadastro())
    choice = input('Você deseja cadastrar mais um aluno? S/N\n')
for dado in lista_de_cadastros:
    alunos.append(dado['Aluno'])
    notas.append(dado['Notas'])
    medias.append(dado['Media'])
selecionarAluno()
