'''
PROJETO DE RECONHECIMENTO FACIAL

Além da pesquisa na documentação oficial das bibliotecas Python, este projeto foi inspirado em outros projetos apresentados na internet, os quais têm as suas fontes listadas abaixo:
*   Reconhecimento Facial com Python, OpenCV e Mediapipe - https://youtu.be/mCcPmlr7y3U
*
'''

## Bibliotecas

import time
from datetime import datetime
import cv2 # opencv # Visão computacional
# import mediapipe as mp
import tkinter as tk # Frontend (telas)
from PySimpleGUI import PySimpleGUI as sg # Frontend (telas)
import reconhecimento_facial # Framework próprio
import shutil # Movimentação de arquivos entre pastas
import engine # Framework próprio
import webcam # Framework próprio

## Banco de Dados
# bd = reconhecimento_facial.Banco_de_Dados()
# bd.bd_ligar_banco('bd_reconhecimento_facial.db')

## Lógica do que deve acontecer ao clicar nos botões

# Cadastro
# cadastro_usuarios = {}




def carimbo_hora():
   # Hora
   agora = datetime.fromtimestamp(time.time())
   hora = agora.strftime('%H:%M:%S')
   carimbo_hora = agora.strftime('%d/%m/%y às ') + hora
   # print(f'Programa iniciado em {carimbo_hora}')
   return carimbo_hora


def cadastrar_usuario():
   cpf = valor['cpf']
   nome = valor['nome']
   sobrenome = valor['sobrenome']
   senha = valor['senha']
   confirmacao_senha = valor['confirmacao_senha']
   nome_foto = f'{cpf}-{nome}.png'
   #face_encodings = 'face_encodings'

   # # Cadastro
   # cadastro_usuarios = {}

   if nome == '' or sobrenome == '' or cpf == '':
       sg.popup('Informe o nome, sobrenome e CPF.')
   elif senha != confirmacao_senha:
       sg.popup('Senha não confere. Digite a mesma senha.')
   else:
       # cadastro_usuarios.update(
       #     {'cpf': {"nome_usuario": nome, "sobrenome": sobrenome, "senha": senha, "foto": foto}})
       #face_encodings = "AJUSTAR FACE ENCODINGS"
       reconhecimento_facial.bd_novo_usuario(cpf=cpf, nome=nome, sobrenome=sobrenome, senha=senha, nome_foto=nome_foto) #, face_encodings=face_encodings)

       sg.popup(f'Usuário salvo com sucesso\n\nUsuário: {nome} {sobrenome}\nCPF: {cpf}\nSenha:{senha}\nConfirmação Senha: {confirmacao_senha}')
       print(f'Log: Cadastro-Salvar Usuário - Usuário salvo: {nome} {sobrenome} - CPF: {cpf} - {carimbo_hora()}')


   # return cadastro_usuarios

## Criar janelas e estilos

def tela_inicial():
   # Tema
   sg.theme('Reddit')

   # Layout
   layout = [
       [sg.Text(text='SISTEMA DE RECONHECIMENTO FACIAL', justification='center')],
       [sg.Button('Cadastrar Novo Usuário', key='cadastrar_usuario', size=(50,3))],
       [sg.Button('Consultar Cadastro', key='consultar_cadastro', size=(50,3))],
       [sg.Text('DADOS DE LOGIN', size=(50, 1))],
       [sg.Text('CPF', size=(9, 1)), sg.Input(key='cpf_login', size=(11, 1)),
        sg.Text('Senha', size=(9, 1)), sg.Input(key='senha_login', size=(15, 1), password_char='*')],
       [sg.Button('DESCOBRIR SEGREDO', key='descobrir_segredo', size=(50,3), button_color='red')],
       [sg.Button('Fechar', size=(50,3))]
   ]

   # Janela
   return sg.Window('Tela Inicial', layout=layout, finalize=True)


def tela_cadastro():
   # Tema
   sg.theme('Reddit')

   # Layout
   layout = [
       [sg.Text(text='SISTEMA DE RECONHECIMENTO FACIAL', justification='center')],
       [sg.Text(text='Cadastrar Usuário')],
       [sg.Text('Nome', size=(9,1)), sg.Input(key='nome', size=(53,1))],
       [sg.Text('Sobrenome', size=(9,1)), sg.Input(key='sobrenome', size=(25,1)), sg.Text(text='CPF', size=(3,1)), sg.Input(key='cpf', size=(21,1))],
       [sg.Text('Senha', size=(9,1)), sg.Input(key='senha', password_char='*', size=(15,1)), sg.Text(text='Confirmação senha',size=(14,1)),sg.Input(key='confirmacao_senha', password_char='*', size=(18,1))],
       [sg.FileBrowse('Importar Foto', key='importar_foto'), sg.Button('Tirar Foto e Salvar', key='tirar_foto'),sg.Button('Salvar Usuário', key='salvar_usuario')],
       [sg.CloseButton('Fechar', key='fechar_cadastro')]
   ]

   # Janela
   return sg.Window('Tela de Cadastro', layout=layout, finalize=True)


