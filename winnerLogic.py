def winnerLogic(playerChoice, computerChoice):

    winTable = {
        0: ["tie", "lose", "win"],
        1: ["win", "tie", "lose"],
        2: ["lose", "win", "tie"]
    }
    return winTable[playerChoice][computerChoice]