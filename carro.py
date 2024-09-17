dias = 60
preço_por_km = 0.15

dias_alugados = float(input("digite quantos dias o carro ficou alugado "))
km_percorrido = float(input("digite quantos km foram percorridos "))

custo_da_diaria = dias*dias_alugados 
custo_do_km = preço_por_km*km_percorrido
custo_final = custo_da_diaria + custo_do_km

print(f"a quatidade a pagar seré de {custo_final}")

