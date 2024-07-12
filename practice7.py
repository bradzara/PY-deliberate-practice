# Write a Car class with attributes for make, model, year, and color.

class Car:
  def __init__(self, make, model, year, color):
    self.make = make
    self.model = model
    self.year = year
    self.color = color

  def __str__(self):
    return f"Car(make='{self.make}', model='{self.model}', year='{self.year}', color='{self.color}')"
  
  def __repr__(self):
    return self.__str__()


  
new_car = Car("Chevy", "Impala", 1979, "black")
print(new_car)