#
# Exemplos de como trabalhar com arquivos
#
import os
from os import path
import shutil #Módulo que permite realizar cópias de arquivos

def copiaArquivo():
    if path.exists("NovoArquivo.txt"):
        pathAtual = path.realpath("NovoArquivo.txt") #Retornando o path real do arquivo indicado
        novoPath = pathAtual + ".bkp" #Adicionando o sufixo .bkp
        shutil.copy(pathAtual, novoPath) #Passando como parâmetro origem e destino desse arquivo

        shutil.copystat(pathAtual, novoPath) #Além de copiar o path estamos aqui copiando as permissões do path indicado.

#copiaArquivo()

def renomearArquivo():
    if path.exists("NovoArquivo.txt.bkp"):
        os.rename("NovoArquivo.txt.bkp", "ArquivoAlterado.txt")

renomearArquivo()