def tela_consulta_cadastro():
   # Tema
   sg.theme('Reddit')

   # Layout
   layout = [
       [sg.Text(text='SISTEMA DE RECONHECIMENTO FACIAL', justification='center')],
       [sg.Text(text='CRIAR CONSULTA CADASTRO', justification='center')],
       # [sg.clipboard_get(reconhecimento_facial.bd_consultar_usuarios())],
       # [sg.Button('Cadastrar Novo Usuário', key='cadastrar_usuario')],
       # [sg.Button('Consultar Cadastro', key='consultar_cadastro')],

       [sg.CloseButton('Fechar', key='fechar_consulta')]
   ]


   # Janela
   return sg.Window('Cadastro', layout=layout, finalize=True)


def tela_segredo():
   # Tema
   sg.theme('Reddit')

   # Layout
   layout = [
       [sg.Text(text='O número Pi é igual a 3,141592653589793...', justification='center', size=(50,1))],
       [sg.Text(text='Fonte: https://numeropi.org/el-numero-pi-completo', justification='center', size=(50, 1))],
       [sg.Text(text='\n', justification='center', size=(50, 1))],
       [sg.Text(text='Já o googol é o número 10¹ºº, ou seja, o dígito 1 seguido de cem zeros.')],
       [sg.Text(text='Fonte: https://pt.wikipedia.org/wiki/Googol', justification='center', size=(50, 1))],
       # [sg.Text(text='Cadastrar Usuário')],
       # [sg.Text('Nome', size=(9,1)), sg.Input(key='nome', size=(53,1))],
       # [sg.Text('Sobrenome', size=(9,1)), sg.Input(key='sobrenome', size=(25,1)), sg.Text(text='CPF', size=(3,1)), sg.Input(key='cpf', size=(21,1))],
       # [sg.Text('Senha', size=(9,1)), sg.Input(key='senha', password_char='*', size=(15,1)), sg.Text(text='Confirmação senha',size=(14,1)),sg.Input(key='confirmacao_senha', password_char='*', size=(18,1))],
       # [sg.FileBrowse('Importar Foto', key='importar_foto'), sg.Button('Tirar Foto', key='tirar_foto'),sg.Button('Salvar Usuário', key='salvar_usuario')],
       [sg.CloseButton('Fechar', key='fechar_segredo')]
   ]

   # Janela
   return sg.Window('SEGREDO', layout=layout, finalize=True)


## Janela inicial
inicio = tela_inicial()
cadastro = None
consulta = None
ver_segredo = None

