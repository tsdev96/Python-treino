"""Desafio para dizer se vai dar tweet ou não com base na quantidade de caracteres"""
T = str(input())

if len(T) <= 140:
    print("TWEET")

else:
    print("MUTE")