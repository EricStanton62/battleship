from random import randint

def rand_num():
    return randint(1,1000)

#check if their input was a valid number
def is_number(stuff):
    try:
        if stuff.isdigit():
            if int(stuff)>=1 and int(stuff)<=1000:
                return True
        else:
            return False
            
    except (ValueError, TypeError):
        return False

#comparing their guess with the random number
def check(actual,user_guess):
    if actual == user_guess:
        print("You got it!")
        return True
    elif actual< user_guess:
        print("Your guess was too high.")
        return False
    else:
        print("Your guess was too low.")
        return False
   
x=rand_num()
y=False
while not y:
    z=input("Guess a number(integer) between 1 and 1000.")
    if is_number(z):
        y= check(x,int(z))