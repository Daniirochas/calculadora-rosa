import os
from colorama import init, Fore, Style
import math

init(autoreset=True)

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu():
    print(Style.BRIGHT + Fore.LIGHTMAGENTA_EX + "\n============================")
    print("      CALCULADORA PINK     ")
    print("============================\n")
    print(Fore.MAGENTA + " [1] Adição")
    print(Fore.MAGENTA + " [2] Subtração")
    print(Fore.MAGENTA + " [3] Multiplicação")
    print(Fore.MAGENTA + " [4] Divisão")
    print(Fore.MAGENTA + " [5] Sair")
    print(Fore.MAGENTA + " [6] Potência (x^y)")
    print(Fore.MAGENTA + " [7] Raiz quadrada")
    print(Fore.MAGENTA + " [8] Porcentagem")
    print(Fore.MAGENTA + " [9] Resto da divisão")
    print(Fore.MAGENTA + " [10] Média entre dois números\n")

def pegar_numero(prompt):
    while True:
        try:
            return float(input(Style.BRIGHT + Fore.LIGHTMAGENTA_EX + prompt))
        except ValueError:
            print(Fore.LIGHTRED_EX + "Entrada inválida. Tente novamente.")

def calcular(operacao):
    if operacao in ['1', '2', '3', '4', '6', '8', '9', '10']:
        num1 = pegar_numero("Digite o primeiro número: ")
        num2 = pegar_numero("Digite o segundo número: ")

    if operacao == '1':
        return f"Resultado: {num1 + num2}"
    elif operacao == '2':
        return f"Resultado: {num1 - num2}"
    elif operacao == '3':
        return f"Resultado: {num1 * num2}"
    elif operacao == '4':
        if num2 == 0:
            return Fore.LIGHTRED_EX + "Erro: divisão por zero!"
        return f"Resultado: {num1 / num2}"
    elif operacao == '6':
        return f"Resultado: {num1 ** num2}"
    elif operacao == '7':
        num = pegar_numero("Digite um número para calcular a raiz quadrada: ")
        if num < 0:
            return Fore.LIGHTRED_EX + "Erro: não existe raiz real de número negativo."
        return f"Resultado: {math.sqrt(num)}"
    elif operacao == '8':
        return f"{num1}% de {num2} = {num1 * num2 / 100}"
    elif operacao == '9':
        if num2 == 0:
            return Fore.LIGHTRED_EX + "Erro: divisão por zero!"
        return f"Resto da divisão: {num1 % num2}"
    elif operacao == '10':
        return f"Média: {(num1 + num2) / 2}"

def main():
    while True:
        limpar_tela()
        mostrar_menu()
        operacao = input(Style.BRIGHT + Fore.LIGHTMAGENTA_EX + "Escolha uma operação (1-10): ")

        if operacao == '5':
            print(Fore.LIGHTGREEN_EX + "\nSaindo... Obrigada por usar a calculadora!")
            break

        if operacao not in [str(i) for i in range(1, 11)]:
            print(Fore.LIGHTRED_EX + "Opção inválida. Tente novamente.")
            input("Pressione Enter para continuar...")
            continue

        resultado = calcular(operacao)
        if resultado:
            print(Fore.LIGHTMAGENTA_EX + f"\n{resultado}")

        input(Style.BRIGHT + Fore.LIGHTMAGENTA_EX + "\nPressione Enter para continuar...")

if __name__ == "__main__":
    main()
