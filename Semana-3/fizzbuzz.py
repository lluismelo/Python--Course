num = int(input("Digite um número inteiro: "))
fizz = num % 3
buzz = num % 5

if (fizz == 0 and buzz == 0):
    print("FizzBuzz")
else:
    print(num)