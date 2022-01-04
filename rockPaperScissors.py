from animateAttacks import animateAttacks
from computerLogic import computerLogic

# Introduction
print('2022 Rock Paper Scissors Tournament')
# Save player's name to variable
playerName = input('What is your name: ')
# Ask player which attack to use
print('_______________')
print('|             |')
print('| Attack Menu |')
print('| 1. Rock     |')
print('| 2. Paper    |')
print('| 3. Scissors |')
print('|_____________|')
playerAttack = int(input(f'{playerName} which attack do you pick (1|2|3): '))
# Do not let player continue unless they've picked an attack
while playerAttack < 1 or playerAttack > 3:
    print('You must enter 1, 2, or 3')
    playerAttack = int(input(f'{playerName} which attack do you pick: '))
# Battle stage begins
print(f'{playerName} has chosen')
# Animate player's attack
animateAttacks(playerAttack)

print('vs')

# Computer to run a random number generator between 1 and 3 for attack
computerAttack = computerLogic()
# Animate the computer's attack
animateAttacks(computerAttack)

# Find the winner
if playerAttack == 1 and computerAttack == 3:
    winner = playerName
elif playerAttack == 2 and computerAttack == 1:
    winner = playerName
elif playerAttack == 3 and computerAttack == 2:
    winner = playerName
elif playerAttack == computerAttack:
    winner = 'Tie'
else:
    winner = 'Computer'

# Announce winner
if winner == playerName:
    print(f'Congratulations {playerName}!! You Win!!')
elif winner == 'Tie':
    print(f'{playerName} you tied with the computer! Try again!')
else:
    print(f'Sorry {playerName}. The Computer is the winner!!')
