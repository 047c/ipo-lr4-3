n = int((input("Введите число (n): ")))  # Получаем число n
a = 0  # Устанавливаем значения для рассчета
b = 1
c = 0
while c < n:  # Считаем и выводим число фибоначчи
    print(a, end=", ")
    d = a + b
    a = b
    b = d
    c += 1
