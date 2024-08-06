# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

# Remember the rules:

# Rock beats scissors
# Scissors beats paper
# Paper beats rock

player1 = input("What is you name? ")
player2 = input("And your name? ")

u1 = input(f"Do you choose rock, paper or scissors {player1}? ")
u2 = input(f"And do you choose rock, paper or scissors {player2}? ")

def compare(u1, u2):
  if u1 == u2:
    return("It's a tie!")
  if u1 == "rock":
    if u2 == "paper":
      return(f"{player2} wins!")
    elif u2 == "scissors":
      return(f"{player1} wins")
  if u1 == "paper":
    if u2 == "rock":
      return(f"{player1} wins!")
    elif u2 == "scissors":
      return(f"{player2} wins")
  if u1 == "scissors":
    if u2 == "rock":
      return(f"{player2} wins!")
    elif u2 == "paper":
      return(f"{player1} wins")
  else:
      return("Invalid input! You have not entered rock, paper or scissors, try again.")
      sys.exit()

print(compare(u1, u2))