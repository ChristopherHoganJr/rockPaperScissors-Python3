from animateAttacks import animateAttacks
from computerLogic import computerLogic
from winnerLogic import winnerLogic

gameActive = True

totalRounds = 0
totalWins = 0


# Introduction
print('2023 Rock Paper Scissors Tournament')
# Save player's name to variable
playerName = input('What is your name: ')
while(gameActive):
    if(totalRounds > 0):
        print(f'Round {totalRounds+1}!')
        print(f"Your win rate is {totalWins / totalRounds * 100:.2f}%")
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
    animateAttacks(playerAttack-1)

    print('vs')

    # Computer to run a random number generator between 0 and 2 for attack
    computerAttack = computerLogic()
    # Animate the computer's attack
    animateAttacks(computerAttack)

    # Find the winner
    outcome = winnerLogic(playerAttack-1, computerAttack)

    # Announce winner
    if outcome == "win":
        print(f'Congratulations {playerName}!! You Win!!')
        totalWins += 1
    elif outcome == 'tie':
        print(f'{playerName} you tied with the computer! Try again!')
    else:
        print(f'Sorry {playerName}. The Computer is the winner!!')

    # Update total rounds
    totalRounds += 1

    # Ask player if they want to play again
    playAgain = input('Do you want to play again (y/n): ').lower()
    if(playAgain != 'y'):
        print(f'Thanks for playing {playerName}!')
        print(f'You played {totalRounds} rounds and won {totalWins} times!')
        gameActive = False
    
    
