from tkinter import *
from tkinter import ttk
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
import pandas as pd


class Aplicacao(Frame):
    def __init__(self, meumaster):
        super().__init__()
        self['height'] = 150
        self['width'] = 200
        self['bd'] = 2
        self['relief'] = SOLID

        # Tendo acesso aos dados web do site
        url = 'https://br.investing.com/currencies/exchange-rates-table'
        option = Options()
        option.headless = True
        driver = webdriver.Chrome(options=option)
        driver.get(url)

        # Encontrando o elemento no site
        elemento = driver.find_element_by_xpath('//div[@class="wrapper"]//section//table[@id="exchange_rates_1"]')
        html_content = elemento.get_attribute('outerHTML')

        # Analisando e Extraindo dados
        souap = BeautifulSoup(html_content, 'html.parser')
        table = souap.find(name='table')


        def conta():
            # Finalizando
            df_full = pd.read_html(str(table).replace(',', '.'))[0]
            df_full.head()
            caixa1 = caixa_escolha1.get()
            caixa2 = caixa_escolha2.get()

            print(df_full)
            
            df_full.set_index('Código', inplace=True)
            df_full.loc[f'{caixa1}', f'{caixa2}']

            valor_1 = df_full.loc[caixa1, caixa2]
            valor_2 = df_full.loc[caixa2, caixa1]
            print(valor_1)
            print(valor_2)

            convert = float(valor1.get()) * float(valor_1)

            Label(self, text=f'{caixa_escolha2.get()} 1.00 = {caixa_escolha1.get()} {valor_1}', fg='blue').grid(row=2, column=1)
            Label(self, text=f'{caixa_escolha1.get()} 1.00 = {caixa_escolha2.get()} {valor_2}', fg='blue').grid(row=2, column=4)
            Label(self, text=f'{caixa_escolha2.get()} {convert:.3f}', fg='black', font=('bold', 12)).grid(row=4, column=0)

        Label(self, text='..............', fg='black', font=('bold', 12)).grid(row=4, column=0)
        bol_val1 = DoubleVar()
        bol_val2 = DoubleVar()
        valor1 = Entry(self, textvariable=bol_val1)
        valor1.grid(row=0, column=1)

        """
        Label(self, text='Cotação de destino:').grid(row=1, column=0)
        valor1.grid(row=0, column=1)
  
        valor2 = Entry(self, textvariable=bol_val2)
        valor2.grid(row=1, column=1)
        """

        Label(self, text='Valor de origem:').grid(row=0, column=0)
        Button(self, text='Converter', command=conta).grid(row=2, column=0)

        Label(self, text='Cotação de destino: ').grid(row=0, column=4)  
        """
        Label(self, text='').grid(row=4, column=0)
        Label(self, text='Convertido para:').grid(row=4, column=0)
        """
        caixa_escolha1 = ttk.Combobox(self, values=['BRL', 'USD', 'EUR', 'GBP', 'JPY', 'CHF', 'CAD', 'AUT'], width=4)
        caixa_escolha1.grid(row=0, column=3)
        caixa_escolha1.current(1)

        caixa_escolha2 = ttk.Combobox(self, values=['BRL', 'USD', 'EUR', 'GBA', 'JPY', 'CHF', 'CAD', 'AUT'], width=4)
        caixa_escolha2.grid(row=0, column=5)
        caixa_escolha2.current(1)
