import tkinter as tk
from arq import Aplicacao

janela = tk.Tk()
janela.title('Conversor de Moeda')
    
Aplicacao(janela).grid()

janela.resizable(0, 0)

janela.mainloop()
