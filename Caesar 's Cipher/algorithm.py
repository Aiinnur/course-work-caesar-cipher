def caesar(text, variables):
    # Четыре словаря под русские и английские символы, большие и маленькие.
    upper_eng_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_eng_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    upper_rus_alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    lower_rus_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

    str="" #Строка, которую будем возвращать

    # Объявляем цикл for. Количество итераций равно длине строки text.
    for i in range(len(text)):

        # Задаем локальные переменные: длину алфавита и значения словарей.
        if variables[1] == 0:
            alphas = 32
            low_alphabet = lower_rus_alphabet
            upp_alphabet = upper_rus_alphabet
        if variables[1] == 1:
            alphas = 26
            low_alphabet = lower_eng_alphabet
            upp_alphabet = upper_eng_alphabet

        # Если text[i] является буквой:
        if text[i].isalpha():

            # Находим место символа text[i] в словаре upp_alphabet либо low_alphabet.
            if text[i] == text[i].lower():
                place = low_alphabet.index(text[i])
            if text[i] == text[i].upper():
                place = upp_alphabet.index(text[i])

            # Если нужно дешифровать, то:
            if variables[0] == 1:
                # Находим индекс для измененного символа.
                # Новый ндекс = Старый индекс - Шаг % Длина алфавита
                index = (place - 3) % alphas


            # Если нужно зашифровать, то:
            elif variables[0] == 0:
                # Находим индекс для измененного символа.
                # Новый ндекс = Старый индекс + Шаг % Длина алфавита
                index = (place + 3) % alphas

            # Выводим измененный символ.
            if text[i] == text[i].lower():
                str += low_alphabet[index]
            if text[i] == text[i].upper():
                str += upp_alphabet[index]

                # Если text[i] не является буквой:
        else:
            # Делаем print этого символа без изменений.
            str += text[i]
    return str
