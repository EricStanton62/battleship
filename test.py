num = [0,0]
y=[1,1]
x=num+y
print (x)
g="Hello"
print(g[1])
h=[]
h=["1","1","1"]
print (len(h))

class room:
    name=''

    def __init__(self,name):
        self.name=name

    def get_name(self):
	    return self.name

    def intro(self):
        print("You are in a room with %s walls." % self.name)

    def info(self):
        print(self.name)
a="a"
b="b"
if a>b:
    print("hi")
if b>a:
    print("ho")
    
red=room("red")
test=red
print(red.get_name())
test.intro()
test.info()
#git add .
#git commit -m “testing”