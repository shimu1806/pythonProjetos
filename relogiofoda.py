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

def relogio(): # definindo o relogio que rodará as horas atuais do momento

    tempo = datetime.now()
    hora = tempo.strftime("%H:%M:%S")
    dia_semana = tempo.strftime("%A")
    dia = tempo.day
    mes = tempo.strftime("%b")
    ano = tempo.strftime("%Y")


    L1.config(text=hora) # a função atribuida ao obj "hora" substituirá o texto apresentado na label
    L1.after(200, relogio) # para manter o tempo dinamico, usamos essa função. como ela funciona? não sei, mas funciona
    L2.config(text=dia_semana + "   " + str(dia) + # apenas entregando ao relógio as demais funções do __relogio__
              "/" + str(mes) + "/" + (ano))


L1 = Label(
    janela,
           text="10:05:05", # tanto faz, só para formatar como 00:00:00, ele logo receberá o hora
           font=('digital-7  80'),
           bg=fundo,
           fg=cor
)

L1.grid(row=0, column=0, sticky=NW, padx=5) # pra ficar bem bacana em cima


L2 = Label(
    janela,
           font=('digital-7  20'),
           bg=fundo,
           fg=cor
)

L2.grid(row=1, column=0, sticky=NW, padx=5)

# executa.py fé
relogio()
janela.mainloop()
