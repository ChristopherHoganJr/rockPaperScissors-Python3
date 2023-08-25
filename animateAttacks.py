from rockArt import rockArt
from paperArt import paperArt
from scissorsArt import scissorsArt

def animateAttacks(attack):
    if attack == 0:
        print(rockArt)
    elif attack == 1:
        print(paperArt)
    else:
        print(scissorsArt)