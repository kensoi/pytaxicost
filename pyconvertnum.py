list_a = ["", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
list_a_wrub = ["рублей", "один рубль", "два рубля", "три рубля", "четыре рубля", "пять рублей", "шесть рублей", "семь рублей", "восемь рублей", "девять рублей"]
list_b = ["десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семнадцать", "девятнадцать"]
list_c = ["", "десять", "двадцать", "тридцать", "сорок", "пятдесят", "шестдесят", "семьдесят", "восемьдесят", "девяносто"]
list_d= ["", "сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"]

list_e = ["тысяч", "одна тысяча", "две тысячи", "три тысячи", "четыре тысячи", "пять тысяч", "шесть тысяч", "семь тысяч", "восемь тысяч", "девять тысяч", "десять тысяч"]

def convert_to_word(value, DEBUG = False):
    """
    Перевод числа из цифровой формы в словесную
    Debug: выводить процесс вычисления в терминал
    """
    if DEBUG:
        print(value)
        print()

    response = ""
    a = value // 100000
    b = value % 100000 // 10000
    c = value % 10000 // 1000
    d = value % 1000 // 100
    e = value % 100 // 10
    f = value % 10

    isGreaterThan1000 = False

    # abc

    if a > 0:
        response += list_d[a] + " "
        isGreaterThan1000 = True
    if DEBUG: print(f"{a=}\n{response=}")
    
    if b >= 0:
        if a == 0 and b == 0:
            pass

        elif b == 1:
            response += list_b[c] + " тысяч"
            isGreaterThan1000 = True

        else:
            response += list_c[b] + " "
            isGreaterThan1000 = True
    if DEBUG: print(f"{b=}\n{response=}")
    
    if b != 1:
        if a == 0 and b == 0 and c == 0:
            pass
        else:
            response += list_e[c] + " "
            isGreaterThan1000 = True

    if DEBUG: print(f"{c=}\n{response=}")
    
    # def

    if d > 0:
        response += list_d[d] + " "
    if DEBUG: print(f"{d=}\n{response=}")
    
    if e >= 0:
        if d > 0 and e == 0:
            pass

        elif e == 1:
            response += list_b[f] + " рублей"

        else:
            response += list_c[e] + " "

    if DEBUG: print(f"{e=}\n{response=}")
    
    if e != 1:
            response += list_a_wrub[f] + " "

    if DEBUG: print(f"{f=}\n{response=}")

    while "  " in response:
        response = response.replace("  ", " ")

    if response[0] == " ":
        response = response[1:]

    if response[-1] == " ":
        response = response[:-1]

    if DEBUG:
        print("test return: ", response)
    return response
