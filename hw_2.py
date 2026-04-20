# ЗАДАЧА 1
def task_1() -> None:
    # 5 переменных с разными типами данных
    var_int: int = 42
    var_float: float = 3.14159
    var_str: str = "testtest"
    var_list: list = [1, 2, 3, 4, 5]
    var_bool: bool = True

    print(f"Тип var_int: {type(var_int)}")
    print(f"Тип var_float: {type(var_float)}")
    print(f"Тип var_str: {type(var_str)}")
    print(f"Тип var_list: {type(var_list)}")
    print(f"Тип var_bool: {type(var_bool)}")


# ЗАДАЧА 2
def task_2() -> None:

    a: list = [1, 2, 3, 5, 8, 13, 21]

    # Вывод первых трёх значений (индексы 0, 1, 2)
    print(f"Вывод первых трех значений: {a[0]}, {a[1]}, {a[2]}")

    # Это последовательность Фибоначчи (каждое следующее число = сумма двух предыдущих)


# ЗАДАЧА 3
def task_3(number: int | float) -> int | float:

    return number ** 2


# ВЫЗОВ ФУНКЦИЙ
if __name__ == "__main__":
    print("ЗАДАЧА 1")
    task_1()

    print("\nЗАДАЧА 2")
    task_2()

    print("\nЗАДАЧА 3")
    result = task_3(7)
    print(f"Квадрат числа 7 = {result}")

    # Можно проверить с другими числами:
    print(f"Квадрат числа 4.5 = {task_3(4.5)}")
    