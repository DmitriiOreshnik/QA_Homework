# 2
def task_2(num1: float, num2: float) -> None:
    """
    Принимает два числа и выводит наибольшее.
    """
    if num1 > num2:
        print(f"Наибольшее число: {num1}")
    elif num2 > num1:
        print(f"Наибольшее число: {num2}")
    else:
        print("Числа равны")


#  3
def task_3(num1: float, num2: float) -> None:
    """
    Принимает два числа. Если разница между ними 135, выводит "yes", иначе "No".
    """
    if abs(num1 - num2) == 135:
        print("yes")
    else:
        print("No")


# 4
def task_4(month: int) -> None:
    """
    Принимает номер месяца (1-12) и выводит название сезона.
    """
    if month in [12, 1, 2]:
        print("зима")
    elif month in [3, 4, 5]:
        print("весна")
    elif month in [6, 7, 8]:
        print("лето")
    elif month in [9, 10, 11]:
        print("осень")
    else:
        print("Некорректный номер месяца")


# 5
def task_5(num1: float, num2: float, num3: float) -> None:
    """
    Принимает три числа. Если все больше 10, выводит "yes", иначе "no".
    """
    if num1 > 10 and num2 > 10 and num3 > 10:
        print("yes")
    else:
        print("no")


# 6
def task_6(numbers: list) -> int:
    """
    Принимает список из 5 чисел. Возвращает количество положительных чисел.
    """
    count = 0
    for num in numbers:
        if num > 0:
            count += 1
    print(f"Количество положительных чисел: {count}")
    return count


# 7
def task_7(years: int, months: int) -> None:
    """
    Принимает количество лет и месяцев. Выводит общее количество дней.
    (Считаем, что в каждом месяце 29 дней).
    """
    total_months = (years * 12) + months
    total_days = total_months * 29
    print(f"Всего дней: {total_days}")

#  ВЫЗОВ ФУНКЦИЙ
if __name__ == "__main__":
    print("=== ЗАДАЧА 2 ===")
    task_2(200, 12)
    task_2(15, 8)
    task_2(5, 10)

    print("\n=== ЗАДАЧА 3 ===")
    task_3(200, 65)
    # Разница 135 → yes
    task_3(100, 50)
    # Разница 50 → No

    print("\n=== ЗАДАЧА 4 ===")
    task_4(1)
    # зима
    task_4(6)
    # лето
    task_4(10)
    # осень
    task_4(3)
    # весна

    print("\n=== ЗАДАЧА 5 ===")
    task_5(11, 12, 15)
    # yes
    task_5(5, 12, 15)
    # no

    print("\n=== ЗАДАЧА 6 ===")
    task_6([-5, 3, -1, 7, 2])
    # 3 положительных

    print("\n=== ЗАДАЧА 7 ===")
    task_7(1, 2)
    # 1 год 2 месяца = 14 месяцев × 29 = 406 дней
    task_7(0,2)
    # 0 лет 2 месяца = 2 месяца × 29 = 58 дней