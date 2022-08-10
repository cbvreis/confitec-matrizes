from random import randint

import psutil


class Matriz:
    def __init__(self, linhas):
        self.linhas = linhas
        self.colunas = linhas
        self.matriz = []
        for i in range(linhas):
            self.matriz.append([])
            for j in range(self.colunas):
                self.matriz[i].append(randint(0, 10))

    def __str__(self):
        return str(self.matriz)

    def __mul__(self, outra):
        if self.colunas != outra.linhas:
            return "Impossivel multiplicar"
        else:
            resultado = []
            for i in range(self.linhas):
                resultado.append([])
                for j in range(outra.colunas):
                    resultado[i].append(0)
                    for k in range(self.colunas):
                        resultado[i][j] += self.matriz[i][k] * outra.matriz[k][j]
            return resultado


if __name__ == "__main__":

    linhas = int(input("Digite a quantidade de linhas da matriz: "))
    try:
        matriz1 = Matriz(linhas)
        matriz2 = Matriz(linhas)
    except:
        print("Erro ao criar matriz")
        exit()
    print("Matriz 1: ", matriz1)
    print("Matriz 2: ", matriz2)
    print("Produto: ", matriz1 * matriz2)
    exit()
