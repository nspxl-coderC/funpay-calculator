

import os
history = []


def menu():
    os.system('cls' if os.name == 'nt' else 'clear' )

    Green = "\033[32m"
    Cyan = "\033[36m"
    reset = "\033[0m"
    syperduperRED = "\033[1;31m"
    YELLOW = "\033[33m"
    Orange = "\033[38;2;255;100;0m"

    print(rf"""{Orange}
    __        __                             _____           _     
    \ \      / /__ _ _   _ ___  ___    _    |_   _|__   ___ | | ___ 
     \ \ /\ / / _` | | | / __|/ _ \   (_)     | |/ _ \ / _ \| |/ __|
      \ V  V / (_| | |_| \__ \ (_) |   _      | | (_) | (_) | |\__ \
       \_/\_/ \__,_|\__, |___/\___/   (_)     |_|\___/ \___/|_||___/
                    |___/                                          
         {reset}""")
    print("1. Калькулятор")
    print("2. Таблица")
    print(f"0. {syperduperRED}Выход{reset}")



def tablitci():
     Green = "\033[32m"
     Cyan = "\033[36m"
     reset = "\033[0m"
     syperduperRED = "\033[1;31m"
     YELLOW = "\033[33m"
     Orange = "\033[38;2;255;100;0m"

     if not history:
         print("Привет! Твоя таблица пустая выполни расчеты в калькуляторе и возвращайся!")
         input("Нажмите Enter, чтобы выйти...")
         return



     for item in history:
         print(f"Товар: {item['название товара']} | {Green}Выгода: {item['выгода']}{reset}")
         print(
             f"| {item['название товара']:<15} | {item['цена']:<12.2f} | {item['закупка']:<10.2f} | {Green}{item['выгода']:<10.2f}{reset} |")
         print("-" * 60)
         input("Нажмите Enter, чтобы выйти...")
         return








def calculator():
    while True:

        os.system('cls' if os.name == 'nt' else 'clear')

        if history:
            print("Все товары....")
            for item in history:
                print(f"Товар: {item['название товара']} | Выгода: {item['выгода']}")
                print("-" * 30 + "\n")



        Green = "\033[32m"
        Cyan = "\033[36m"
        reset = "\033[0m"
        syperduperRED = "\033[1;31m"
        YELLOW = "\033[33m"



        nazvanie = input(f"ВВЕДИ {Cyan}НАЗВАНИЕ ТОВАРА{reset}")


        x = float(input("Цена продажи на фп 14%"))


        #x - цена продажи на фп
        #0.14 - комка на фп
        #y - фп комкой
        #d - чистая прибыль после комок фп
        #b - комка процент
        #v - комка
        #a - цена товара с комкой
        #c - выгода без комки поставщика
        #z - цена закупки


        y = x * 0.14

        d = x - y


        z = float(input("Цена закупки"))

        while True:

            otvet = input(f"Нужно умножать? {Green}ДА{reset}/{syperduperRED}НЕТ{reset}").lower()

            if otvet in ["да", "нет", "lf", "ytn", "Да", "ДА", "НЕТ", "Нет", "YTN", "Ytn", "LF", "Lf"]:
                break
            else:
                print("ТОЧНО ПРОПИШИ ЭТО")



        if otvet.lower() == "да":
            b = float(input("Ввведи число в виде десятичной дроби"))
            v = z * b
            a = z + v
            print(f"{Cyan}{nazvanie}{reset} Выгода 1 шт  {Green}{d - a}{reset}")

        else :
            c = d - z
            print(f"{Cyan}{nazvanie}{reset} Выгода 1 шт  {Green}{c}{reset}")

        a = 0
        c = 0

        product_data = {
            "название товара": nazvanie,
            "цена": d,
            "закупка": a if otvet in ["да", "lf", "ДА", "LF", "Lf"] else z,
            "выгода": (d - a) if otvet in ["да", "lf", "ДА", "LF", "Lf"] else c
        }
        history.append(product_data)


        popitkodva = input(f"Посчитать еще один товар? {Green}Да{reset} / {syperduperRED}Нет{reset}").lower()
        if popitkodva.lower() == "нет":
            print(f"{YELLOW}Удачи!{reset}")
            return

    input("Нажмите Enter, чтобы выйти...")


while True:
    reset = "\033[0m"
    YELLOW = "\033[33m"
    menu()
    choice = input("Выбери раздел!")

    if choice == "1":
     calculator()

    elif choice == "2":
     tablitci()

    elif choice == "0":
     print(f"{YELLOW}пока пока!{reset}")
     break
    else:
         print("Выбери что-то из списка!")