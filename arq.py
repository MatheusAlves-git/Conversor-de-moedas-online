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

        # Finalizando
        df_full = pd.read_html(str(table).replace(',', '.'))[0]
        sleep(5)

        def conta():
            print(df_full)
            df_full.head()
            caixa1 = caixa_escolha1.get()
            caixa2 = caixa_escolha2.get()

            x = df_full.loc[(df_full['Código'] == f'{caixa1}') & (df_full['BRL'] == f'{caixa2}')]
            print(x)
            df_full.loc[2]
            df1 = df_full.loc[2, [f'{caixa1}']]
            df2 = df_full.loc[2, [f'{caixa2}']]

            for l in enumerate(df1):
                valor_1 = l[1]

            for l in enumerate(df2):
                valor_2 = l[1]

            calc = valor_1 * valor_2

            Label(self, text=f'{caixa_escolha2.get()}    {calc}', fg='blue').grid(row=4, column=1)
            Label(self, text=f'Valor {caixa_escolha1.get()} atual:    {valor_1}', fg='red').grid(row=2, column=1)
            Label(self, text=f'Valor {caixa_escolha2.get()} atual:   {valor_2}', fg='red').grid(row=3, column=1)

        bol_val1 = DoubleVar()
        bol_val2 = DoubleVar()

        Label(self, text='Valor de origem:').grid(row=0, column=0)
        valor1 = Entry(self, textvariable=bol_val1)
        valor1.grid(row=0, column=1)

        Label(self, text='Cotação de destino:').grid(row=1, column=0)
        valor2 = Entry(self, textvariable=bol_val2)
        valor2.grid(row=1, column=1)

        Button(self, text='Somar', command=conta).grid(row=2, column=0)
        Label(self, text='').grid(row=4, column=0)
        Label(self, text='Convertido para:').grid(row=4, column=0)

        caixa_escolha1 = ttk.Combobox(self, values=['BRL', 'USD', 'EUR', 'GBA', 'JPY', 'CHF', 'CAD', 'AUT'], width=4)
        caixa_escolha1.grid(row=0, column=3)
        caixa_escolha1.current(1)

        caixa_escolha2 = ttk.Combobox(self, values=['BRL', 'USD', 'EUR', 'GBA', 'JPY', 'CHF', 'CAD', 'AUT'], width=4)
        caixa_escolha2.grid(row=1, column=3)
        caixa_escolha2.current(1)


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

        # Finalizando
        df_full = pd.read_html(str(table).replace(',', '.'))[0]
        sleep(5)

        def conta():
            print(df_full)
            df_full.head()
            caixa1 = caixa_escolha1.get()
            caixa2 = caixa_escolha2.get()

            x = df_full.loc[(df_full['Código'] == f'{caixa1}') & (df_full['BRL'] == f'{caixa2}')]
            print(x)
            df_full.loc[2]
            df1 = df_full.loc[2, [f'{caixa1}']]
            df2 = df_full.loc[2, [f'{caixa2}']]

            for l in enumerate(df1):
                valor_1 = l[1]

            for l in enumerate(df2):
                valor_2 = l[1]

            calc = valor_1 * valor_2

            Label(self, text=f'{caixa_escolha2.get()}    {calc}', fg='blue').grid(row=4, column=1)
            Label(self, text=f'Valor {caixa_escolha1.get()} atual:    {valor_1}', fg='red').grid(row=2, column=1)
            Label(self, text=f'Valor {caixa_escolha2.get()} atual:   {valor_2}', fg='red').grid(row=3, column=1)

        bol_val1 = DoubleVar()
        bol_val2 = DoubleVar()

        Label(self, text='Valor de origem:').grid(row=0, column=0)
        valor1 = Entry(self, textvariable=bol_val1)
        valor1.grid(row=0, column=1)

        Label(self, text='Cotação de destino:').grid(row=1, column=0)
        valor2 = Entry(self, textvariable=bol_val2)
        valor2.grid(row=1, column=1)

        Button(self, text='Somar', command=conta).grid(row=2, column=0)
        Label(self, text='').grid(row=4, column=0)
        Label(self, text='Convertido para:').grid(row=4, column=0)

        caixa_escolha1 = ttk.Combobox(self, values=['BRL', 'USD', 'EUR', 'GBA', 'JPY', 'CHF', 'CAD', 'AUT'], width=4)
        caixa_escolha1.grid(row=0, column=3)
        caixa_escolha1.current(1)

        caixa_escolha2 = ttk.Combobox(self, values=['BRL', 'USD', 'EUR', 'GBA', 'JPY', 'CHF', 'CAD', 'AUT'], width=4)
        caixa_escolha2.grid(row=1, column=3)
        caixa_escolha2.current(1)
