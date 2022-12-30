# Реализовать класс цифрового счетчика. В классе реализовать методы:
# начальной инициализации счётчика (предусмотреть установку счётчика значениями по умолчанию 0-100)
# (метод __init__())
# увеличения счетчика на 1 (метод increase())
# возвращения текущего значения счётчика (метод get_current_value())

class DigitalCounter:
    def __init__(self, start=0, end=100, current=None):
        self.start = start
        self.end = end
        self.current = current

    def increase(self):
        if self.current < self.end:
            self.current += 1
            return self.current
        else:
            print('Out of range')

    def get_current_value(self):
        return self.current


value_counter = DigitalCounter(current=100)
value_counter.increase()
print(value_counter.get_current_value())
