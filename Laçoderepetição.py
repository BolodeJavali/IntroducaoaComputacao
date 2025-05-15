# Pedir para ao usuário digitar um novo número, somar e parar até ele digitar 0
while True:
  numero = int(input("Digite um número (ou 0 para sair) "))
  if numero==0:
    break
  else:
    print(f"O número digitado foi: {numero}\n")
    numero = numero + numero
    print(f"A soma dos números é {numero}\n")