loc=[0,5]

#function for checking valid directional input
def direction(user):
    if user.lower() =="up" or user.lower() =="down" or user.lower()=="left" or user.lower()=="right":
        return True
    else: 
        return False

#function for switching rooms
def move():
    while True:
        x=input("what direction will you go?")
        if direction(x):
            if x.lower() =="up":
                return 1,0
            elif x.lower() =="down":
                return -1,0
            elif x.lower() =="left":
                return 0,-1
            else:
                return 0,1

#function to change loc
def 
#first room
if 