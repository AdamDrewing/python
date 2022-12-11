import random
choices=['Rock','Paper','Scissors']
name=input("Enter your name :")
PlayerScore=0 
Player2Score=0
NumberOfRounds=0
gameOn=True
print(f"Welcome to game: {name.title()}")
while NumberOfRounds<3:
  PlayerOption=random.choice(choices)
  Player2Option=input("Enter Rock/ Paper/ Scissors :").title()
  print(f"Player option :{PlayerOption}")
  print(f"{name.title()} option :{Player2Option}")
  NumberOfRounds += 1
  if PlayerOption == Player2Option:
    print('Tie')
  elif (PlayerOption =='Rock' and Player2Option == 'Scissors') or (PlayerOption =='Scissors' and Player2Option =='Paper') or (PlayerOption =='Paper' and Player2Option =='Rock'):
    print("Player win")
    PlayerScore += 1
    print(f"{name.title()} Wins")
    Player2Score += 1
  else:
   print("Choose option to play this game.") 
  print("---")
  print("")
  print(f"Round No: {NumberOfRounds}")
  print("--- Score Board ---")
  print(f"{name.title()}: {Player2Score} | Player: {PlayerScore}")
  print("===")
  print("")
  if NumberOfRounds==3:
    gameOn=False
    break
if Player2Score==PlayerScore:
  print("Draw!!")
elif Player2Score>Player2Score:
  print(f"Congrats {name.title()}, You won the game!!")
else:
  print(f"Player won the game!! Next time {name.title()}!")