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
