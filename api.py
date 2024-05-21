
from requests import get
rost = input('Введите ваш рост(rost) = ')
ves = input('Введите ваш вес(ves) = ')
razmer = input('Введите ваш размер обуви(razmer) = ')
print(get(f'http://localhost:5000/api?temp={rost}&pulse={ves}&pain_level={razmer}').json())