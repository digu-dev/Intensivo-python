#1 entrar no sistema
#2 fazer login
#3 abrir a base de dados
#4 cadastrar 1 produto
#5 repetir o passo 4 ate acabar a base de dados

#pip install pyautogui

import time

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

pyautogui.click(x=982, y=504)  # Clique para o campo de email
pyautogui.write('rodrigo@rodrigo.com.br')  # Digite o email
pyautogui.click(x=1519, y=506)  # Clique para fora dos campos de email e senha
pyautogui.click(x=822, y=643)  # Clique para o campo de senha
pyautogui.write('123456')  # Digite a senha 
pyautogui.click(x=1519, y=506)  # Clique para fora dos campos de email e senha
pyautogui.click(x=963, y=712)  # Clique para o campo de logar


