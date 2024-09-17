print("vamos começar a viagem")
kwh = float(input("digite a quantidade de kwh cosumidas"))
instalação = input("digite o tipo de instalação, 'r' para residencia, 'i' para industria e 'c' para comercio")

total_consumido = kwh * instalação

if instalação ==  "r" and kwh <= 500:
    valor1 = kwh * 0,40
    print(valor1)

if instalação ==  "r" and kwh >= 500:
    valor2 = kwh * 0,65
    print(valor2)
    
if instalação ==  "i" and kwh <= 5000:
    valor3 = kwh * 0,55
    print(valor3)

if instalação ==  "i" and kwh >= 5000:
    valor4 = kwh * 0,60
    print(valor4)

if instalação ==  "c" and kwh <= 1000:
    valor5 = kwh * 0,55
    print(valor5)

if instalação ==  "c" and kwh >= 1000:
    valor6 = kwh * 0,60
    print(valor6)

total_consumido = kwh * instalação