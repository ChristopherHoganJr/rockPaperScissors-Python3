from rockArt import rockArt
from paperArt import paperArt
from scissorsArt import scissorsArt

def animateAttacks(attack):
    if attack == 1:
        print(rockArt)
    elif attack == 2:
        print(paperArt)
    else:
        print(scissorsArt)