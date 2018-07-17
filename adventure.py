#function for checking valid directional input
def direction():
    y=0
    while y<1:
        x=input("what direction will you go?")
        try:
            if x.lower() =="up" or x.lower() =="down" or x.lower()=="left" or x.lower()=="right":
                motion = x.lower()
                y+=1
                return motion
        except (ValueError, TypeError):
            pass

#function to change the tuple loc
def moving(mov):
    y=loc[0]
    x=loc[1]
    if mov=="up":
        y=loc[0]+1
        x=loc[1]
    elif mov=="left":
        y=loc[0]
        x=loc[1]-1
    elif mov=="right":
        y=loc[0]
        x=loc[1]+1
    elif mov=="down":
        y=loc[0]-1
        x=loc[1]
    return (y,x)

#Owen Wilson or the indian
def cupboard():
    return(input("Do you take the \"indian\" or Owen?"))

#wardrobe event
def wardrobe():
    while True:
        r=input("Do you go into the wardrobe? (y/n)")
        try:
            if r.lower()=="y" or r.lower()=="n" or r.lower()=="yes" or r.lower()=="no":
                if r.lower()=="y" or r.lower()=="yes":
                    print("You enter Narnia. Before you know it you've spent an hour (1 turn) \
there before leaving.")
                    return 2
                else:
                    return 0
        except (TypeError, ValueError):
            pass

#my class I call room to differentiate which room you are in
class room:
    """This is my attempt to use a class for each room"""
    __color=''
    __description=''
    __up=True
    __down=False
    __left=True
    __right=True

    def __init__(self,color,description,up,down,left,right):
        self.__color=color
        self.__description=description
        self.__up=up
        self.__down=down
        self.__left=left
        self.__right=right

#returns the color so i can later use it to determine what room they're in
    def get_color(self):
        return self.__color

#prints introduction to  the room
    def intro(self):
        print("You are in a room with %s walls." % self.__color)

#hopefully this prints only the correct directions when true.
    def direction(self):
        directions=[self.__up,self.__down,self.__left,self.__right]
        print("There is a door", end='')
        if directions[0]==True:
            print(" \"up\"", end='')
        if directions[1]==True:
            print(" \"down\"", end='')
        if directions[2]==True:
            print(" \"left\"", end='') 
        if directions[3]==True:
            print(" \"right\"", end='')
        print(".")

#prints a room description
    def info(self):
        print(self.__description)

#function for switching rooms
    def move(self,motion):
        if motion =="up" and self.__up==True:
            return motion
        elif motion =="down" and self.__down==True:
            return motion
        elif motion =="left" and self.__left==True:
            return motion
        elif motion =="right" and self.__right==True:
            return motion
        else:
            print("you are confused, you walked into a wall, you are not dead yet. -1 Turn.")

#setting up the rooms
white=room("white","""There is an old receptionist desk in the middle of the room with nothing
of value on it or in it.""",True,False,True,True)
pink=room("pink","There is a cupboard that perks your interest.",False,False,False,True)
purple=room("purple","There is a wardrobe with the door cracked open that peaks your interest.",\
False,False,True,False)
green=room("green","There is an exit sign above a keyhole in the \"up\" direction.",False,True,\
False,True)
orange=room("orange","There is nothing but a miniature mouse hole in the wall.",False,False,\
True,False)

#set-up
temp=[]
hi=""
yo=""
loc=(1,5)
turn=0
mini=5
key = False

while turn<12:
#initializing values for turn 1 (turn 0)
    if turn==0:
        print("""while following your soccer coach down the stairs into an underground building
a large boulder fell and blocked the entrance, you will need to find another exit. You might be
dreaming, you see yourself from above. You don't know where the rest of the team is. You have
enough oxygen to enter 10 rooms until you pass out.""")
        temp=[]
        hi=""
        yo=""
        loc=(1,5)
        mini=5
        key = False
#print (loc) I used while testing

#if you run out of time
    if turn==10:
        print ("you have run out of oxygen and died.")
        hi= input("care to play again(y/n)?")
        try:
            if hi.lower()=="y" or hi.lower()=="yes":
                turn=0
                continue
        except (TypeError, ValueError):
            break
        else:
            break
            
     
#checks what room you're in
    if loc == (1,5):
        location=white

    elif loc==(1,4):
        location=pink

    elif loc == (1,6):
        location=purple

    elif loc == (2,5):
        location=green

    elif loc == (2,6):
        location=orange

#prints the color of the room 
    location.intro()

#prints a room description
    location.info()
    turn+=1

#taking a miniature person is a forced result of entering the pink room
    if location.get_color()=="pink" and mini==5:
        print("""Miniature people appear to be fighting in the cupboard. You notice one
of them looks like Owen Wilson and the other is just some indian. You don't want them
to fight anymore so you take one of them. Which do you want to take?""")
        if cupboard().lower() == "indian":
            print("You grab the indian.")
            mini=1
        else:
            print("Owen Wilson jumps into your hand.")
            mini=2

#retrieving the key if in the orange room                
    if location.get_color()=="orange" and key==False:
            if mini==1:
                print("The indian jumps down without hesitation into the hole and emerges with \
a key shortly after.")
                key=True
            elif mini==2:
                key=True
                print("""Owen Wilson looks at the hole. He is clearly terrified. After a long while
and some encouragement from you he goes into the hole. After some screaming and
a panic attack he emerges with a key.""")
            else:
                print("If only you had a miniature person to investigate the hole.")
    
#purple room asks if you want to go into the wardrobe, if you do waste a turn.
    if location.get_color()=="purple":
        turn+=wardrobe()

#prints which directions are available based on what room you are in
    location.direction()

#asks user what direction they want to go and checks for valid input
    hi=direction()

#if you choose up in the green room it checks if you have the key for victory.
    if location.get_color()=="green" and hi =="up":
        if key==True:
            print ("The wall seperates in front of you. Congratulations you have escaped!")
            break
        else:
            print("""You inspect the keyhole. It looks like a regular keyhole only a bit smaller.
Upon closer investigation there is a slight vertical line from floor to ceiling just beside it.
You charge into the wall and fail to break it open. You need to find a key.""")
            if mini==1:
                print("The indian is not amused.")
            elif mini==2:
                print("Owen Wilson laughs.")
    
#moves the player checking what room they are in and only advances if ther eis a door there
    yo=location.move(hi)
    temp=moving(yo)
    loc=temp
       
