class Button:

    # Aтрибут класса. Наследуется у всех экземпляров. Объявляется в классе как переменные
    type: str = 'Кнопка'


    # Атрибуты обычные. Объявляются в конструкторе (в инит), работают как аргументы функции.
    def __init__(self, text, link):
        self.text = text
        self.link = link

# Создаем экземпляры класса
home = Button('Домой', '/home')
catalog_msk = Button('Каталог', '/msk/catalog')

# Получаем доступ к атрибутам
print(home.text)
print('Кнопка ' + home.text + ' имеет ссылку ' + home.link)

print('\n')

print(catalog_msk.text)
print('Кнопка ' + catalog_msk.text + ' имеет ссылку ' + catalog_msk.link)


class ButtonTwo:

    def __init__(self, text, link, loc):
        self.text = text
        self.link = link
        self.loc = loc

    def click(self):
        return 'Клик по локатору - {}'.format(self.loc)

# Создаем экземпляры класса
home_two = ButtonTwo('Домой', '/home', 'button#home')

# Вызываем метод. Отличие вызова метода от аргумента - передаем фигурные скобки
print(home_two.click())