class Car:
    """
    Автомобиль
    имеет цвет
    имеет мощность дивгателя
    имеет максимальный запас бензина в баке
    имеет расход (например 9.3 литра на 100 км)
    можно перекрасить
    можно заправить N литров
    можно проехать N киллометров
    можно узнать цвет
    мощность
    сколько осталось литров в баке
    узнать расход
    """
    color: str = 'white'  # цвет
    engine_power: int = 500  # мощность двигателя л.с
    max_fuel: int = 75  # максимальный запас бензина
    consumption: float = 10  # расход на 100км
    now_fuel: int = 0

    def __init__(self, color: str = 'black', engine_power: int = 600, max_fuel: int = 9, consumption: float = 8, now_fuel: float = 10):
        self.color = color
        self.engine_power = engine_power
        self.max_fuel = max_fuel
        self.consumption = consumption
        self.now_fuel = now_fuel

    def set_color(self, color): # Устанавливаем значение цвета
        self.color = color
        return self.color

    def get_color(self): # выводим какой цвет у машины
        return self.color

    def set_max_fuel(self, max_fuel): # меняем максимальный запас топлива
        self.max_fuel = max_fuel
        return self.max_fuel

    def get_fuel(self): # выводим максимальный запас топлива
        return self.max_fuel

    def refill(self, now_fuel): # заправляем
        if now_fuel <= self.max_fuel:
            self.now_fuel += now_fuel
        else:
            print('Брат, бак полон. Заливать больше некуда')
        return self.now_fuel



c = Car(color='Purple', engine_power=555, max_fuel=8, consumption=5, now_fuel=15)

print('Машина была такого цвета:', c.get_color())
c.set_color('Orange')
print('Вы покрасили машину в:', c.get_color())

c.set_max_fuel(60)
print('Максимальный бак:', c.get_fuel())

print(c.now_fuel)
print(c.refill(55))



