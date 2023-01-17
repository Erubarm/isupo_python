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
    consumption: float = 1  # расход на 1км
    now_fuel: int = 0

    def __init__(self, color: str = 'black', engine_power: int = 600, max_fuel: int = 9, consumption: float = 8, now_fuel: float = 10):
        self.color = color
        self.engine_power = engine_power
        self.max_fuel = max_fuel
        self.consumption = consumption
        self.now_fuel: float = now_fuel

    def set_color(self, color): # Устанавливаем значение цвета
        self.color = color
        return self.color

    def get_color(self): # выводим какой цвет у машины
        return self.color

    def get_max_fuel(self): # выводим максимальный запас топлива
        return self.max_fuel

    def set_max_fuel(self, max_fuel): # меняем максимальный запас топлива
        self.max_fuel = max_fuel
        return self.max_fuel

    def get_fuel(self): # кол-во топлива на данный момент
        return self.now_fuel

    def get_consumption(self): # какой расход топлива на 1км
        return self.consumption

    def get_refill(self): # На сколько литров можно заправиться
        return self.max_fuel - self.now_fuel

    def refill(self, fuel): # Функция заправки автомобиля и условия можно ли заправить
        if self.max_fuel >= self.now_fuel:
            if fuel > c.get_refill():
                print('Нельзя заправиться больше, чем можешь')
            else:
                self.now_fuel += fuel
                return self.now_fuel
        else:
            print('Дозаправка не требуется')

    def true_distance(self): # Сколько можно проехать км при данном баке
        return self.now_fuel / self.consumption




c = Car(color='Purple', engine_power=555, max_fuel=70, consumption=5, now_fuel=15)

print('Машина такого цвета:', c.get_color())
print('Максимальный бак:', c.get_fuel())
print(f'С запасом топлива {c.get_fuel()} можно проехать {c.true_distance()}')

print()

c.set_color('Yellow')
c.set_max_fuel(60)
print(f'Машина перекрашенна в {c.get_color()}')
print(f'Максимальная вместимость бака {c.get_max_fuel()} литров')
print(f'В баке сейчас {c.now_fuel} литров')
print(f'Можно заправиться на {c.get_refill()} литров')
c.refill(6)
print(f'Можно проехать {c.true_distance()}')





