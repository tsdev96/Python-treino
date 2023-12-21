# ### Cuidados!
# 1. Whatsapp não gosta de nenhum tipo de automação
# 2. Isso pode dar problema porque o whatsapp pode bloquear se entender que está fazendo uso indevido.
# 3. Isso não é o uso da API oficial do Whatsapp, o próprio whatsapp tem uma API oficial. Se o seu objetivo é fazer envio em massa 
#ou criar bots que respondem automaticamente no whatsapp, então use a API oficial.
# 4. Objetivo é 100% educacional

# - Vamos usar o Selenium
# - Temos 1 ferramenta muito boa alternativas:
#     - Usar o wa.me (mais fácil, mais seguro, mas mais demorado)

#É necessário ter um xlsx com as colunas pessoa, mensagem e número preenchida com antecedência. Vamos ler essa planilha para automatizar.
from IPython.display import display
import pandas as pd
#Usando o pandas para ler a armazenando os dados da tabela
contatos_df = pd.read_excel("Enviar.xlsx")
display(contatos_df)#Mostrando os dados capturados da tabela pelo Pandas


from selenium import webdriver #Importando selenium e webdriver que ajuda em toda a comunicação entre PYTHON e web
from selenium.webdriver.common.keys import Keys #Importando as keys que servem para enviar as mensagens e interagir com teclado
import time #Importando a biblioteca para usar o time
import urllib

navegador = webdriver.Chrome() #Estamos criando um navegador novo
navegador.get("https://web.whatsapp.com/") #get permite irmos para links
#find_elements é um método de navegador(webdriver)
while len(navegador.find_elements_by_id("side")) < 1: #Esperando aparecer o id side(área do código onde ficam as conversas) O Python espera a 
#página carregar a este ponto
    time.sleep(1)#Aguarda 1 segundo antes de seguir

# já estamos com o login feito no whatsapp web
for i, mensagem in enumerate(contatos_df['Mensagem']):#Para cada mensagem na coluna mensagem, guardaremos o valor da coluna em mensagem. 
    #enumerate pega a coluna.
    pessoa = contatos_df.loc[i, "Pessoa"] #No i estamos pegando o índice da tabela e com a mensagem estamos pegando a mensagem da tabela em 
    #cada passada do for
    numero = contatos_df.loc[i, "Número"]
    texto = urllib.parse.quote(f"{pessoa}! {mensagem}")#Com essa biblioteca e função fazemos o parse do texto em urlcode
    link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
    navegador.get(link)
    while len(navegador.find_elements_by_id("side")) < 1:
        time.sleep(1)
    navegador.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]').send_keys(Keys.ENTER)
    #Buscando o xpath da caixa de mensagem para dar enter
    time.sleep(10)
        
    



