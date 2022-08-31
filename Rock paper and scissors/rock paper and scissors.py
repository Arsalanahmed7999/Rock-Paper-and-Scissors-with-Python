from random import randint
randomComp = ['Rock', 'Paper', 'Scissors']
comp = randint(1,3)
Computer = randomComp[comp - 1]

while True:
    player = input('Choose Rock (r) , Paper (p) or Scissors (s) : \n')
    # Player chooses Rock
    if((player == 'r' or player == 'Rock') and Computer == 'Paper'):
        print(f'You lose, you choose Rock and Computer chooses {Computer}')
        break

    elif((player == 'r' or player == 'Rock') and Computer == 'Scissors'):
        print(f'You win, you choose Rock and Computer chooses {Computer}')
        break

        
    elif((player == 'r' or player == 'Rock') and Computer == 'Rock'):
        print(f'Draw, you choose Rock and Computer chooses {Computer}')
        break
        
        
    # Player chooses Paper
    if((player == 'p' or player == 'Paper') and Computer == 'Paper'):
        print(f'Draw, you choose Paper and Computer chooses {Computer}')
        break
        
    elif((player == 'p' or player == 'Paper') and Computer == 'Scissors'):
        print(f'You lose, you choose Paper and Computer chooses {Computer}')
        break
        

    elif((player == 'p' or player == 'Paper') and Computer == 'Rock'):
        print(f'You win, you choose Paper and Computer chooses {Computer}')
        break
      
    # Player chooses Scissors
    if((player == 's' or player == 'Scissors') and Computer == 'Paper'):
        print(f'You win, you choose Scissors and Computer chooses {Computer}')
        break
        

    elif((player == 's' or player == 'Scissors') and Computer == 'Scissors'):
        print(f'Draw, you choose Scissors and Computer chooses {Computer}')
        break
        
    elif((player == 's' or player == 'Scissors') and Computer == 'Rock'):
        print(f'You lose, you choose Scissors and Computer chooses {Computer}')
        break
        

        

   
