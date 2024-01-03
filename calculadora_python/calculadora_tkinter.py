                                                #Calculadora com interface gráfica, toda em Python.

#Importando Tkinter, biblioteca para usar gui
from tkinter import *

                                    ##CRIANDO LÓGICA PARA INSERIR VALORES, CALCULAR VALORES E LIMPAR VALORES##
todos_inputs = ''

def insere_valores(event):

    global todos_inputs
    todos_inputs = todos_inputs + str(event)

    texto_no_display.set(todos_inputs)

def calcular():
    global todos_inputs
    resultado = eval(todos_inputs)

    texto_no_display.set(resultado)

def clear():
    global todos_inputs
    todos_inputs = ""
    texto_no_display.set("")




                                            ###CRIANDO TODA A INTERFACE POR ETAPAS###
# Cores utilizadas, esboço:
black = "#1e1f1e"
white = "#feffff"
blue = "#38576b"
gray = "#ECEFF1"
orange = "#FFAB40"

        ###CRIANDO JANELA DA APLICAÇÃO###

#Criando janela da aplicação e título
janela = Tk()
janela.title("Calculadora")

#Definindo dimensões da janela e cor
janela.geometry("235x310")
janela.config(bg=black)

#Criando um frame dentro da janela, que será nosso display, que mostra resultados
frame_display = Frame(janela, width=235, height=50, bg=blue)
frame_display.grid(row=0, column=0)

#Criando um frame dentro de janela, que receberá as teclas
frame_teclas = Frame(janela, width=235, height=268, bg=black)
frame_teclas.grid(row=1, column=0)


        ###CRIANDO LABEL, DISPLAY DE RESULTADOS###
texto_no_display = StringVar() #Esta variável precisa ser str por que a propriedade dentro do label textvariable recebe apenas str

label_display = Label(frame_display, textvariable=texto_no_display, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18'), bg=blue, fg=white)
label_display.place(x=0, y=0)


        ###CRIANDO BOTÕES DENTRO DO SEGUNDO FRAME DE BOTÕES###

#Cada botão recebe um command com lambda, chamando a função insere valores com parâmetro event, que é o caracter do botão.

##PRIMEIRA FILEIRA##
#Button Clear, o command dele chama a função clear
button_c = Button(frame_teclas, command=clear, text="C", width=11, height=2, bg=gray, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_c.place(x=-1, y=0)

#Button Módulo
button_modulo = Button(frame_teclas, command= lambda: insere_valores("%") ,text="%", width=5, height=2, bg=gray, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_modulo.place(x=118, y=0)

#Button Divisão
button_divisao = Button(frame_teclas, command= lambda: insere_valores("/"), text="/", width=5, height=2, bg=orange, fg=black, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_divisao.place(x=177, y=0)


##SEGUNDA FILEIRA##
#Button 7
button_7 = Button(frame_teclas, command= lambda: insere_valores("7"), text="7", width=5, height=2, bg=gray, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_7.place(x=0, y=52)

#Button 8
button_8 = Button(frame_teclas, command= lambda: insere_valores("8"), text="8", width=5, height=2, bg=gray, fg=black, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_8.place(x=59, y=52)

#Button 9
button_9 = Button(frame_teclas, command= lambda: insere_valores("9"), text="9", width=5, height=2, bg=gray, fg=black, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_9.place(x=118, y=52)

#Button Multiplicação
button_multiplicacao = Button(frame_teclas, command= lambda: insere_valores("*"), text="*", width=5, height=2, bg=orange, fg=black, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_multiplicacao.place(x=177, y=52)


##TERCEIRA FILEIRA##
#Button 4
button_4 = Button(frame_teclas, command= lambda: insere_valores("4"), text="4", width=5, height=2, bg=gray, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_4.place(x=0, y=104)

#Button 5
button_5 = Button(frame_teclas, command= lambda: insere_valores("5"), text="5", width=5, height=2, bg=gray, fg=black, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_5.place(x=59, y=104)

#Button 6
button_6 = Button(frame_teclas, command= lambda: insere_valores("6"), text="6", width=5, height=2, bg=gray, fg=black, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_6.place(x=118, y=104)

#Button Subtração
button_subtracao = Button(frame_teclas, command= lambda: insere_valores("-"), text="-", width=5, height=2, bg=orange, fg=black, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_subtracao.place(x=177, y=104)


##QUARTA FILEIRA##
#Button 1
button_1 = Button(frame_teclas, command= lambda: insere_valores("1"), text="1", width=5, height=2, bg=gray, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_1.place(x=0, y=156)

#Button 2
button_2 = Button(frame_teclas, command= lambda: insere_valores("2"), text="2", width=5, height=2, bg=gray, fg=black, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_2.place(x=59, y=156)

#Button 3
button_3 = Button(frame_teclas, command= lambda: insere_valores("3"), text="3", width=5, height=2, bg=gray, fg=black, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_3.place(x=118, y=156)

#Button Adição
button_adicao = Button(frame_teclas, command= lambda: insere_valores("+"), text="+", width=5, height=2, bg=orange, fg=black, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_adicao.place(x=177, y=156)


##QUINTA FILEIRA##
#Button Zero
button_zero = Button(frame_teclas, command= lambda: insere_valores("0"), text="0", width=11, height=2, bg=gray, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_zero.place(x=-1, y=208)

#Button ponto
button_ponto = Button(frame_teclas, command= lambda: insere_valores("."), text=".", width=5, height=2, bg=gray, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_ponto.place(x=118, y=208)

#Button igual, o command dele chama a função calcular
button_igual = Button(frame_teclas, command=calcular, text="=", width=5, height=2, bg=orange, fg=black, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_igual.place(x=177, y=208)

janela.mainloop() #Chamando janela




