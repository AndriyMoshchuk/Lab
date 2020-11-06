import math
from math import sqrt

print ("Перша константа", False)
print ("Друга константа", True)
print ("2 в степені 11", pow(2,11))
print ("Піднесення -2 в степінб 9 і пошук модулю", abs(pow(-2, 9)))

for i in range(20):
    if i >= 5:
        print(i)

Numb = -4
try:
    print("Що буде якщо", sqrt(Numb), "?")  
except Exception as e:
    print(e)
finally:
    print ("А вот воно що!")    

with open("README.md", "w") as f:
    f.write("Hello Andrii")

lambda_function = lambda first, last: f'This kod was writted by {first} {last}'
print("This is simple function", lambda_function)
print("This is her call:", lambda_function('Andrii', 'Moshchuk'))