# Calculadora em Python

print("\n******************* Python Calculator *******************")

def menu():

    print("1. Adição\n")
    print("2. Subtração\n")
    print("3. Divisão\n")
    print("4. Multiplicação\n")

def adicao(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def divisao(num1, num2):
    if(num2 != 0):
        return num1 / num2
    else:
        print("Não existe divisão por zero!")

def multiplicacao(num1, num2):
    return num1 * num2

menu()

op = input("Digite sua opção: ")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundoo número: "))

if (op == '1'):
    print(num1, "+", num2, "=", adicao(num1,num2))
elif (op == '2'):
    print(num1, "-", num2, "=", subtracao(num1,num2))
elif (op == '3'):
    print(num1, "/", num2, "=", divisao(num1,num2))
elif (op == '4'):
    print(num1, "*", num2, "=", multiplicacao(num1,num2))
else:
    print("Opção inválida!")