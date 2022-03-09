
#sleep de time para gerarmos delay
from time import sleep

import pandas as pd

#biblioteca selenium webdrive e beautifulsoup respectivamente
from selenium import webdriver
from selenium.webdriver.chrome.options  import Options#implementar opções no selenium
from bs4 import BeautifulSoup


#bibliotecas de data, uso opcional
from datetime import datetime
from locale import LC_ALL, setlocale
"""
DESCRIÇÃO: A classe e métodos abaixo geram uma busca no site de apostas de futebol, 'https://www.bet365.com/#/IP/B1',
e nos retornam quais os jogos e o placar por partida que estão ocorrendo atualmente. Para isso cria-se um bot com selenium 
que faz um request e repassa para o beautifulsoup fazer a varredura e encontrar os valores pretendidos.

ATENÇÃO: Leia o arquivo README para atender os requisitos.


"""

class Aposta:
    def __init__(self):
        """
        Método inicilizador da nossa classe Aposta, aqui atribuo a instância uma URL para que WebDriver do 
        selenium faça um get e depois gere um página automatizada sem problemas de carregar a página ao lado cliente,
        assim depois passo o contéudo da página pelo self.navegador.page_source integrando o selenium com o BeautifulSoup.

        Posteriormente de forma opcional é possível configurar a hora e data para a hora local da sua máquina,
        assim encontramos a hora local e formatamos o dia e hora da partida.
        
        """
    
        #OPTATIVO para o tamanho de janela selenium: Para usar precisa descomentar as duas linhas abaixos e inserir posteriormente em "wedriver.Chrome(options=self.options)""
        #self.options = Options()
        #self.options.add_argument("--window-size=400,800")

        #Selenium
        self.url = r"https://www.bet365.com/#/IP/B1"
        self.navegador = webdriver.Chrome()
        self.navegador.get(self.url)

        sleep(2) #sleep será usado para dar tempo o contéudo da página ser gerado, uma espécie de delay

        #BeautifaulSoup
        self.navegador=self.navegador.page_source
        self.site = BeautifulSoup(self.navegador, "html.parser") #usando o beautifulsoup para retornar o html

        #definindo data local
        setlocale(LC_ALL, "pt_BR.UTF-8") 
        self.data = datetime.now() #data atual
        self.data = self.data.strftime("%A as %H:%M").capitalize()

    def buscar_jogos(self):
        """
        Método que faz uma busca do html carregado, utilizando o .findAll sobre o contéudo do objeto consumido pelo BeautifulSoup,
        por meio de div e class do contéudo busca-se o elemento na página e gera um laço que busca conteúdos em text. Quando os 
        valores são encontrados são inseridos em listas separadas e que depois são unidas em uma lista única por zip. 

        A função zip gera uma lista que contém duas listas, com valores diferentes, então é precio iterar sobre a lista maior e
        por fim unir os valores dentro das listas, tornando apto a geração de um dataframe.

        """

        elemento = self.site.findAll("div", attrs={"class": "ovm-FixtureDetailsTwoWay ovm-FixtureDetailsTwoWay-1"}) #varredura em todo html na busca das class/div

        print("------------------JOGOS AO VIVO-------------------") #estético
        lista_gols = []
        lista_time =[]
        for item in elemento: #percorre todos itens dentro do elemento que tem o findAll
            
            equipes = item.find("div", attrs={"class": "ovm-FixtureDetailsTwoWay_TeamsWrapper"}) #busca nome de times
            gols = item.find("div", attrs={"class": "ovm-StandardScores_ScoresWrapper"}) #busca gols
            
            #dando append em equipes
        
            for eqp in equipes:
                lista_time.append(eqp.text)
            
            #dando append em gols
            
            for scor in gols:
                lista_gols.append(scor.text)
            
        #unindo valores das listes de equipes e gols
        unir = zip(lista_time,lista_gols)
            

        pulo=0 #separando duas equipes por partida
        self.lista_dataframe = [] #criando uma lista para gerar nosso dataframe
        contador_p = 1
        for eqp in unir:
            #desempactondado itens da tupla [0] para nome [1] para gols
            print(f"Equipe: {eqp[0]} - Gols: {eqp[1]} → Partida: {contador_p}")
            self.lista_dataframe.append([eqp[0], eqp[1], contador_p]) #dá append da equipe os gols na lista
            pulo+=1 #pulo recebe +1 no aculumo de dois da um print vazio separando duas equipes por partidas
            
            if pulo ==2:
                contador_p +=1
                print()
                pulo=0 #pulo retorna a zero

    def gerar_dataframe(self):
        """
        Método que recebe a lista gerada pelo método buscar_jogos() e implementa com pandas um dataframe com linhas e colunas

        """
        try:
            self.df = pd.DataFrame(self.lista_dataframe, columns=["Equipe", "Gols", "Partida"]) #gera um dataframe com pandas 
            return self.df #retorna o valor do dataframe para ser instanciado opcionalmente
        except Exception as e:
            self.df= None
            print("Nenhum conteúdo foi gerado na WEB.")
            
        return self.df

    def gerar_csv(self, conjunto):
        """
        Método que recebe um valor esperado do dataframe, posteriormente verifica se é de fato uma instância de DataFrames 
        e converte o DF em csv, caso não seja  do tipo DF o csv não é gerado.

        """
        try:
            if not isinstance(conjunto, pd.DataFrame): #verificando se é instância do tipo pandas DF
                print("Não há nada para gerar um CSV")
                return 
            else:
                conjunto =conjunto.to_csv("aovivo_play.csv", index=False, sep=",", encoding="utf-8") #aqui geravmos o csv
        except TypeError as e:
            print("Erro do tipo atribuido.")
        except AttributeError as e:
            print("Erro de atributo, nada foi gerado DataFrame.")


    def ler_csv(self):
        """Método que gera a leitura do csv gerado"""
        try:
            with open("aovivo_play.csv", "r", encoding="utf-8") as file: #fazemos a abertura com encoding
                    file.seek(0)
                    for linha in file.readlines():
                        print(linha)
        except FileNotFoundError as e:
            print("Arquivo não encontrado no diretório.")



#testando no nosso módulo main

if __name__ == "__main__":

    jogos_vivo = Aposta()
    jogos_vivo.buscar_jogos()
    jogos_vivo.gerar_dataframe()
    jogos_vivo.gerar_csv(jogos_vivo.df)
    jogos_vivo.ler_csv()



                
        
        
            
        

        
