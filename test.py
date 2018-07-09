from random import randint

# I use this several times to merely not return an error if the user is supposed to input an
# integer but does not.
def integer_check(statement):
  number=input(statement)
  while number.isdigit() == False:
    number=input(statement)
  return int(number)

# Helps create the board, codecademy helped write this. not sure why it's a function since I only
# need one board so I call them only once each. Maybe they thought 2 player the players would
# need their own board and possibly place their own ships.
def random_row(board):
  return randint(1, len(board)-1)

def random_col(board):
  return randint(1, len(board[0])-1)


# wrote this initially as a check that player guessed a letter/number combination that could
# be on the board at its largest size, if not simply have them guess again without losing a turn.
# It returns their guess column as both an integer and a letter in a string and the guess row.
def player_guess():
  y=0
  while y<1:
    guesses = input("Guess: (EX:a1 or A1)")
    if not len(guesses) ==2:
      print ("try again in A1 format")
    else:
      guess= guesses.lower()
      if not guess in "a1a2a3a4a5a6a7a8a9b1b2b3b4b5b6b7b8b9c1c2c3c4c5c6c7c8c9d1d2d3d4d5d6d7d8d9\
      e1e2e3e4e5e6e7e8e9f1f2f3f4f5f6f7f8f9g1g2g3g4g5g6g7g8g9h1h2h3h4h5h6h7h8h9i1i2i3i4i5i6i7i8i9":
        print("try again in A1 format(must be on the board also)")
        print_board(board)
      else:  
        y+=1
        guess_row=int(guesses[1])
        x=guesses[0].lower()
        guess_col = convert_to_number(x)  
        return guess_row,guess_col,x

# simply asks players how many ships they want on the game board, checks for valid input, 
# generates ships checking they're unique locations, and returns a list with first value
# a string of ship locations and 2nd value the number of ships
def how_many_ships(): 
  ship_num="How many ships do you want to sink?(integer)"
  numbers=integer_check(ship_num)
  ship_length="Up to what length do you want the ships?"
  ship_size=0
  while ship_size <1 or ship_size < number_of_rows:
    ship_size=integer_check(ship_length)
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
def convert_to_letter(ship_column):
  if ship_column == 1:
      return "a"
  elif ship_column ==2:
      return "b"
  elif ship_column ==3:
      return "c"
  elif ship_column ==4:
      return "d"
  elif ship_column ==5:
      return "e"
  elif ship_column ==6:
      return "f"
  elif ship_column ==7:
      return "g"
  elif ship_column ==8:
      return "h"
  elif ship_column ==9:
      return "i"

# this function removes a successful hit location from the ship location string once a player
# sinks it.
def sunk_ship(large,small):
  temp_num= large.find(small)
  if len(large)-2==temp_num:
    medium=large[:len(large)-2]
  else:
    medium= large[:temp_num]+large[temp_num+2:len(large)]
  return medium

# at the end if the players lose, this function places "S" on the remaining ship locations
# so they can see where they were. 
def alive_ship(large):
  medium=large[:2]
  guess_col=convert_to_number(medium[0])
  guess_row=int(medium[1])
  board[guess_row][guess_col] = "S"
  return large[2:]

name1=""
name2=""
# asks player name
def ask_name():
  player1=""
  player2=""
  player1=input("What is your name player 1?")
  if player_num==2:
    player2=input("What is your name player 2?")
    while player1==player2:
      player2=input("That name is already taken, try a different one.")
    if player2=="Mr. Hankey" or player1=="Mr. Hankey":
      player2="Cartman"
      print ("Great I'll call you Cartman.")
    else:
      player2="Mr. Hankey"
      print ("Great I'll just call you Mr. Hankey.")
  return player1, player2

# asks if they want to restart battleship     
def play_again_q():
  joke = str(input("Care to play again?(y/n)?"))
  if joke.lower() == "y":
    "nothing"
    print ("Good luck!")
    return True
  elif joke.lower() == "n":
    if player_num==2:
      print ("Final score:")
      print (name1+ ": " + str(perm_player1_count) + " ships sunk")
      print (name2+ ": " + str(perm_player2_count) + " ships sunk")
    print ("Cya")
    return False
  else:
    print ("No wonder you lost.")
    return False

perm_player1_count=0
perm_player2_count=0
play_again=True
already_played=False
# put the entire code in a while loop so they can play again
while play_again==True:
  number_of_rows=1
