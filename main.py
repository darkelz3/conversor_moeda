from tkinter import Tk, ttk
from tkinter import *

# Importando bibliotecas

from PIL import Image, ImageTk, ImageOps, ImageDraw

import requests
import json
import string

# Cores
cor0 = "#FFFFFF" # White/Branco
cor1 = "#333333" # Black/Preto
cor2 = "#38576b" # Blue/Azul

# Interface Grafica

janela = Tk()
janela.geometry('300x320')
janela.title('Conversor')
janela.configure(bg=cor0)
janela.resizable(False, False)

style = ttk.Style(janela)
style.theme_use("clam")


# Frame da interface grafica
# Frame Superior
frame_cima = Frame(janela, width=300, height=60, padx=0, pady=0, bg=cor2, relief='flat')
frame_cima.grid(row=0, column=0, columnspan=2)

# Frame Inferior
frame_baixo = Frame(janela, width=300, height=260, padx=0, pady=5, bg=cor0, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW)


#Função Converter

def converter():
    moeda_de = combo_de.get()
    moeda_para = combo_para.get()
    valor_entrado = valor.get()

    response = requests.get('https://api.exchangerate-api.com/v4/latest/{}'.format(moeda_de))
    dados = json.loads(response.text)
    cambio = dados['rates'][moeda_para]

    resultado = float(valor_entrado) * float(cambio)

    if moeda_para == 'USD':
        simbolo = '$ '
    elif moeda_para == 'EUR':
        simbolo = '€ '
    else:
        simbolo = 'R$ '

    moeda_equivalente = simbolo + "{:,.2f}".format(resultado)
    
    app_resultado['text'] = moeda_equivalente




# Config Frame_Cima

icon = Image.open('images/icon.png')
icon = icon.resize((40, 40))
icon = ImageTk.PhotoImage(icon)

app_nome = Label(frame_cima, image=icon, compound=LEFT, text='Conversor de Moeda ', height=5, pady=30, padx=13, relief='raised', anchor=CENTER, font=('Arial 16 bold'), bg=cor2, fg=cor0)
app_nome.place(x=0, y=0)


# Config Frame_Baixo

app_resultado = Label(frame_baixo, text='', width=16, height=2, relief='solid', anchor=CENTER, font=('Ivy 15 bold'), bg=cor0, fg=cor1)
app_resultado.place(x=50, y=10)

moeda = ['BRL', 'EUR', 'USD']

#Caixa de Seleção DE
app_de = Label(frame_baixo, text='De', width=8, height=1, relief='flat', anchor=CENTER, font=('Ivy 10 bold'), bg=cor0, fg=cor1)
app_de.place(x=48, y=90)
combo_de = ttk.Combobox(frame_baixo, width=8, justify=CENTER, font=('Ivy 12 bold'))
combo_de.place(x=50, y=115)
combo_de['values'] = (moeda)

#Caixa de Seleção PARA
app_para = Label(frame_baixo, text='Para', width=8, height=1, relief='flat', anchor=CENTER, font=('Ivy 10 bold'), bg=cor0, fg=cor1)
app_para.place(x=158, y=90)
combo_para = ttk.Combobox(frame_baixo, width=8, justify=CENTER, font=('Ivy 12 bold'))
combo_para.place(x=160, y=115)
combo_para['values'] = (moeda)

valor = Entry(frame_baixo, width=22, justify=CENTER, font=('Ivy 12 bold'), relief=SOLID)
valor.place(x=50, y=155)

botao = Button(frame_baixo, command=converter, text='Converter', width=19, padx=5, height=1, bg=cor2, fg=cor0, font=('Ivy 12 bold'), relief='raised', overrelief=RIDGE)
botao.place(x=50, y=210)


janela.mainloop()