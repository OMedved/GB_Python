import time


class TrafficLight:
    __color = ['Красный', 'Жёлтый', 'Зелёный']

    def running(self):
        light = 0
        while light <= 3:
            print(f'Горит \n {TrafficLight.__color[light]}')
            if light == 0:
                time.sleep(7)
            elif light == 1:
                time.sleep(2)
            elif light == 2:
                time.sleep(1)
                light = -1
            light += 1


drive = TrafficLight()
drive.running()
