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
            if x.lower() =="up" and u==True:
                return 1,0
            elif x.lower() =="down" and d==True:
                return -1,0
            elif x.lower() =="left" and l==True:
                return 0,-1
            elif x.lower() =="right" and r==True:
                return 0,1
            else:
                print("you are confused, you walked into a wall, you are not dead yet.")
                return 0,0

#Owen Wilson or the indian
def cupboard():
    return(input("Do you take the indian or Owen?"))

#wardrobe event
def wardrobe():
    

#function to change loc
def moving(a,b):
    y=loc[0]+a
    x=loc[1]+b
    return y,x

#set-up
print("while following your soccer coach down the stairs into an underground building\
 a large boulder fell and blocked the entrance, you will need to find another exit.\
 You don't know where the rest of the team is. You predict you'll have enough oxygen\
 to enter 7 rooms until you pass out.")
temp=[]
loc=[1,5]
stuck=0
mini=5

while stuck<8:

#first room
    if loc == [1,5]:
        u=l=r=True
        d=False
        stuck+=1
        print("You are in a room with white walls. There is an old receptionist desk in the\
        middle of the room with nothing of value on it or in it. There are however three doors.\
        One door \"up\", one door \"left\", and one door \"right\".)
        temp=move()
        loc=moving(temp[0],temp[1])
    elif loc == [1,4]:
        global mini
        r=True
        u=l=d=False
        print("You enter a room with pink walls. There is a cupboard that perks your interest.\
        Little people appear to be fighting. You notice one of them is Owen Wilson and the other\
         is just some indian. You don't want them to fight anymore so you take one of them. Which?")
        if cupboard().lower() == "indian":
            mini=1
        else:
            mini=2
        temp=move()
        loc=moving(temp[0],temp[1])
    elif loc == [1,6]:
        l=True
        u=r=d=False
        print("You enter a room with purple walls. There is a wardrobe with the door cracked open\
         that peaks your interest.")
        
