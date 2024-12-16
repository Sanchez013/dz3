class Person:
    """Клас для моделювання людини у симуляції."""
    
    def __init__(self, name, age, health=100):
        """
        Ініціалізує об'єкт класу Person.
        
        :param name: Ім'я людини
        :param age: Вік людини
        :param health: Рівень здоров'я людини (від 0 до 100)
        """
        self.name = name
        self.age = age
        self.health = health
    
    def work(self, hours):
        """
        Моделює роботу людини, що впливає на її рівень здоров'я.
        
        :param hours: Кількість годин роботи
        """
        health_decrease = hours * 2  # Кожна година роботи зменшує здоров'я на 2 одиниці
        self.health -= health_decrease
        if self.health < 0:
            self.health = 0
    
    def rest(self, hours):
        """
        Моделює відпочинок людини, що відновлює її рівень здоров'я.
        
        :param hours: Кількість годин відпочинку
        """
        health_increase = hours * 3  # Кожна година відпочинку відновлює 3 одиниці здоров'я
        self.health += health_increase
        if self.health > 100:
            self.health = 100
    
    def __str__(self):
        return f"{self.name}, Вік: {self.age}, Здоров'я: {self.health}"


class Workplace:
    """Клас для моделювання робочого місця, де люди працюють."""
    
    def __init__(self, name, max_employees):
        """
        Ініціалізує об'єкт класу Workplace.
        
        :param name: Назва робочого місця
        :param max_employees: Максимальна кількість працівників
        """
        self.name = name
        self.max_employees = max_employees
        self.employees = []
    
    def add_employee(self, person):
        """
        Додає працівника на робоче місце, якщо є вільне місце.
        
        :param person: Об'єкт класу Person
        """
        if len(self.employees) < self.max_employees:
            self.employees.append(person)
            print(f"{person.name} додано до {self.name}.")
        else:
            print(f"Немає місць для {person.name} у {self.name}.")
    
    def simulate_work_day(self, hours):
        """
        Симулює робочий день для всіх працівників.
        
        :param hours: Кількість годин роботи
        """
        print(f"Симуляція робочого дня ({hours} годин) у {self.name}.")
        for employee in self.employees:
            employee.work(hours)
            print(f"{employee.name} працював(ла) {hours} годин. Здоров'я тепер: {employee.health}.")
    
    def __str__(self):
        employee_names = ', '.join([employee.name for employee in self.employees]) or 'Немає працівників'
        return f"{self.name} (Максимум працівників: {self.max_employees})\nПрацівники: {employee_names}"


# Демонстрація роботи симуляції
if __name__ == "__main__":
    # Створення людей
    person1 = Person("Олександр", 25)
    person2 = Person("Ірина", 30)
    person3 = Person("Олег", 40)
    
    # Створення робочого місця
    office = Workplace("Офіс IT-компанії", max_employees=2)
    
    # Додавання працівників
    office.add_employee(person1)
    office.add_employee(person2)
    office.add_employee(person3)  # Цей працівник не буде доданий через обмеження місць
    
    print(office)  # Інформація про робоче місце
    
    # Симуляція робочого дня
    office.simulate_work_day(hours=8)
    
    # Люди відпочивають
    person1.rest(hours=5)
    person2.rest(hours=3)
    
    print(person1)  # Інформація про стан людини
    print(person2)  # Інформація про стан людини
