#У репозиторії python-hw-1 стоворити файл calculate.py який повинен місти программу вирішення базових арифметичних операцій.
#Програма повинна зчитувати аргументи командної строки і виконувати арифметичні операції. За допомогою модуля sys.
#Необхідна підтримка 4 базових арифметичних операцій: +, -, *, /
#додавання, віднімання, множення, ділення.
#Результат виконання арифметичної операції потрібно виводити у консоль.
#Программа повинна адекватно оброблювати помилки.
#Программа повинна запускатись наступним чином: python calculate.py 2 + 2
#Тестові запуски:
#python calculate.py 2 + 2 -> 4
#python calculate.py 2 - 200 -> -198
#python calculate.py 2 * 8 -> 16
#python calculate.py 200 / 2 -> 100

import sys

Argumentu = sys.argv
Deistvie = Argumentu[2]

try:
    Arg1 = int(Argumentu[1])
    Arg2 = int(Argumentu[3])
    KolArg = len(Argumentu)
    if KolArg == 4:
        match Deistvie:
            case "+":
                print ("Сумма:", int(Arg1) + int(Arg2))
            case "-":
                print ("Разница:", int(Arg1) - int(Arg2))
            case "*":
                print ("Умножение:", int(Arg1) * int(Arg2))
            case "/":
                if int(Arg2) == 0:
                    print ("Ошибка деление на 0")
                else:
                    print ("Деление:", int(Arg1) / int(Arg2))
    else:
        print ("Неверное количество аргументов")
except ValueError:
    print ("Введите числа")