# simply asks user how many rows they want the battleship board to have,
# and keeps asking until it receives a valid input.
  def num_of_rows():
    number_of_rows=1
    while number_of_rows <2 or number_of_rows >9:  
      welcome="how many rows/columns(2-9)?(must be a square)"
      number_of_rows= integer_check(welcome)
    return number_of_rows
  number_of_rows=num_of_rows()

  board= []
  def board_setup():
    board_size= [" ","A","B","C","D","E","F","G","H","I" ]
# shrinks the board based on how many rows the user wanted
    board_size[number_of_rows+1:10]=[]
    board=[board_size]
    for x in range(1, number_of_rows+1):
      board.append([str(x)]+["O"] * number_of_rows)
    return board
  board=board_setup()

# prints the board fairly neatly
  def print_board(board):
    for row in board:
      print (" ".join(row))

  print_board(board)
# a lot of variables I have to make sure exist before they're called upon..
# is it normal to have this many? or is this a sign I need more functions?? classes?? help.
  check=""
  ship_col=0
  ship_row=0
  turn=0
  player1_turn=0
  player2_turn=100
  guess_row=3
  guess_col=3
  store_guess=[3,3,""]
  ship_quantity=["",1]
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
# they say they want 0 guesses or negative guesses I just end the program,
# my integer check will let those values pass on purpose 
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
    if already_played==False:
      player_num= integer_check(player_statement)
    else:
      player_num=2
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
      player_name=ask_name()
      name1=player_name[0]
      name2=player_name[1]
      player2_guesses=guess_num
      player2_turn=0

# players are asked how many ships they want here      
    ship_quantity=how_many_ships()
    check=check+ship_quantity[0]
    ship=int(ship_quantity[1])
# if ships value is less than 1 end the game  
    if ship<=0:
      print ("That's a great strategy in life, never even try.")
# if there's no way for both players to lose becuase the board is too small for the
# guesses/ships end the game 
    if ship>=number_of_rows**number_of_rows-guess_num*player_num:
      print ("That was too many ships, you fail at life.")
      ship=0
    eric="happy"

# playing battleship starts
  while turn <guess_num and ship>0:
    print (check)

# if two players randomize whose turn it is and print to let them know.
    if player_num ==2 and player1_guesses == player2_guesses:
      which_player=randint(1,2)
      if which_player==1:
        print (name1, end="")
      else:
        print (name2, end="")
    elif player_num==2 and player1_guesses>player2_guesses:
      which_player=1
      print (name1, end="")
    elif player_num==2 and player2_guesses>player1_guesses:
      which_player=2
      print (name2, end="")

# if only one player    
    else:
      print (name1, end="")
    
    print (" guesses remaining:",  guess_num-turn)

# player inputs a guess here  
    store_guess = player_guess()
    guess_row = int(store_guess[0])  
    guess_col = int(store_guess[1])
    col_check= str(store_guess[2])
    guess_string= col_check +str(guess_row)

# guess is a hit,this adds "S" to the board and gives that player a point
    if guess_string in check:
      print ("Congratulations! You sank a battleship!")
      board[guess_row][guess_col] = "S" 
      print_board(board)
      remaining_ship= sunk_ship(check,guess_string)
      check=remaining_ship
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
          perm_player1_count+=player1_count
          perm_player2_count+=player2_count
          print (name1 +" sunk: " + str(player1_count))
          print (name2 +" sunk: " + str(player2_count))
          if player1_count==player2_count:
            print ("nobody wins, weak.")
          elif player1_count>player2_count:
            print (name1 +" wins!")
          else:
            print (name2 +" wins!")
        
        while len(check)>0:
          remaining_ships=alive_ship(check)
          check=remaining_ships
        print_board(board)
# I do this 3 times, can I put this in a function? play_again_q() returns True or False
        play_again=play_again_q()
        already_played=play_again
      
# ending if players win the game        
  if ship==0:
    if player_num==1:
      print ("you win!" +name1)
      play_again=play_again_q()
      already_played=play_again
    else:
      perm_player1_count+=player1_count
      perm_player2_count+=player2_count
      print (name1 +" sunk: " + str(player1_count))
      print (name2 +" sunk: " + str(player2_count))
      if player1_count==player2_count:
        print ("nobody wins, maybe chose an odd number of ships next game.")
      elif player1_count>player2_count:
        print (name1 +" wins!")
      else:
        print (name2 +" wins!")
      play_again=play_again_q()
      already_played=play_again
        