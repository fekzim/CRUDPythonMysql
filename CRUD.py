import mysql.connector 
import PySimpleGUI as sg
from tabela import janelaInfo
from create_db_connection import *
from janelaLogin import janelaLogin, Logar
from menu import janelaMenu
from Cadastrar import *
#Conexão com banco de dados
connection = create_db_connection("localhost","root","fek123","bdtestes")
#Cursor = aquele que executara as querys
cursor = connection.cursor()


#Janela inicial
janela1 = janelaLogin()

#LOOP DE EVENTOS
while True:
    window, event,values = sg.read_all_windows()

    #window closed
    if event == sg.WINDOW_CLOSED:
        break
    
    ## JANELA DE LOGIN ##
    if window == janela1 and event== 'Logar':
        #Recebe valores do que foi digitado no text box 
        user = values['usuario']
        
        senhaDigitada = values['senha']

        logado = Logar(user,senhaDigitada,connection,cursor)

        if logado == True:
            janela1.close()
            janela1 = janelaMenu()
        else:
            window['mensagem'].Update("Falha ao logar")

    if window == janela1 and event== 'Cadastrar Cliente':
        janela1.close()
        janela1 = janelaCadastro()

    if window == janela1 and event== 'Visualizar Clientes':
        janela1.close()
        janela1 = janelaInfo()
    
    if window == janela1 and event== 'DESLOGAR':
        janela1.close()
        janela1 = janelaLogin()
    
    if window == janela1 and event== 'Voltar':
        janela1.close()
        janela1 = janelaMenu()

    if window == janela1 and event == 'Cadastrar':
        connection = create_db_connection("localhost","root","fek123","bdtestes")
        #Cursor = aquele que executara as querys
        cursor = connection.cursor()
        login = values['user']
        senhaCadastrar = values['password']
        sexCadastrar = values['sex']
        Cadastrar(login,senhaCadastrar,sexCadastrar,cursor)
        Limpar(values,window)
        
    if window == janela1 and event ==  'Limpar':
        Limpar(values,window)

cursor.close()
connection.close()