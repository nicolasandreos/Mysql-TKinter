import pyodbc

def conectar_bd(dados_conexao:str) -> pyodbc.Connection | None:
  try:
    conexao = pyodbc.connect(dados_conexao)
    print('✅ Conexão bem sucedida!')
    return conexao
  except pyodbc.Error as error:
    print(f'❌ Erro ao conectar ao banco: {error}')
    return None


def criar_cursor(conexao:pyodbc.Connection) -> pyodbc.Cursor:
  cursor = conexao.cursor()
  return cursor


def consultar(cursor:pyodbc.Cursor, tabela:str) -> list[tuple]:
  comando = f'SELECT * FROM {tabela}'
  cursor.execute(comando)
  return cursor.fetchall()


def adicionar_aluno(cursor:pyodbc.Cursor, nome:str, email:str, dt_nascimento:str, var_alunos: int):
  comando = f"INSERT INTO alunos VALUES (NULL, '{nome}', '{email}', '{dt_nascimento}')"
  cursor.execute(comando)
  cursor.commit()
  print('Aluno adicionado com sucesso!')
  alunos = consultar(cursor, 'alunos')
  var_alunos.set(len(alunos))


def adicionar_curso(cursor:pyodbc.Cursor, nome:str, preco:float, var_cursos: int):
  comando = f"INSERT INTO cursos VALUES (NULL, '{nome}', {preco})"
  cursor.execute(comando)
  cursor.commit()
  print('Curso adicionado com sucesso!')
  cursos = consultar(cursor, 'cursos')
  var_cursos.set(len(cursos))


def adicionar_matricula(cursor:pyodbc.Cursor, id_aluno:int, id_curso:int, dt_matricula:str, var_matriculas: int):
  comando = f"INSERT INTO matriculas VALUES (NULL, {id_aluno}, {id_curso}, '{dt_matricula}')"
  cursor.execute(comando)
  cursor.commit()
  print('Matrícula adicionada com sucesso!')
  matriculas = consultar(cursor, 'matriculas')
  var_matriculas.set(len(matriculas))

def atualizar_aluno(cursor:pyodbc.Cursor, campos:list, novos_valores:str, id:int):
  for i, campo in enumerate(campos):
    comando = f"UPDATE alunos SET {campo} = '{novos_valores[i]}' WHERE ID_Aluno = {id}"
    cursor.execute(comando)
    cursor.commit()
  aluno = pegar_aluno(cursor, id)
  print(f'Os dados do aluno {aluno[0][1]} foram atualizados com sucesso!')


def deletar_aluno(cursor:pyodbc.Cursor, id:int):
  aluno = pegar_aluno(cursor, id)
  comando = f'DELETE FROM alunos WHERE ID_Aluno = {id}'
  cursor.execute(comando)
  cursor.commit()
  print(f'O aluno {aluno[0][1]} foi detetado do Banco de Dados')


def pegar_aluno(cursor:pyodbc.Cursor, id:int) -> list[tuple]:
  comando = f"SELECT * FROM alunos WHERE ID_Aluno = {id}"
  cursor.execute(comando)
  return cursor.fetchall()


def extrair_colunas(cursor:pyodbc.Cursor) -> list:
  return [tupla[0] for tupla in cursor.description]


def fechar_conexao(cursor:pyodbc.Cursor, conexao: pyodbc.Connection):
  cursor.close()
  conexao.close()