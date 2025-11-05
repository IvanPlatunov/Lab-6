class Car():
    def __init__(self, volume, consumption, speed):
        self.consumption = consumption
        self.volume = volume
        self.speed = speed

    def get_consuption(self):
        return self.consumption
    def set_consumption(self, cons):
        self.consumption = cons

    def get_volume(self):
        return self.volume
    def set_volume(self, vol):
        self.volume = vol

    def get_speed(self):
        return self.speed
    def set_speed(self, sp):
        self.speed = sp
    
    def count_dist(self):
        return round(self.volume/self.consumption*100, 2)
    
    def count_ratio(self, amount):
        return round(amount/(self.consumption*2.5), 2)
    def info(self):
        print('Объем бака:', self.volume)
        print('Расход топлива:', self.consumption)
        print('Средняя скорость:', self.speed)
        print('Пройденное расстояние до опустошения бака:', self.count_dist())


class Truck(Car):
    class_name = 'Грузовик'
    def __init__(self, volume, consumption, speed, capacity):
        super().__init__(volume, consumption, speed)
        self.capacity = capacity

    def get_capacity(self):
        return self.capacity
    def set_capacity(self, cap):
        self.speed = cap

    def info(self):
        print('-'*10+Truck.class_name+'-'*10)
        super().info()
        print('Отношение грузоподъемности к количеству топлива на 250 км:', self.count_ratio(self.capacity))
        print('Грузоподъёмность:', self.capacity)
    def __add__(self, other):
        return Truck(self.volume+other.volume, (self.consumption+other.consumption)//2, (self.speed+other.speed)//2, self.capacity+other.capacity)
        


class Bus(Car):
    class_name = 'Автобус'
    def __init__(self, volume, consumption, speed, seats):
        super().__init__(volume, consumption, speed)
        self.seats = seats

    def get_seats(self):
        return self.seats
    def set_seats(self, seats):
        self.seats = seats
    
    def info(self):
        print('-'*10+Bus.class_name+'-'*10)
        super().info()
        print('Отношение количества пассажиров к количеству топлива на 250 км:', self.count_ratio(self.seats))
        print('Колчиество сидений:', self.seats)
    def __add__(self, other):
        return Bus(self.volume+other.volume, (self.consumption+other.consumption)//2, (self.speed+other.speed)//2, self.seats+other.seats)

truck = Truck(80, 20, 70, 15)
bus = Bus(50, 9, 50, 20)
truck.info()
print()
bus.info()

print('-'*50)
bus2 = Bus(65, 12, 55, 40)
bus3 = bus+bus2
print('Перегрузка __add__: объем бака и грузоподъемность/количество сидений складываются, из скорости и расхода вычисляется среднее')
print('Пример: bus(50, 9, 50, 20) + bus2(65, 12, 55, 40)')
print(bus3.info())