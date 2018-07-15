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

#function for switching rooms
def move(motion):
    if motion =="up" and u==True:
        return motion
    elif motion =="down" and d==True:
        return motion
    elif motion =="left" and l==True:
        return motion
    elif motion =="right" and r==True:
        return motion
    else:
        print("you are confused, you walked into a wall, you are not dead yet. -1 Turn.")
         
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
                    print("You enter Narnia. You spend a few hours there and then leave.")
                    return 2
                else:
                    return 0
        except (TypeError, ValueError):
            pass

#function to change loc
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

#set-up
temp=[]
hi=""
yo=""
loc=(1,5)
stuck=0
mini=5
key = False

while stuck<12:
#initializing values for turn 1 (stuck 0)
    if stuck==0:
        print("while following your soccer coach down the stairs into an underground building\
 a large boulder fell and blocked the entrance, you will need to find another exit. You might be\
 dreaming, you see yourself from above. You don't know where the rest of the team is. You have\
 enough oxygen to enter 10 rooms until you pass out.")
        temp=[]
        hi=""
        yo=""
        loc=(1,5)
        mini=5
        key = False
    print (loc)

#if you run out of time
    if stuck==10:
        print ("you have run out of oxygen and died.")
        hi= input("care to play again(y/n)?")
        try:
            if hi.lower()=="y" or hi.lower()=="yes":
                stuck=0
                continue
        except (TypeError, ValueError):
            break
        else:
            break
            
     
#first room
    if loc == (1,5):
        u=True
        l=True
        r=True
        d=False
        stuck+=1
        print("You are in a room with white walls. There is an old receptionist desk in the\
 middle of the room with nothing of value on it or in it. There are however three doors.\
 One door \"up\", one door \"left\", and one door \"right\".")
        hi=direction()
        yo=move(hi)
        temp=moving(yo)
        loc=temp
       
    elif loc == (1,4):
        r=True
        u=False
        l=False
        d=False
        stuck+=1
        print("You enter a room with pink walls. There is a door only on the \"right\"")
        if mini==5:
            print("There is a cupboard that perks your interest. Little people appear to be\
 fighting. You notice one of them is Owen Wilson and the other is just some indian. You don't\
  want them to fight anymore so you take one of them. Which do you want to take?")
            if cupboard().lower() == "indian":
                print("You grab the indian.")
                mini=1
            else:
                print("Owen Wilson jumps into your hand.")
                mini=2
        hi=direction()
        yo=move(hi)
        temp=moving(yo)
        loc=temp

    elif loc == (1,6):
        l=True
        u=False
        r=False
        d=False
        stuck+=1
        print("You enter a room with purple walls. There is a wardrobe with the door cracked open\
 that peaks your interest.")
        stuck+=wardrobe()
        hi=direction()
        yo=move(hi)
        temp=moving(yo)
        loc=temp

    elif loc == (2,5):
        l=False
        u=False
        d=True
        r=True
        stuck+=1
        print("You enter a room with green walls. There is an exit sign above the door in the \"up\"\
 direction. There is also a door \"down\" and to the \"right\".")
        hi=direction()
        if hi =="up":
            if key==True:
                print ("congratulations you didn't die!")
                break
            else:
                if mini==1:
                    print("you try to open the door. It is locked. You try to knock\
    it down the door by charging at it and fail. The indian laughs.")
                elif mini==2:
                    print("you try to open the door. It is locked. Owen Wilson laughs.")
                else:
                    print("You try to open the door, but it is locked.")
        else:
            yo=move(hi)
            temp=moving(yo)
            loc=temp

    elif loc == (2,6):
        l=True
        u=False
        d=False
        r=False
        stuck+=1
        print("You enter an orange room. There is nothing but a miniature mouse hole in the wall.\
 If only you had a little person to go investigate the hole.")
        if key==False:
            if mini==1:
                print("The indian jumps down and into the hole and emerges with a key shortly after.")
                key=True
            elif mini==2:
                key=True
                print("Owen Wilson looks at the hole. He is clearly terrified. After a long while\
 and some encouragement from you he goes into the hole. After some screaming and \
a panic attack he emerges with a key.")
                stuck+=1
        hi=direction()
        yo=move(hi)
        temp=moving(yo)
        loc=temp

