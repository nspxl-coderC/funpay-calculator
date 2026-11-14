

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
    print("")
    print("2. Таблица")
    print("")
    print("3. Желаемая прибыль")
    print("")
    print("-----------------------------")
    print(f"0. {syperduperRED}Выход{reset}")
    print("-----------------------------")

#ета деф функция прибыль вся вайбкод тк я тупоголовый математек)) и нихуя не понял как ее сделать😭 (но доработки делал уже я 😈😈)
def pribil():
    while True:

        os.system('cls' if os.name == 'nt' else 'clear')

        Green = "\033[32m"
        Cyan = "\033[36m"
        reset = "\033[0m"
        syperduperRED = "\033[1;31m"
        YELLOW = "\033[33m"
        Orange = "\033[38;2;255;100;0m"


        komka_funpay = 0.12


        while True:
            try:
                x = float(input("Привет, введи свою желаемую прибыль с товара! --- "))
                break
            except ValueError:
                print(f"{syperduperRED}Ошибка! Введи число.{reset}")


        while True:
            try:
                b = float(input("Теперь введи стоимость товара при закупке --- "))
                break
            except ValueError:
                print(f"{syperduperRED}Ошибка! Введи число.{reset}")

        while True:
            komisia = input("Была ли комиссия при покупке товара? Да/Нет --- ").lower()
            if komisia in ["да", "нет", "lf", "ytn"]:
                break
            else:
                print(f"{syperduperRED}Пропиши еще раз!{reset}")

        v_pokupki = 0.0
        if komisia in ["да", "lf"]:
            while True:
                try:
                    procent = float(input("Введи комиссию при покупке в процентах (например, 2) --- "))
                    if procent >= 0:
                        v_pokupki = procent / 100
                        break
                    else:
                        print(f"{syperduperRED}Процент не может быть отрицательным!{reset}")
                except ValueError:
                    print(f"{syperduperRED}Ошибка! Введи число.{reset}")

        sebestoimost = b + (b * v_pokupki)
        itog_cena = (sebestoimost + x) / (1 - komka_funpay)
        birzha_rub = itog_cena - (sebestoimost + x)

        print(f"\n{Cyan}--- ИТОГ ---{reset}")
        print(f"Реально ты потратил на закупку: {YELLOW}{sebestoimost:.2f} руб.{reset}")
        print(f"Выставить на бирже нужно за: {Green}{itog_cena:.2f} руб.{reset}")
        print(f"Биржа заберет свои 12%: {Orange}{birzha_rub:.2f} руб.{reset}")
        print(f"Твоя чистая прибыль: {Green}{x:.2f} руб.{reset}")

        eze = input(f"Посчитать еще один товар? {Green}Да{reset} / {syperduperRED}Нет{reset}").lower()
        if eze.lower() == "нет":
            print(f"{YELLOW}Удачи!{reset}")
            return




def tablitci():

     os.system('cls' if os.name == 'nt' else 'clear')

     Green = "\033[32m"
     Cyan = "\033[36m"
     reset = "\033[0m"
     syperduperRED = "\033[1;31m"
     YELLOW = "\033[33m"
     Orange = "\033[38;2;255;100;0m"

     if not history:
         print(f"Привет! Твоя таблица {syperduperRED}пустая{reset} выполни расчеты в калькуляторе и возвращайся!")
         print("--------------------")
     input("Нажмите Enter, чтобы выйти... ")
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



        nazvanie = input(f"ВВЕДИ {Cyan}НАЗВАНИЕ ТОВАРА{reset} --- ")

        while True:
            try:
               x = float(input("Цена Продажи --- "))
               break
            except ValueError:
                print("Напиши число! ")



        while True:
            f = input("Комиссия продажи 14% или 12%? --- ")

            if f in ["14", "12"]:
                break
            else:
                print(f"{syperduperRED}Укажи 14 или 12{reset}")

        if f == "14":
            q = x * 0.14
            d = x - q
        else:
            w = x * 0.12
            d = x - w




        #x - цена продажи на фп
        #0.14 - комка на фп
        #y - фп комкой
        #d - чистая прибыль после комисиий
        #b - процент комисии закупки товара
        #v - комииссия
        #a - цена товара с комисиией
        #c - выгода без комки поставщика
        #z - цена закупки




        while True:
            try:
                 z = float(input("Цена закупки"))
                 break
            except ValueError:
                print("Напиши число! ")

        while True:

            otvet = input(f"Нужно умножать? {Green}ДА{reset}/{syperduperRED}НЕТ{reset}").lower()

            if otvet in ["да", "нет", "lf", "ytn", "Да", "ДА", "НЕТ", "Нет", "YTN", "Ytn", "LF", "Lf"]:
                break
            else:
                print(f"{syperduperRED}ТОЧНО ПРОПИШИ ЭТО{reset}")



        if otvet.lower() in ['lf', 'да']:
            while True:
                try:
                    b = float(input("Ввведи число! ( --- "))
                    if b >=0:
                        a = b / 100
                        break
                    else:
                        print(f"{syperduperRED}Процент не может быть отрицательным! {reset}")
                except ValueError:
                    print("Введи число! ")

            v = z * a
            m = z + v
            print(f"НАЗВАНИЕ ТОВАРА --- {Cyan}{nazvanie}{reset}")
            print(f"ЦЕНА ПРОДАЖИ --- {Green}{x:.2f}{reset} ")
            print(f"ЦЕНА ПОКУПКИ --- {YELLOW}{m:.2f}{reset}")
            print(f"ВЫГОДА --- {Green}{d - m:.2f}{reset}")


        else :
            c = d - z
            print(f"НАЗВАНИЕ ТОВАРА --- {Cyan}{nazvanie}{reset}")
            print(f"ЦЕНА ПРОДАЖИ --- {Green}{x:.2f}{reset} ")
            print(f"ЦЕНА ПОКУПКИ --- {YELLOW}{z:.2f}{reset}")
            print(f"ВЫГОДА --- {Green}{c:.2f}{reset}")



        product_data = {
            "название товара": nazvanie,
            "цена": d,
            "закупка": m if otvet in ["да", "lf", "ДА", "LF", "Lf"] else z,
            "выгода": (d - m) if otvet in ["да", "lf", "ДА", "LF", "Lf"] else c
        }
        history.append(product_data)

        while True:
            popitkodva = input(f"Посчитать еще один товар? {Green}Да{reset} / {syperduperRED}Нет{reset}").lower()
            if popitkodva.lower() in ['ytn', 'нет', 'lf', 'да']:
                break
            else:
                print("Напиши Да/Нет! ")

        if popitkodva.lower() in ['ytn', 'нет']:
            print(f"{YELLOW}Удачи!{reset}")
            return

    input("Нажмите Enter, чтобы выйти...")


while True:
    reset = "\033[0m"
    YELLOW = "\033[33m"
    menu()
    choice = input("Выбери раздел! ")

    if choice == "1":
     calculator()

    elif choice == "2":
     tablitci()
    elif choice == "3":
        pribil()

    elif choice == "0":
     print(f"{YELLOW}пока пока!{reset}")
     break
    else:

         print("Выбери что-то из списка!")