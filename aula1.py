
valores = [200,300,400,500,600]

with open("novo_arquivo", "w") as arquivo:
    for valor in valores:
        arquivo.write(str(valor) + "\n")
        print(valor)
    