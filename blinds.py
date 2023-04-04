# import potrzebnych modułów
from machine import Pin
import time

# Ustawienie pinów mikrokontrolera
IN1 = Pin(2, Pin.OUT)
IN2 = Pin(3, Pin.OUT)
IN3 = Pin(4, Pin.OUT)
IN4 = Pin(5, Pin.OUT)
IN5 = Pin(6, Pin.OUT)
IN6 = Pin(7, Pin.OUT)
IN7 = Pin(8, Pin.OUT)
IN8 = Pin(9, Pin.OUT)
button1 = Pin(14, Pin.IN, Pin.PULL_DOWN)
button2 = Pin(15, Pin.IN, Pin.PULL_DOWN)
led = Pin(25, Pin.OUT)

krok = 0

# Zdefiniowano listy z pinami dla dwóch silników
pins = [IN1, IN2, IN3, IN4]
pins2 = [IN8, IN7, IN6, IN5]

# Wartości, które będą przekazywane do pinów, aby obracać silnikiem krokowym
UP = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
DOWN = [[0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0], [1, 0, 0, 0]]

while True:
    led.value(1)  # zapal diodę LED
    while button1.value() == 1:  # jeżeli wciskamy przycisk 1
        while krok < 6000:  # wykonaj maksymalnie 6000 kroków silnikiem
            for step in UP:  # wykonaj jedno obroty silnika (pełna sekwencja kroków)
                for i in range(len(pins)):
                    pins[i].value(step[i])  # przekaż wartości do pinów, aby obrócić silnik
                    pins2[i].value(step[i])
                    led.value(0)  # wyłącz diodę LED
                    time.sleep(0.001)  # poczekaj przez krótki czas między krokami
            krok = krok + 1
        krok = 0  # zresetuj kroki, aby móc wykonać kolejne obroty
        for i in range(len(pins)):
            pins[i].value(0)  # wyłącz wszystkie piny, aby zatrzymać silnik
            pins2[i].value(0)
    while button2.value() == 1:  # jeżeli wciskamy przycisk 2, wykonaj obroty w przeciwną stronę
        while krok < 6000:
            for step in DOWN:
                for i in range(len(pins)):
                    pins[i].value(step[i])
                    pins2[i].value(step[i])
                    time.sleep_us(600)  # poczekaj przez krótki czas między krokami
            krok = krok + 1
        krok = 0
        for i in range(len(pins)):
            pins[i].value(0)	# wyłącz wszystkie piny, aby zatrzymać silnik
            pins2[i].value(0)
    time.sleep(0.2)	# Oczekiwanie na wciśnięcie przycisku