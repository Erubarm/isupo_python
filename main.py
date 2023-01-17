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
    color: str = 'white' # цвет
    engine_power: int = 500 # мощность двигателя л.с
    max_tank: int = 75 # максимальный запас бензина
    consumption: float = 10 # расход на 100км

    def __init__(self, color: str = 'black', engine_power: int = 600, max_tank: int = 9, consumption: float = 8):

        self.color = color
        self.engine_power = engine_power
        self.max_tank = max_tank
        self.consumption = consumption

    def set_color(self, color):
        self.color = color

c = Car('White', 555, 11, 7)
print(c.set_color('Orange'))





