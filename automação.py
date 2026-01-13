import pyautogui
import time
import pandas as pd
import webbrowser

pyautogui.PAUSE = 0.3

webbrowser.open("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
time.sleep(3)

pyautogui.click(x=837, y=407)
pyautogui.write("emailltotalmentelegitimo@gmail.com")
pyautogui.press("tab")
pyautogui.write("sua senha muito secreta")
pyautogui.press("enter")
time.sleep(3)

tabela = pd.read_csv("produtos.csv")

for linha in tabela.index:
    
    pyautogui.click(x=808, y=296)
    
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs = str(tabela.loc[linha,"obs"])
    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(5000)    
