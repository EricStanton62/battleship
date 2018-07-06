from random import randint

# I use this several times to merely not return an error if the user is supposed to input an integer but does not.
def integer_check(statement):
  number=raw_input(statement)
  while number.isdigit() == False:
    number=raw_input(statement)
  return int(number)

# Helps create the board, codecademy helped write this. not sure why it's a function since I only need one board so I call them only once each. Maybe they thought 2 player the players would need their own board and possibly place their own ships.
def random_row(board):
  return randint(1, len(board)-1)

def random_col(board):
  return randint(1, len(board[0])-1)

# wrote this initially as a check that player guessed a letter/number combination that could be on the board at its largest size, if not simply have them guess again without losing a turn. It returns their guess column as both an integer and a letter in a string and the guess row.
def player_guess():
  y=0
  while y<1:
    guesses = raw_input("Guess: (EX:a1 or A1)")
    if not len(guesses) ==2:
      print ("try again in A1 format")
    else:
      guess= guesses.lower()
      if not guess in "a1a2a3a4a5a6a7a8a9b1b2b3b4b5b6b7b8b9c1c2c3c4c5c6c7c8c9d1d2d3d4d5d6d7d8d9e1e2e3e4e5e6e7e8e9f1f2f3f4f5f6f7f8f9g1g2g3g4g5g6g7g8g9h1h2h3h4h5h6h7h8h9i1i2i3i4i5i6i7i8i9":
        print("try again in A1 format(must be on the board also)")
        print_board(board)
      else:  
        y+=1
        guess_row=int(guesses[1])
        x=guesses[0].lower()
        guess_col = convert_to_number(x)  
        return guess_row,guess_col,x

# simply asks players how many ships they want on the game board, checks for valid input, generates ships checking they're unique locations, and returns a list with first value a string of ship locations and 2nd value the number of ships
def how_many_ships(): 
  ship_num="How many ships do you want to sink?(integer)"
  numbers=integer_check(ship_num)
  checker=check  
  while len(checker) <numbers*2:
    ship_row = random_row(board)
    ship_col = random_col(board)
    str_ship_col=convert_to_letter(ship_col)
    temp_ship= str_ship_col + str(ship_row)
    if not temp_ship in checker:
      checker = checker + temp_ship
  return checker,numbers

# converts a string letter to a number a=1.. etc
def convert_to_number(lower_case):
  if lower_case == "a": 
          return 1
  elif lower_case=="b":
          return 2
  elif lower_case=="c":
          return 3
  elif lower_case=="d":
          return 4
  elif lower_case=="e":
          return 5
  elif lower_case=="f":
          return 6
  elif lower_case=="g":
          return 7
  elif lower_case=="h":
          return 8
  elif lower_case=="i":
          return 9

# converts a number back into a string letter
def convert_to_letter(temp_ship_col):
  if temp_ship_col == 1:
      return "a"
  elif temp_ship_col ==2:
      return "b"
  elif temp_ship_col ==3:
      return "c"
  elif temp_ship_col ==4:
      return "d"
  elif temp_ship_col ==5:
      return "e"
  elif temp_ship_col ==6:
      return "f"
  elif temp_ship_col ==7:
      return "g"
  elif temp_ship_col ==8:
      return "h"
  elif temp_ship_col ==9:
      return "i"

# this function removes a successful hit location from the ship location string once a player sinks it.
def sunk_ship(large,small):
  temp_num= large.find(small)
  if len(large)-2==temp_num:
    medium=large[:len(large)-2]
  else:
    medium= large[:temp_num]+large[temp_num+2:len(large)]
  return medium

# at the end if the players lose, this function places "S" on the remaining ship locations so they can see where they were. 
def alive_ship(large):
  medium=large[:2]
  guess_col=convert_to_number(medium[0])
  guess_row=int(medium[1])
  board[guess_row][guess_col] = "S"
  return large[2:]

number_of_rows=1
#simply asks user how many rows they want the battleship board to have, and keeps asking until it receives a valid input.
while number_of_rows <2 or number_of_rows >9:  
  welcome="how many rows/columns(2-9)?(must be a square)"
  number_of_rows= integer_check(welcome)
  
board= []
board_size= [" ","A","B","C","D","E","F","G","H","I" ]
# shrinks the board based on how many rows the user wanted
board_size[number_of_rows+1:10]=[]
board=[board_size]
for x in range(1, number_of_rows+1):
  board.append([str(x)]+["O"] * number_of_rows)

# prints the board fairly neatly
def print_board(board):
  for row in board:
    print (" ".join(row))

print_board(board)
# a lot of variables I have to make sure exist before they're called upon.. is it normal to have this many? or is this a sign I need more functions?? classes?? help.
check=""
ship_col=0
ship_row=0
turn=0
player1_turn=0
player2_turn=100
guess_row=3
guess_col=3
temp=[3,3,""]
temp2=["",1]
guess_statement="How many guesses per player would you like?(integer)"
# players enter how many guesses they'd like.
guess_num= integer_check(guess_statement)
player1_guesses=guess_num
player2_guesses=0
player1_count=0
player2_count=0
which_player=1

