'''1 - Classe simples
Crie uma classe Pessoa com atributos: nome, idade e email.
Crie um método que exiba as informações da pessoa em formato
de string. Instancie pelo menos 3 objetos e teste.'''

'''2 - Encapsulamento e validação
Na classe Pessoa, garanta que a idade não pode ser negativa.
Adicione um método aniversario() que aumenta a idade em 1.'''

'''3 - Herança
Crie uma classe Aluno que herda de Pessoa.
Adicione atributos: matricula e curso.
Adicione um método exibir_dados_aluno() 
que mostra todas as informações (inclusive herdadas).'''

'''4 - Composição
Crie uma classe Curso com os atributos: nome e alunos 
(lista de objetos Aluno).
Crie métodos para:
Adicionar aluno.
Listar todos os alunos.'''

class Pessoa:
  def __init__(self, nome, idade, email):
    self.nome = nome
    if idade < 0:
      raise ValueError('Idade não pode ser negativa')
    self.idade = idade
    self.email = email
  
  def __str__(self):
    return 'Nome:{}\nIdade:{}\nEmail:{}\n'.format(self.nome, str(self.idade), self.email)
  
  def aniversario(self):
    self.idade += 1

class Aluno(Pessoa):
  def __init__(self, nome, idade, email, matricula, curso):
    super().__init__(nome, idade, email)
    self.matricula = matricula
    self.curso = curso
  
  def exibir_dados_aluno(self):
    info_pessoa = super().__str__()
    info_aluno = 'Matricula:{}\nCurso:{}\n'.format(
      self.matricula, self.curso)
    return info_pessoa + info_aluno

class Curso():
  def __init__(self, nome):
    self.nome = nome
    self.list_alunos = []
    
  def add_aluno(self, aluno):
    self.list_alunos.append(aluno)
    return 'Aluno(a) {} adicionado ao curso de {}'.format(aluno.nome, self.nome)
    
  def listar_alunos(self):
    for i, aluno in enumerate(self.list_alunos, start=1):
      print(f'{i},{aluno}')

p1 = Pessoa('Breno Moura', 22, 'dantas@gmail.com')
p2 = Pessoa('Herbet Vinicius', 18, 'davi@gmail.com')
p3 = Pessoa('Alexandre', 20, 'Lucas@gmail.com')
p1.aniversario()
print(p1,'\n')
print(p3,'\n')
print(p2,'\n')

a1 = Aluno('Fabio', 30, 'fabio@gmail.com', '20230001', 'Info')
a2 = Aluno('Vagner', 25, 'Vagner@gmail.com', '20230002', 'mat')
a3 = Aluno('Marcos', 30, 'Marcos@gmail.com', '20230003', 'Tec')
a1.aniversario()
print(a1.exibir_dados_aluno(),'\n')


curso1 = Curso('Informática')
print(curso1.add_aluno(a1))
print(curso1.add_aluno(a2))
print(curso1.add_aluno(a3))
curso1.listar_alunos()