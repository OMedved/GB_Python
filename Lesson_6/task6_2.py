class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def weight(self):
        return (self._length * self._width * 25 * thickness) / 1000


thickness = int(input('Введите толщину дорожного полотна в сантиметрах: '))
road = Road(20, 5000)
print(f'Вес дорожного полотна составляет {road.weight()} тонн.')