## Loop de leitura de eventos
while True:
   tela, evento, valor = sg.read_all_windows()

   # Eventos tela inicial
   if tela == inicio and evento == sg.WINDOW_CLOSED or evento == 'Fechar':
       break
       print(f'Log: Programa encerrado - {carimbo_hora()}')
   if tela == inicio and evento == 'cadastrar_usuario':
       inicio.hide()
       cadastro = tela_cadastro()
       cadastro.un_hide()
       print(f'Log: Cadastrar usuário - {carimbo_hora()}')
   if tela == inicio and evento == 'consultar_cadastro':
       consulta = tela_consulta_cadastro()
       print(f'Log: Consultar cadastro - {carimbo_hora()}')
   if tela == inicio and evento == 'descobrir_segredo': #and str(evento['senha']) == str(evento['senha_login']):
       nome_pessoa = webcam.verificar_pessoa()
       # nome_pessoa = webcam.nome()  # Abre a webcam para identificar a pessoa
       if nome_pessoa != 'Desconhecido':
           sg.popup(f'Olá {nome_pessoa}!', title='Pessoa identificada')
           print(f'Log: Ver segredo - {nome_pessoa} identificado(a) - {carimbo_hora()}')
           inicio.hide()
           ver_segredo = tela_segredo()
           ver_segredo.un_hide()
           # print(f'Log: Ver segredo - {carimbo_hora()}')
       else:
           sg.popup('Pessoa não identificada. Segredo não revelado')
           print(f'Log: Ver segredo - Pessoa não identificada. Segredo não revelado - {carimbo_hora()}')



   # Eventos da tela SEGREDO
   if tela == ver_segredo and evento == sg.WIN_CLOSED or evento == 'fechar_segredo':
       ver_segredo.hide()
       inicio = tela_inicial()
       inicio
       print(f'Log: Segredo fechado - {carimbo_hora()}')


   # Eventos tela de cadastro
   if tela == cadastro and evento == sg.WIN_CLOSED or evento == 'fechar_cadastro':
       cadastro.hide()
       inicio = tela_inicial()
       inicio
       print(f'Log: Cadastro fechado - {carimbo_hora()}')
   if tela == cadastro and evento == 'importar_foto':
       print(f'Log: Cadastro-Importar Foto - {carimbo_hora()}')
   if tela == cadastro and evento == 'tirar_foto':
       nome = valor['nome']
       # sobrenome = valor['sobrenome']
       cpf = valor['cpf']
       # senha = valor['senha']
       # confirmacao_senha = valor['confirmacao_senha']

       webcam = cv2.VideoCapture(0)  # Determina qual câmera ligada ao computador será usada. Cada número a partir do zero representa uma.

       if webcam.isOpened():
           print('Webcam funcionando')

           validacao, frame = webcam.read()

           while validacao:  # Executa o comando enquanto a validação for "True", ou seja, enquanto a validação que a câmera está aberta for "Verdadeira".
               validacao, frame = webcam.read()
               cv2.imshow('Cadastro Novo', frame)  # Mostra janela com imagem da webcam
               key = cv2.waitKey(5)  # Tempo de intervalo entre os frames em milisegundos

               # Cancelar o Cadastro
               if key == 27:  # Se clicar na tecla "ESC" (representada pelo número "27") a janela fecha.
                   webcam.release()
                   # cv2.destroyWindow(str(webcam))
                   # consulta.hide()
                   inicio = tela_inicial()
                   inicio
                   msg_cancelamento = tk.Label(text='Cadastramento Cancelado')
                   print('CADASTRO CANCELADO')

                   # validacao == False
                   break

               # if tela == consulta and evento == sg.WIN_CLOSED or evento == 'fechar_consulta':
               #     consulta.hide()
               #     inicio = tela_inicial()
               #     inicio

               # Tirar Foto
               if key == ord('p'):
                   nome_foto = f'{cpf}-{nome}.png'


                   cv2.imwrite(nome_foto, frame)

                   foto_para_mover = 'C:/Users/danil/PycharmProjects/TCC_Reconhecimento_Facial/'
                   foto_para_mover = f'{foto_para_mover}{nome_foto}'
                   pasta_onde_colar = 'C:/Users/danil/PycharmProjects/TCC_Reconhecimento_Facial/venv/Fotos Cadastradas'
                   shutil.move(foto_para_mover, pasta_onde_colar)
                   print('FOTO MOVIDA COM SUCESSO.')

                   print(f'FOTO SALVA COM SUCESSO: {nome_foto}')
                   cadastrar_usuario()

                   cv2.imread(f'{nome_foto}')

       webcam.release()
       tela_cadastro()
       # cv2.destroyWindow(webcam)
       # cv2.destroyAllWindows()

       print('WEBCAM DESLIGADA')

       # Mensagem de confirmação do cadastro com data e hora.
       agora = datetime.fromtimestamp(time.time())
       hora = agora.strftime('%H:%M:%S')
       status = agora.strftime('Cadastro realizado em %d/%m/%y às ') + hora
       print(status)

       print(f'Log: Cadastro-Tirar Foto - {carimbo_hora()}')

   if tela == cadastro and evento == 'salvar_usuario':
       cadastrar_usuario()

       try:
           foto_para_mover = 'C:/Users/danil/PycharmProjects/TCC_Reconhecimento_Facial/'
           foto_para_mover = foto_para_mover + nome_foto
           pasta_onde_colar = 'C:/Users/danil/PycharmProjects/TCC_Reconhecimento_Facial/venv/Fotos Cadastradas'
           pasta_onde_colar = pasta_onde_colar + nome_foto
           # Mover foto para fotos cadastradas
           shutil.move(foto_para_mover, pasta_onde_colar)
       except:
           pass

   # Eventos tela de consulta ao cadastro
   if tela == consulta and evento == sg.WIN_CLOSED or evento == 'fechar_consulta':
       consulta.hide()
       inicio = tela_inicial()
       inicio
       print(f'Log: Consulta ao cadastro fechada - {carimbo_hora()}')
   if tela == consulta:
       reconhecimento_facial.bd_consultar_usuarios()
   if tela == consulta: # and evento == 'importar_foto':
       # print(f'Log: Importar foto - {carimbo_hora()}')
       print('CADASTRO ATUALIZADO')
       pass


