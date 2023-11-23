def fib(n, allNumbers):
    if n in allNumbers:
        return allNumbers[n]
    if n <= 1:
        return n
    allNumbers[n] = fib(n-1, allNumbers) + fib(n-2, allNumbers)
    return allNumbers[n]

allNumbers = {}
while True:
    numero = int(input("Qué número quieres calcular? "))
    print(fib(numero, allNumbers))
