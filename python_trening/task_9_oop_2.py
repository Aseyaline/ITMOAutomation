# Создайте класс Page принимающий 1 аргумент при инициализации url
# В этом классе реализуйте метод get() который выводит url
# Создайте объект home и вызовите метод get()

class Page:
    def __init__(self, url):
        self.url = url

    def get(self):
        print(self.url)

home = Page('/home')
home.get()

