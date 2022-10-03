# Лабораторная работа № 4
# Прокофьев Андрей Фт-210008

from pyconvertnum import convert_to_word

def get_int(text: str = "Введите числа через пробел", value_count: int = None) -> list[int]:
    resource = list(map(int, input(text).split(" ")))

    if value_count:
        if isinstance(value_count, int):
            if value_count < len(resource):
                resource = resource[:value_count]

        else:
            raise TypeError("value_count should be int or NoneType")

    return resource


def fix_index(list_to_fix):
    return [{"index": i, "value": list_to_fix[i]} for i in range(len(list_to_fix))]


def main(N, first_line, second_line):
    first_dict, second_dict = fix_index(first_line), fix_index(second_line)

    first_dict.sort(key = lambda x: x["value"], reverse=False)
    second_dict.sort(key = lambda x: x["value"], reverse=True)

    result = [{
        "sotrudnik_id": first_dict[i]["index"] + 1, 
        "taxi_id": second_dict[i]["index"] + 1, 
        "taxi_cost": first_dict[i]["value"] * second_dict[i]["value"]}
        for i in range(N)]

    result.sort(key=lambda x: x["sotrudnik_id"])
    print("Отсортированные пары:\n")
    for i in range(N):
        print("Номер такси для сотрудника №{sotrudnik_id}: {taxi_id}".format(
            **result[i]
        ))

    print()
    total_sum = sum(map(lambda x: x['taxi_cost'], result))
    total_sum_word = convert_to_word(total_sum)

    print(f'Общая стоимость развоза всех сотрудников составляет {total_sum} р.')
    print(f'Сумма словами: {total_sum_word}')
    

if __name__ == "__main__":
    N = int(input("Введите N >> "))
    first_line = get_int("Введите первые N чисел (расстояние до дома сотрудника) >> ", N) # расстояния для сотрудников
    second_line = get_int("Введите вторые N чисел (тариф такси за 1 км.) >> ", N) # цена за 1 км езды
    print()
    main(N, first_line, second_line)