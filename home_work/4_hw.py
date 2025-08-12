# 1. создайте класс прямоугольника.
# a. атрибуты - прямоугольнику можно задать ширину и высоту
# b. методы - реализуйте 2 метода:
# i. расчет площади прямоугольника
# ii. расчет периметра прямоугольника
# c. создайте 3 объекта, рассчитайте площадь и периметр для каждого. Результаты выводить в консоль.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

# Площадь прямоугольника
    def S(self):
        return self.width * self.height
# Периметр прямоугольника
    def P(self):
        return 2 * (self.width + self.height)

obj_1 = Rectangle(100, 100)
obj_2 = Rectangle(120, 65)
obj_3 = Rectangle(105, 148)

print(f'Прямоугольник №1 имеет Площадь: {obj_1.S()}, Периметр: {obj_1.P()}\n'
f'Прямоугольник №2 имеет Площадь: {obj_2.S()}, Периметр: {obj_2.P()}\n'
f'Прямоугольник №3 имеет Площадь: {obj_3.S()}, Периметр: {obj_3.P()}')


# 2. Создайте класс Math.
# a. Создайте два атрибута — a и b.
# b. Напишите методы
# i. addition — сложение,
# ii. multiplication — умножение,
# iii. division — деление,
# iv. subtraction — вычитание.
# При передаче в методы параметров a и b с ними нужно производить соответствующие действия и печатать ответ.

class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        print(self.a + self.b)
    def subtraction(self):
        print(self.a - self.b)
    def multiplication(self):
        print(self.a * self.b)
    def division(self):
        print(self.a / self.b)

Math(3,2).addition()
Math(3,2).subtraction()
Math(3,2).multiplication()
Math(3,2).division()


# 3. откройте страницу https://demoqa.com/text-box
# На странице присутствует сайдбар (меню слева)
# a. Создайте объекты для каждой кнопки 2-го уровня вложенности (“Text Box” и т.п.)
# Для этого опишите класс.
# Каждый объект должен содержать в себе:
# - текст кнопки (пример: “Text Box”)
# - тип - одинаковый для всех “Кнопка”
# - локатор - не заполнять, сделать по умолчанию пустой строкой
# Также на кнопку можно нажать - реализуйте метод. Метод возвращает текст “Клик по кнопке { ТЕКСТ КНОПКИ }”
# b. выведите текст для каждой кнопки
# c. вызовите “Клик” для каждой кнопки

class Elements:
    def __init__(self, text, type = "Кнопка", loc = ""):
        self.text = text
        self.type = type
        self.loc = loc

    def click(self):
        print(f'Клик по кнопке {self.text}')

text_box = Elements('Text Box')
check_box = Elements('Check Box')
radio_button = Elements('Radio Button')
web_tables = Elements('Web Tables')
buttons = Elements('Buttons')
links = Elements('Links')
broken_links = Elements('Broken Links - Images')
upload_and_download = Elements('Upload and Download')
dynamic_properties = Elements('Dynamic Properties')

print(text_box.text)
text_box.click()

print(check_box.text)
check_box.click()

print(radio_button.text)
radio_button.click()

print(web_tables.text)
web_tables.click()

print(buttons.text)
buttons.click()

print(links.text)
links.click()

print(broken_links.text)
broken_links.click()

print(upload_and_download.text)
upload_and_download.click()

print(dynamic_properties.text)
dynamic_properties.click()