#1 entrar no sistema

#pip install pyautogui

import time

import pandas as pd

import pyautogui

pyautogui.PAUSE = 0.5  # Adiciona uma pausa de meio segundo entre as ações
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

#pyautogui.click -> clica
#pyautogui.write -> escreve
#pyautogui.press -> aperta uma tecla
#pyautogui.hotkey -> aperta uma combinação de teclas

pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
pyautogui.press('tab')
pyautogui.press('enter')
pyautogui.hotkey('ctrl', 't')
pyautogui.write(link)
pyautogui.press('enter')  
time.sleep(3)  # Aguarda 2 segundos para a página carregar 

#2 fazer login

pyautogui.click(x=982, y=504)  # Clique para o campo de email
pyautogui.write('rodrigo@rodrigo.com.br')  # Digite o email

#
#pyautogui.click(x=1519, y=506)  # Clique para fora dos campos de email e senha
#pyautogui.click(x=822, y=643)  # Clique para o campo de senha
#pyautogui.write('123456')  # Digite a senha 
#pyautogui.click(x=1519, y=506)  # Clique para fora dos campos de email e senha
#pyautogui.click(x=963, y=712)  # Clique para o campo de logar
#

pyautogui.press('tab')  # Pressiona a tecla Tab para ir para o campo de senha
pyautogui.write('123456')  # Digite a senha
pyautogui.press('tab')  # Pressiona a tecla Tab para ir para o botão de logar
pyautogui.press('enter')  # Pressiona a tecla Enter para clicar no botão
time.sleep(5)  # Aguarda 2 segundos para a página carregar

pyautogui.click(x=1519, y=506)  # Clique para fora dos campos de email e senha
time.sleep(2)  # Aguarda 2 segundos para a página carregar

#3 abrir a base de dados
table = pd.read_csv('produtos.csv')
print(table)

#4 cadastrar 1 produto

for line in table.index:
    pyautogui.click(x=827, y=367)  # Clique para o campo de nome do produto
    
    #codigo
    codigo = str(table.loc[line, "codigo"])
    pyautogui.write(codigo)  # Digite o codigo do produto
    pyautogui.press('tab')  # Pressiona a tecla Tab para ir para o campo de preço
    
    #marca
    marca = str(table.loc[line, "marca"])
    pyautogui.write(marca)  # Digite a marca do produto
    pyautogui.press('tab')  # Pressiona a tecla Tab para ir para o campo de quantidade

    #tipo
    tipo = str(table.loc[line, "tipo"])
    pyautogui.write(str(table.loc[line, "tipo"]))  # Digite o tipo do produto
    pyautogui.press('tab')  # Pressiona a tecla Enter para cadastrar o produto

    #categoria
    categoria = str(table.loc[line, "categoria"])
    pyautogui.write(str(table.loc[line, "categoria"]))  # Digite a categoria do produto
    pyautogui.press('tab')  # Pressiona a tecla Tab para ir para o campo de preço

    #preco_unitario
    preco_unitario = str(table.loc[line, "preco_unitario"])
    pyautogui.write(preco_unitario)  # Digite o preço do produto
    pyautogui.press('tab')  # Pressiona a tecla Tab para ir para o campo de custo

    #custo
    custo = str(table.loc[line, "custo"])
    pyautogui.write(str(table.loc[line, "custo"]))  # Digite o custo do produto
    pyautogui.press('tab')  # Pressiona a tecla Tab para ir para o campo de observação

    #obs
    obs = str(table.loc[line, "obs"])
    pyautogui.write(obs)  # Digite a observação do produto 
    pyautogui.press('tab')  # Pressiona a tecla tab para ir para o campo de cadastrar
    pyautogui.press('enter')  # Pressiona a tecla Enter para cadastrar o produto
    
    pyautogui.scroll(5000)  # Rola a tela para baixo para visualizar o próximo produto

    time.sleep(3)  # Aguarda 1 segundo para o cadastro ser processado

#5 repetir o passo 4 ate acabar a base de dados

