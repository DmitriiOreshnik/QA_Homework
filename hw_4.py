# ЗАДАЧА 1
class Rectangle:
    """
    Класс прямоугольника с шириной и высотой.
    """
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
    
    def area(self) -> float:
        """Расчёт площади прямоугольника."""
        return self.width * self.height
    
    def perimeter(self) -> float:
        """Расчёт периметра прямоугольника."""
        return 2 * (self.width + self.height)


# ЗАДАЧА 2
class Math:
    """
    Класс с базовыми математическими операциями.
    """
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b
    
    def addition(self) -> None:
        """Сложение a и b."""
        print(f"Сложение: {self.a} + {self.b} = {self.a + self.b}")
    
    def multiplication(self) -> None:
        """Умножение a и b."""
        print(f"Умножение: {self.a} * {self.b} = {self.a * self.b}")
    
    def division(self) -> None:
        """Деление a на b."""
        if self.b != 0:
            print(f"Деление: {self.a} / {self.b} = {self.a / self.b}")
        else:
            print("Ошибка: деление на ноль!")
    
    def subtraction(self) -> None:
        """Вычитание b из a."""
        print(f"Вычитание: {self.a} - {self.b} = {self.a - self.b}")

# ЗАДАЧА 3
class SidebarButton:
    """
    Класс для кнопки в сайдбаре сайта.
    """
    def __init__(self, text: str, btn_type: str = "Кнопка", locator: str = ""):
        self.text = text
        self.type = btn_type
        self.locator = locator
    
    def click(self) -> str:
        """Имитация клика по кнопке."""
        return f"Клик по кнопке {self.text}"


# ВЫЗОВ ФУНКЦИЙ 
if __name__ == "__main__":
    
    # ЗАДАЧА 1
    print("ЗАДАЧА 1: Прямоугольники")
    
    rect1 = Rectangle(5, 10)
    rect2 = Rectangle(7.5, 3.2)
    rect3 = Rectangle(100, 50)
    
    rectangles = [rect1, rect2, rect3]
    
    for i, rect in enumerate(rectangles, 1):
        print(f"\nПрямоугольник #{i}:")
        print(f"  Размер: {rect.width} x {rect.height}")
        print(f"  Площадь: {rect.area()}")
        print(f"  Периметр: {rect.perimeter()}")
    
    
    # ЗАДАЧА 2
    print("\n\nЗАДАЧА 2: Математические операции")
    
    math1 = Math(10, 5)
    math1.addition()
    math1.multiplication()
    math1.division()
    math1.subtraction()
    
    print("\nПроверка деления на ноль:")
    math2 = Math(20, 0)
    math2.division()
    
    
    # ЗАДАЧА 3
    print("\n\nЗАДАЧА 3: Кнопки сайдбара")
    
    # Создаём объекты кнопок
    buttons = [
        SidebarButton("Text Box"),
        SidebarButton("Check Box"),
        SidebarButton("Radio Button"),
        SidebarButton("Web Tables"),
        SidebarButton("Buttons"),
        SidebarButton("Links"),
        SidebarButton("Broken Links - Images"),
        SidebarButton("Upload and Download"),
        SidebarButton("Dynamic Properties"),
    ]
    
    # Выводим текст каждой кнопки
    print("Текст кнопок:")
    for btn in buttons:
        print(f"  • {btn.text} (тип: {btn.type})")
    
    # Кликаем по каждой кнопке
    print("\nКлики по кнопкам:")
    for btn in buttons:
        print(f"  → {btn.click()}")