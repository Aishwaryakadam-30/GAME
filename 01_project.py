import random
#Sanke Water Gun game
def gameWin(comp, you):
    #if two value same declare a tei!
    if comp==you:
        return None
    #check when computer choose sanke
    elif comp=='s':
         if you=='w':
             return False
         elif you =='g':
            return True
    #check when computer choose water
    elif comp=='w':
        if you=='g':
            return False
        elif you=='s':
            return True
    #check when computer choose gun
    elif comp=='g':
            if you=='s':
                return False
            elif you =='w':
                return True 
print("comp turn : Snake(s) Water(w) Gun(g)?")
randNo = random.randint(1,3)
if randNo==1:
    comp='s'
elif randNo==2:
    comp='w'
elif randNo==3:
    comp='g'

you=input("your turn : Snake(s) Water(w) Gun(g)?")

a= gameWin(comp,you)

print(f"computer chose {comp}")
print(f"you chose {you}")

if a==None:
    print("the game is tie !")
elif a:
    print("you win")
else:
    print("you lose")