# def é utilizado para declarar um método/função
def sacar(valor): # : inicia o bloco do método sacar
    saldo = 500

# Os blocos são identificados pela identação do código, o que torna claro.
    if saldo >= valor:
        print("valor sacado!")
        print("retire o seu dinheiro na boca do caixa.")

    print("Obrigado por ser nosso cliente, tenha um bom dia!")


def depositar(valor):
    saldo = 500
    saldo += valor


sacar(1000)
