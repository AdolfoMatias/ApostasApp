#chamando a classe implementa em bet365
from bet365 import Aposta
""" 
A documentação e códigos estão no arquivo bet365.py caso tenha interesse de ler todo o código abra o conteúdo original,
este módulo main apenas roda o código que fora gerado em bet365.py.
"""

#testando no nosso múdlo main
if __name__ == "__main__":
    jogos_vivo = Aposta()
    jogos_vivo.buscar_jogos()
    jogos_vivo.gerar_dataframe()
    jogos_vivo.gerar_csv(jogos_vivo.df)
    jogos_vivo.ler_csv()