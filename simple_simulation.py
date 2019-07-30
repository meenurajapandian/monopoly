from random import randint
import numpy as np

places = np.zeros(40, dtype=int)
position = 0
for i in range(1, 100000):
    d1 = randint(1, 6) #Dice 2
    d2 = randint(1, 6) #Dice 1
    d = d1 + d2
    position += d
    if position == 30:  # Jail position
        places[position] += 1 # Actually in Jail taken away
        position = 10 # But the position is set to 10 which is actually the jail
    elif position >= 40:
        position -= 40  # Resetting once Go is reached
        places[position] += 1
    else:
        places[position] += 1 # All other cases. Because actually in jail is taken apart from the place


t_places = np.zeros((40,500), dtype=int)
for i in range(1,100000): # Repeat timeline simulation 100 times
    position = 0
    for j in range(1,500): # For 500 time points
        d1 = randint(1, 6)  # Dice 2
        d2 = randint(1, 6)  # Dice 1
        d = d1 + d2
        position += d
        if position == 30:  # Jail position
            t_places[position,j] += 1  # Actually in Jail taken away
            position = 10  # But the position is set to 10 which is actually the jail
        elif position >= 40:
            position -= 40  # Resetting once Go is reached
            places[position,j] += 1
        else:
            places[position,j] += 1

