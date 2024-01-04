from tkinter import *

# Constantes de cores
BLACK = "#1e1f1e"
WHITE = "#feffff"
BLUE = "#38576b"
GRAY = "#ECEFF1"
ORANGE = "#FFAB40"

def insere_valores(event):
    display_text.set(display_text.get() + str(event))

def calcular():
    try:
        resultado = eval(display_text.get())
        display_text.set(resultado)
    except Exception as e:
        display_text.set("Erro")

def clear():
    display_text.set("")

# Criação da janela
janela = Tk()
janela.title("Calculadora")
janela.geometry("235x310")
janela.config(bg=BLACK)

# Criação do display
frame_display = Frame(janela, width=235, height=50, bg=BLUE)
frame_display.grid(row=0, column=0)

display_text = StringVar()
label_display = Label(frame_display, textvariable=display_text, width=16, height=2, padx=7,
                      relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18'), bg=BLUE, fg=WHITE)
label_display.place(x=0, y=0)

# Criação dos botões
frame_teclas = Frame(janela, width=235, height=268, bg=BLACK)
frame_teclas.grid(row=1, column=0)

buttons = [
    ("C", clear, 0, 0, 11, 2, GRAY),
    ("%", lambda: insere_valores("%"), 118, 0, 5, 2, GRAY),
    ("/", lambda: insere_valores("/"), 177, 0, 5, 2, ORANGE),
    ("7", lambda: insere_valores("7"), 0, 52, 5, 2, GRAY),
    ("8", lambda: insere_valores("8"), 59, 52, 5, 2, GRAY),
    ("9", lambda: insere_valores("9"), 118, 52, 5, 2, GRAY),
    ("*", lambda: insere_valores("*"), 177, 52, 5, 2, ORANGE),
    ("4", lambda: insere_valores("4"), 0, 104, 5, 2, GRAY),
    ("5", lambda: insere_valores("5"), 59, 104, 5, 2, GRAY),
    ("6", lambda: insere_valores("6"), 118, 104, 5, 2, GRAY),
    ("-", lambda: insere_valores("-"), 177, 104, 5, 2, ORANGE),
    ("1", lambda: insere_valores("1"), 0, 156, 5, 2, GRAY),
    ("2", lambda: insere_valores("2"), 59, 156, 5, 2, GRAY),
    ("3", lambda: insere_valores("3"), 118, 156, 5, 2, GRAY),
    ("+", lambda: insere_valores("+"), 177, 156, 5, 2, ORANGE),
    ("0", lambda: insere_valores("0"), 0, 208, 11, 2, GRAY),
    (".", lambda: insere_valores("."), 118, 208, 5, 2, GRAY),
    ("=", calcular, 177, 208, 5, 2, ORANGE)
]

for text, command, x, y, width, height, color in buttons:
    button = Button(frame_teclas, command=command, text=text, width=width, height=height,
                    bg=color, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
    button.place(x=x, y=y)

janela.mainloop()