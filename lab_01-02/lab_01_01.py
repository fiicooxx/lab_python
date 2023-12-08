## 1
import datetime


current_time = datetime.datetime.now()
name = input("Podaj imie: ")
age = int(input("Podaj wiek: "))
print(f"Cześć {name}! ")
print(f"Twoje imię ma {len(name)} liter i zaczyna się od {name[0]}")
print(f"Teraz masz {age}, a za rok będzie to {age + 1}. Rok urodzenia to {current_time.year - age}")
