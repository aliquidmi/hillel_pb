class Counter:

   def __init__(self, current: int = 1, min_value: int = 0, max_value: int = 10) -> None:
       self.current = current
       self.min_value = min_value
       self.max_value = max_value

   def set_max(self, max_max: int) -> None:
       if max_max < self.min_value:
           raise ValueError("Максимум не може бути меншим за мінімум")
       self.max_value = max_max
       if self.current > self.max_value:
           self.current = self.max_value

   def set_min(self, min_min: int) -> None:
       if min_min > self.max_value:
           raise ValueError("Мінімум не може бути більшим за максимум")
       self.min_value = min_min
       if self.current < self.min_value:
           self.current = self.min_value

   def set_current(self, start: int) -> None:
       if start < self.min_value or start > self.max_value:
           raise ValueError("Початкове значення має бути в межах мінімуму та максимуму")
       self.current = start

   def step_up(self) -> None:
       if self.current >= self.max_value:
           raise ValueError("Достигнут максимум")
       self.current += 1

   def step_down(self) -> None:
       if self.current <= self.min_value:
           raise ValueError("Достигнут минимум")
       self.current -= 1

   def get_current(self) -> int:
       return self.current


counter = Counter()
counter.set_current(7)
counter.step_up()
counter.step_up()
counter.step_up()
assert counter.get_current() == 10, 'Test1'
try:
    counter.step_up()  # ValueError
except ValueError as e:
    print(e)  # Достигнут максимум
assert counter.get_current() == 10, 'Test2'

counter.set_min(7)
counter.step_down()
counter.step_down()
counter.step_down()
assert counter.get_current() == 7, 'Test3'
try:
    counter.step_down()  # ValueError
except ValueError as e:
    print(e)  # Достигнут минимум
assert counter.get_current() == 7, 'Test4'
