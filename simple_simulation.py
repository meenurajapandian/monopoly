from random import randint
import numpy as np

places = np.zeros(40, dtype=int)
position = 0
for i in range(1, 50):
    d1 = randint(1, 6)
    d2 = randint(1, 6)
    d = d1 + d2
    position += d
    if position == 30:  # Jail position
        position = 10
    elif position >= 40:
        position -= 40  # Resetting once Go is reached
    places[position] += 1

