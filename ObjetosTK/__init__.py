from tkinter import *


class Aplicacao(Frame):
    def __init__(self, meumaster):
        super().__init__()
        self['height'] = 150
        self['width'] = 200
        self['bd'] = 2
        self['relief'] = SOLID

        def conta():
            val1 = bol_val1.get()
            val2 = bol_val2.get()
            resultado = val1 / val2
            entrada = Label(self, text=f'US${resultado:.3f}', fg='blue').grid(row=3, column=1)

        bol_val1 = DoubleVar()
        bol_val2 = DoubleVar()

        texto1 = Label(self, text='Valor que deseja converter:   R$')
        valor1 = Entry(self, textvariable=bol_val1)
        texto1.grid(row=0, column=0)
        valor1.grid(row=0, column=1)

        texto2 = Label(self, text='Cotação do Dólar:\t\t US$')
        valor2 = Entry(self, textvariable=bol_val2)
        texto2.grid(row=1, column=0)
        valor2.grid(row=1, column=1)

        bt = Button(self, text='Somar', command=conta).grid(row=2, column=0)
        entrada = Label(self, text='Convertido para:').grid(row=3, column=0)

