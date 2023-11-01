'''
Study about variables and constants in Python
Author: Marcos Souza
'''
#Variables

#Attributing values to variables using in one line
conta, nome, saldo, limite = 0, "", 0.0, 0.0

#Attributing values to variables using in multiple lines (recommended). using input function.
conta = input("Digite o número da conta: ")
nome = input("Digite o nome do cliente: ")
saldo = float(input("Digite o saldo da conta: "))
limite = float(input("Digite o limite da conta: "))
print("O número da conta é:", conta)
print("O nome do cliente é:", nome)
print("O saldo da conta é:", saldo)
print("O limite da conta é:", limite)

saldo = 'marcos'

#Constants

