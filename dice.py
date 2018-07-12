from random import randint

#function to randomly generate an integer between two integer values
def dice_roll(minimum,maximum):
    print(randint(minimum,maximum))

again="y"
while again.lower()=="y" or again.lower() == "yes":
  #asks user for integers
  number1, number2 = input("Enter two positive integers here.").split()
  try:
    dice_roll(int(number1), int(number2))
  except ValueError:
    print("not valid input (integers >=1, with lower number first)")
  again=input("Care to play again?(y/n)")
  