eric ="content"
# this is set-up for the game
while eric != "happy":
# they say they want 0 guesses or negative guesses I just end the program, my integer check will let those values pass on purpose 
  if guess_num<=0:
    print ("ok then you lose!")
    break
# if they choose more guesses than spots on the board program ends    
  if guess_num>= number_of_rows**number_of_rows-1:
    print ("You win! Cheater.")
    guess_num=0
    break

  player_statement="1 or 2 players?(integer)"
# players input  whether there are 1 or 2 players  
  player_num= integer_check(player_statement)
# if they put 0 players, or negative players, program ends  
  if player_num<=0:
    print ("everybody wins and losses.")
    guess_num=0
    break
# if they put more than 2 players program ends  
  if player_num>2:
    print ("L2 follow directions.")
    guess_num=0
    break
# sets some values for player 2 if they exist    
  if player_num==2:
# checks that the game is still loseable, if not program ends.    
    if guess_num*player_num>= number_of_rows**number_of_rows-1:
      print ("You guys can't lose, that's no fun for me.")
      guess_num=0
      break
    player2_guesses=guess_num
    player2_turn=0

# players are asked how many ships they want here      
  temp2=how_many_ships()
  check=check+temp2[0]
  ship=int(temp2[1])
# if ships value is less than 1 end the game  
  if ship<=0:
    print ("That's a great strategy in life, never even try.")
# if there's no way for both players to lose becuase the board is too small for the guesses/ships end the game 
  if ship>=number_of_rows**number_of_rows-guess_num*player_num:
    print ("That was too many ships, you fail at life.")
    ship=0
  eric="happy"

# playing battleship starts
while turn <guess_num and ship>0:
  print check

# if two players randomize whose turn it is and print to let them know.
  if player_num ==2 and player1_guesses == player2_guesses:
    which_player=randint(1,2)
    if which_player==1:
      print ("Player 1 "),
    else:
      print ("Player 2 "),
  elif player_num==2 and player1_guesses>player2_guesses:
    which_player=1
    print ("Player 1 "),
  elif player_num==2 and player2_guesses>player1_guesses:
    which_player=2
    print ("Player 2 "),

# if only one player    
  else:
    print ("Player 1 "),
  
  print ("Guesses remaining: "), guess_num-turn

# player inputs a guess here  
  temp = player_guess()
  guess_row = int(temp[0])  
  guess_col = int(temp[1])
  col_check= str(temp[2])
  temp_check= col_check +str(guess_row)

# guess is a hit,this adds "S" to the board and gives that player a point
  if temp_check in check:
    print ("Congratulations! You sank a battleship!")
    board[guess_row][guess_col] = "S" 
    print_board(board)
    fart= sunk_ship(check,temp_check)
    check=fart
    ship-=1
    print (str(ship) +" ship(s) remaining")
    if which_player ==1:
      player1_count+=1
    else:
      player2_count+=1

# guess is not a hit gives user more instructions why    
  else:
    if guess_row > number_of_rows or \
      guess_col > number_of_rows:
      print ("Oops, that's not even in the ocean.")
    elif board[guess_row][guess_col] == "X" or \
    board[guess_row][guess_col] == "S":
      print( "You guessed that one already." )  

# a miss is recorded on the board as "X" and that player losses a turn          
    else:
      print ("You missed my battleship!")
      board[guess_row][guess_col] = "X"
      if which_player==1:
        player1_turn+=1
        player1_guesses-=1
      elif which_player==2:
        player2_turn+=1
        player2_guesses-=1
      if turn<player1_turn and turn< player2_turn:
        turn+=1
    print_board(board)

# ending of the players lose the game    
    if (turn == guess_num):
      print ("Game Over. ")
      if player_num==2:
        print ("Player 1 sunk: " + str(player1_count))
        print ("Player 2 sunk: " + str(player2_count))
        if player1_count==player2_count:
          print ("nobody wins, weak.")
        elif player1_count>player2_count:
          print ("Player 1 wins!")
        else:
          print ("Player 2 wins!")
      
      while len(check)>0:
        farts=alive_ship(check)
        check=farts
      print_board(board)

# just a joke since the program doesn't restart right now. is that easy to do?      
      joke = str(raw_input("Care to play again?(y/n)?"))
      if joke.lower() == "y":
        print ("Then click run again")
      elif joke.lower() == "n":
        print ("Cya loser")
      else:
        print ("No wonder you lost.")

# ending if players win the game        
  if ship==0:
    if player_num==1:
      print ("you win!")
    else:
      print ("Player 1 sunk: " + str(player1_count))
      print ("Player 2 sunk: " + str(player2_count))
      if player1_count==player2_count:
        print ("nobody wins, maybe chose an odd number of ships next game.")
      elif player1_count>player2_count:
        print ("Player 1 wins!")
      else:
        print ("Player 2 wins!")
        