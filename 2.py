def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fib(n-1) + fib (n-2)

n = int(input('Введите, какой член последовательности Фибоначчи рассчитать: '))
print(fib(n))
