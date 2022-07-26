import sqlite3
import pandas as pd
from deepface import DeepFace
import cv2
import matplotlib.pyplot as plt
import sqlalchemy
from PySimpleGUI import PySimpleGUI as sg

# class Banco_de_Dados():
#
#     # Criação do Banco de Dados
#
#     def __init__(self):
#         pass
#
#     def bd_criar_bd(self, nome_bd):
#         '''Cria ou abre banco de dados.'''
#         self.nome_bd = f'{nome_bd}.db'
#         self.banco = sqlite3.connect(self.nome_bd)
#         self.cursor = self.banco.cursor()
#
#     def bd_ligar_banco(self, nome_bd):
#         '''Abrir Banco de Dados'''
#         self.nome_bd = nome_bd
#         self.banco = sqlite3.connect(self.nome_bd)
#         self.cursor = self.banco.cursor()
#
#     def bd_desligar_bd(self):
#         '''Fechar Banco de Dados'''
#         self.banco.close()
#
#     # def bd_criar_tabela(self):
#     #     self.campos_tabela = input('Informe os campos da tabela no formato SQL: ')
#     #     self.nome_tabela = input('Informe o nome da tabela: ')
#     #     self.cursor.execute(f'CREATE TABLE {self.nome_tabela} ({self.campos_tabela})')
#
#
#
#
#
# # bd_reconhecimento_facial = Banco_de_Dados()
# # bd_reconhecimento_facial.bd_criar_bd('bd_reconhecimento_facial')
# # bd_reconhecimento_facial.bd_criar_tabela()


def bd_novo_usuario(cpf, nome, sobrenome, senha, nome_foto): #, face_encodings):
   banco = sqlite3.connect('bd_reconhecimento_facial.db') # Conexão com o banco de dados
   cursor = banco.cursor() # Criação de cursor, conforme indicado na documentação da biblioteca

   # def bd_novo_usuario(cpf, nome, sobrenome, senha, nome_foto):  # , face_encodings):
   #    banco = sqlite3.connect('bd_reconhecimento_facial.db')  # Conexão com o banco de dados
   #   cursor = banco.cursor()

   # Insere uma nova linha

   cursor.execute(f'INSERT INTO usuarios VALUES ({cpf}, "{nome}", "{sobrenome}", "{senha}", "{nome_foto}")') #, "{face_encodings}")')

   # try:
   #     with banco:
   #          cursor.execute(f'INSERT INTO usuarios VALUES ({cpf}, "{nome}", "{sobrenome}", "{senha}", "{nome_foto}")')
   # except sqlite3.IntegrityError:
   #     print('Usuário já cadastrado.')

   #Salva (commit) as alterações
   banco.commit()
   banco.close()

def bd_consultar_usuarios():
   # banco = sqlite3.connect('bd_reconhecimento_facial.db')
   # cursor = banco.cursor()
   # '''Visualizar tabela'''
   # cursor.execute(f'SELECT * FROM usuarios')
   # # cursor.execute(f'SELECT * oid FROM usuarios')
   #
   # lista_usuarios = cursor.fetchall()
   # lista_usuarios = pd.DataFrame(lista_usuarios, columns=['CPF', 'Nome', 'Sobrenome', 'Senha', 'Nome da Foto'])
   # print(lista_usuarios)
   # return lista_usuarios
   #
   # banco.commit()
   # banco.close()

   engine = sqlalchemy.create_engine('sqlite:///bd_reconhecimento_facial.db')
   relatorio_usuarios = pd.read_sql('usuarios', engine,index_col='cpf')
   relatorio_usuarios.rename(columns={'cpf':'CPF', 'nome':'Nome', 'sobrenome':'Sobrenome', 'senha':'Senha', 'nome_foto':'Foto'}, inplace=True)
   relatorio_usuarios.align(other=relatorio_usuarios, join="outer", axis=1)

   print(relatorio_usuarios)

   sg.popup(relatorio_usuarios)

   return relatorio_usuarios

def consultar_imagem(cpf):
   cpf = cpf

   banco = sqlite3.connect('bd_reconhecimento_facial.db')
   cursor = banco.cursor()
   '''Visualizar tabela'''
   cursor.execute(f'SELECT "nome_foto" FROM "usuarios" WHERE "cpf" = {cpf}')
   # # cursor.execute(f'SELECT * oid FROM usuarios')
   #
   nome_foto_consulta = cursor.fetchone()
   # x = cursor.f
   # lista_usuarios = pd.DataFrame(lista_usuarios, columns=['CPF', 'Nome', 'Sobrenome', 'Senha', 'Nome da Foto'])
   print(nome_foto_consulta)
   # return lista_usuarios
   #
   banco.commit()
   banco.close()

def comparar_imagens():
   img1 = cv2.imread(r'C:\Users\danil\PycharmProjects\TCC_Reconhecimento_Facial\venv\Foto Acesso\313-Daniel.png')
   # plt.imshow(img1[:, :, ::-1])
   # plt.show()

   img2 = cv2.imread(r'C:\Users\danil\PycharmProjects\TCC_Reconhecimento_Facial\venv\Fotos Cadastradas\111-Danilo Donizeti.png')
   # plt.imshow(img2[:, :, ::-1])
   # plt.show()

   ## 3. COMPARAR DUAS IMAGENS
   result = DeepFace.verify(img1, img2)
   # print(result)


   if result['verified'] == True:
      print('É a mesma pessoa')
      print(result)
   else:
      print('Pessoa não identificada')
      print(result)
