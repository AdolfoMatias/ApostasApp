1 DESCRIÇÃO
A classe e métodos do arquivo bet365.py geram uma busca no site de apostas de futebol, 'https://www.bet365.com/#/IP/B1',
e nos retornam quais os jogos e o placar por partida que estão ocorrendo no momento. Para isso, cria-se um bot com selenium 
que faz um request e repassa para o beautifulsoup, para que este possa fazer a varredura e encontrar os valores pretendidos.

2 OPCIONAL
Adicionalmente cria-se com o pyinstaller um executável, que fará todo o processo apenas executando o arquivo, 
garanta que o chromedrive.exe esteja na mesma pasta do arquivo executável.


3 REQUISITOS
	Usar no seu terminal: pip install -r Requeriments.txt


- Esta versão foi realizada para windows, porém há métodos semelhantes para Linux, deixarei informações na documentação com o selenium.
-  Além dos Requerimentes.txt, é necessário baixar o driver do chrome que seja baseado na sua versão e máquina, para isso você precisa 
   saber no painel de 'ajuda > sobre o chrome' e buscar sua versão. Baixe a versão de acordo com o seu chrome e coloque na pasta do arquivo .py desejado.



4 - TRANSFORMANDO EXECUTÁVEL

Transformando em .exe:
No seu terminal na pasta do arquivo "exemplo.py" você deve executar a linha:

pyinstaller --noconsole --name="AoVivo" --icon="pyi.ico"  --add-data="pyi.ico;." --add-binary=".\chromedriver.exe;." --onefile bet365.py

4.1 Dicionário do pyinstaller:
- noconsole: não exibe o console ao clicar no executável;
- name: Nome do arquivo gerado no .exe;
- icon: imagem em formato de icone para o executável;
- add-data: inserir arquivo adicional ao exceutável;
- add-binary:  arquivo binário inserido ao .exe;
- onefile: arquivo a ser gerado do .py.

4.2 Arquivos/Pastas Geradas pelo pyinstaller:

build/
dist/
AoVivo.spec

4.3 Como usar o executável:

Entre na pasta dist/ e execute o arquivo AoVivo.exe
Garanta que o arquivo chromedriver.exe esteja junto
	

5 DOCUMENTAÇÃO REFERENCIAL E DOWNLOADS DO DRIVER:

 - Selenium: https://selenium-python.readthedocs.io/
 - Chrome Driver: https://chromedriver.chromium.org/downloads
 - Firefox Driver(Opção 2): https://github.com/mozilla/geckodriver/releases