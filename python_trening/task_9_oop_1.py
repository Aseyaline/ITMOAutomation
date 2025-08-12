# Создайте класс Input, принимающий 1 аргумент при инициализации (Loc)
# Создайте объект search (экземпляр класса Input)
# Выведите в консоль значение аргумента Loc, объекта search

# *** Добавьте к классу Input атрибут объекта text
# В этом же файле создайте: Классы Button, Title, Link
# Для каждого класса пропишите атрибуты text и loc
# Создайте каждому из 4х классов объекты с любыми данными
# Выведите в консоль text и loc каждого класса


# в файле task_9_oop_1.py
# c. наследуйте все классы от класса Checks
# i. чтобы использовать класс из другого файла его нужно импортировать
# from название файла(без расширения) import название класса
# d. переделайте все 4 класса в файле task_9_oop_1.py так чтоб в объектах можно было использовать методы родительского класса
# e. распечатайте в консоль результаты метода .check_text() вызванного от каждого объекта классов файла task_9_oop_1.py


from task_9_checks import Checks

class Input(Checks):

    def __init__(self, loc, text):
        super().__init__(loc)
        self.text = text

class Button(Checks):

    def __init__(self, loc, text):
        super().__init__(loc)
        self.text = text

class Title(Checks):

    def __init__(self, loc, text):
        super().__init__(loc)
        self.text = text

class Link(Checks):
    def __init__(self, loc, text):
        super().__init__(loc)
        self.text = text

search = Input('Input#search', 'Поиск')
click = Button('Button#click','Кнопка')
text = Title('Title#text', 'Заголовок')
type = Link('Link#type', 'Ссылка')

print(search.loc, search.text)
print(click.loc, click.text)
print(text.loc, text.text)
print(type.loc, type.text)

print(search.check_text())
print(click.check_text())
print(text.check_text())
print(type.check_text())