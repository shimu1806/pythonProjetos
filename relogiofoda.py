"""

Relogio digital, horas, dia/mes/ano, semana

"""

from tkinter import *
from datetime import *

cor1 = "#3d3d3d"  # preta
cor2 = "#fafcff"  # branca
cor3 = "#21c25c"  # verde
cor4 = "#eb463b"  # vermelha
cor5 = "#dedcdc"  # cinza
cor6 = "#3080f0"  # azul

fundo = cor1
cor = cor3


# janela

janela = Tk()
janela['bg'] = "black"
janela.title = ("Relogio Digital")
janela.geometry = "800x200"
janela.resizable(width=FALSE, height=FALSE)


# horario

def relogio():

    tempo = datetime.now()
    hora = tempo.strftime("%H:%M:%S")
    dia_semana = tempo.strftime("%A")
    dia = tempo.day
    mes = tempo.strftime("%b")
    ano = tempo.strftime("%Y")

    L1.config(text=hora)
    L1.after(200, relogio)


    L1.config(text=hora)
    L1.after(200, relogio)
    L2.config(text=dia_semana + "   " + str(dia) +
              "/" + str(mes) + "/" + (ano))


L1 = Label(
    janela,
           text="10:05:05",
           font=('digital-7  80'),
           bg=fundo,
           fg=cor
)

L1.grid(row=0, column=0, sticky=NW, padx=5)


L2 = Label(
    janela,
           font=('digital-7  20'),
           bg=fundo,
           fg=cor
)

L2.grid(row=1, column=0, sticky=NW, padx=5)


relogio()
janela.mainloop()