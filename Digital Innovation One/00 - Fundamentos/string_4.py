nome = "Guilherme"

#Para passar strings de múltiplas linhas, é necessário passar 3 aspas duplas ou simples. São chamados de strings triplas.

mensagem = f"""
   Olá meu nome é {nome},
 Eu estou aprendendo Python.
     Essa mensagem tem diferentes recuos.
"""

print(mensagem)

#Ele preserva todos os recuos. Seja dentro de uma variável ou direto num print.
print(
    """
    ============= MENU =============

    1 - Depositar
    2 - Sacar
    0 - Sair

    ================================

            Obrigado por usar nosso sistema!!!!
"""
)
