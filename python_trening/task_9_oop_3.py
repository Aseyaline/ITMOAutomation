# Создайте класс Soda (для определения типа газированной воды),
# принимающий 1 аргумент при инициализации (отвечающий за добавку к выбираемому лимонаду).
# В этом классе реализуйте метод show_my_drink(), выводящий на печать "Газировка и {ДОБАВКА}" в случае наличия добавки,
# а иначе отобразите следующую фразу: "Обычная газировка".


class Soda:
    def __init__(self, soda_flavor=None):
        self.soda_flavor = soda_flavor

    def show_my_drink(self):
        if self.soda_flavor:
            print('Газировка и {}'.format(self.soda_flavor)) # Или можно написать (f'Газировка и {self.soda_flavor}')
        else:
            print('Обычная газировка')


soda_flavor_true = Soda('Лимон')
soda_flavor_false = Soda()

soda_flavor_true.show_my_drink()
soda_flavor_false.show_my_drink()