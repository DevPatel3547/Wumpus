# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Name:         Dev Rahulbhai Patel
# Section:      505
# Assignment:   WUMPUS AKA LET'S CODE LIKE THE 70'S
# Date: DAY 8 MONTH 10 YEAR 2021
# UIN:931007975







# WUMPUS
#Programming like the 70's



#importing#
import random
import turtle
###########               

#creating required lists and variables#
wumpusprobability = random.randint(0,3)#probability for wumpus whether it stays put or not
z = random.sample(range(1, 20), 10)#random different values for intial postition of wumpus,player,bats,and pits
nextturn = 0#for te whileloop
#all random values
num1 = z[0]
num2 = z[1]
num3 = z[2]
num4 = z[3]
num5 = z[4]
num6 = z[5]
num7 = z[6]
num8 = z[7]
num9 = z[8]
num10 = z[9]
#and assigning them
player = num1
wumpus = num2
bats = [num3, num4]
bpits = [num5, num6]
arrow = player
numberofarrows = 5#as the name suugests


#creating three rings based on the structure of map
ring1 = [1, 2, 3, 4, 5]
ring2 = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
ring2a = [7, 9, 11, 13, 15]
ring3 = [17, 18, 19, 20, 16]
#these allows easy movement with an effecient code
#####################################


#####defining functions####

def displaychoices():#for the movement of player providing him with the choice of moving to the room in displaychoice variable
    global player
    global displaychoice
    if player in ring1:

        if player == 5:
            displaychoice = [1, 6, 4]

        else:
            index = ring1.index(player)
            ring2index = player * 2
            displaychoice = [ring1[index + 1], ring1[index - 1], ring2[ring2index]]

    if player in ring2:
        if player == 8 or player == 10 or player == 12:
            index = ring2.index(player)
            qadas = int(index / 2)
            displaychoice = [ring2[index + 1], ring2[index - 1], qadas]

        if player == 14:
            displaychoice = [15,4,13]

        if player == 7 or player == 9 or player == 11 or player == 13:
            index = ring2.index(player)
            index1 = ring2a.index(player)
            qadas = ring3[index1]
            displaychoice = [ring2[index + 1], ring2[index - 1], qadas]

        if player == 6:
            displaychoice = [5, 7, 15]

        if player == 15:
            displaychoice = [6,14,16]

    if player in ring3:
        index = ring3.index(player)
        displaychoice = [ring2a[index]]
    return displaychoice







def arrowdisplaychoices(arrow):#same thing as displaychoices function but used for things other than players mainly for the shooting of arrow
    global arrowdisplaychoice
    if arrow in ring1:

        if arrow == 5:
            arrowdisplaychoice = [1, 6, 4]

        else:
            index = ring1.index(arrow)
            ring2index = arrow * 2
            arrowdisplaychoice = [ring1[index + 1], ring1[index - 1], ring2[ring2index]]

    if arrow in ring2:
        if arrow == 8 or arrow == 10 or arrow == 12:
            index = ring2.index(arrow)
            qadas = int(index / 2)
            arrowdisplaychoice = [ring2[index + 1], ring2[index - 1], qadas]

        if arrow == 7 or arrow == 9 or arrow == 11 or arrow == 13:
            index = ring2.index(arrow)
            index1 = ring2a.index(arrow)
            qadas = ring3[index1]
            arrowdisplaychoice = [ring2[index + 1], ring2[index - 1], qadas]

        if arrow == 6:
            arrowdisplaychoice = [5, 7, 15]
        if arrow == 14:
            arrowdisplaychoice = [15,4,13]
        if arrow == 15:
            arrowdisplaychoice = [14,6,16]


    if arrow in ring3:
        index = ring3.index(arrow)
        arrowdisplaychoice = [ring2a[index]]
    return arrowdisplaychoice

def surekill():#kills the player if he is in the same room as wumpus
 global player
 global nextturn
 if player == wumpus:
     nextturn = 1#will end the loop
     print('You foolishly entered into the same room as wumpus and died')
     print('GAME OVER')
     #using turtle graphics to print a game over message if the player looses
     turtle.color('maroon')
     style = ('goudy stout', 30, 'bold')
     turtle.write('GAME OVER!!!!', font=style, align='center')
     turtle.getscreen().mainloop()


#using out of range default settings so that the function can be called and used without having to use all 5 varialbes
#Example for shooting 1 to 5 rooms i can use it for the first room then the first two rooms and so on
def wumpuskill(a = 100, b=100, c=100, d=100, e=100):#kills the wumpus if shot by player if the condition is met
    global nextturn
    if wumpus == a or wumpus == b or wumpus == c or wumpus == d or wumpus == e  :
        nextturn = 1
        print("The arrow has  hit the wumpus which was in the room")
        print("You won")
        # using turtle graphics to print a You won message if the player wins
        style = ('goudy stout', 30, 'bold')
        turtle.color('dark blue')
        turtle.write('YOU WIN!!!!', font=style, align='center')
        turtle.getscreen().mainloop()


def randomkill(a = 100, b=100, c=100, d=100, e=100):#kills the wumpus or the player by the randomly generated arrow path if the condition is met
    global nextturn
    if wumpus == a or wumpus == b or wumpus == c or wumpus == d or wumpus == e:
        nextturn = 1
        print("The arrow has somehow hit the wumpus")
        print("You WON!!!!!")
        # using turtle graphics to print a You won message if the player wins
        style = ('goudy stout', 30, 'bold')
        turtle.color('dark blue')
        turtle.write('YOU WON!!!!', font=style, align='center')
        turtle.getscreen().mainloop()

    if player == a or player == b or player == c or player == d or player == e  :
        nextturn = 1
        print("The arrow has somehow hit you")
        print("GAME OVER!!")
        # using turtle graphics to print a game over message if the player looses
        turtle.color('maroon')
        style = ('goudy stout', 30, 'bold')
        turtle.write('GAME OVER!!!!', font=style, align='center')
        turtle.getscreen().mainloop()

def wumpusmove():#movement of wumpus
    global wumpus
    if wumpusprobability != 3:#if the number is 3 there is a 25% probability else, there is a 75% probability(based on the variable wumpusprobability created initially)
        wumpusmoves = arrowdisplaychoices(wumpus)
        wmove = random.choice(wumpusmoves)
        wumpus = wmove
        print("The wumpus moved to a different room")
        surekill()#calling a previous function to check
    else:
        print("The wumpus stays put")


def bpitkill():
    global nextturn
    global player
    if player in bpits:
        print('You foolishly fell into a pit and died')
        print('GAME OVER')  # DEAD
        # printing a game over message with turtle graphics if the player looses
        nextturn = 1
        #using turtle to print a game over message if the player loses
        turtle.color('maroon')
        style = ('goudy stout', 30, 'bold')
        turtle.write('GAME OVER!!!!', font=style, align='center')
        turtle.getscreen().mainloop()


###########################





















####main loop####

while nextturn <1:#if the player looses or wins the game, nextturn will become 1, ending the loop


 displaychoices()
 #calling a function to signal player of the dangers around him if any
 if bats[0] in displaychoice or bats[1] in displaychoice:
     print('Bats nearbu')
 if bpits[0] in displaychoice or bpits[1] in displaychoice:
     print('I feel a draft')
 if wumpus in displaychoice:
     print('I smell a Wumpus')
 print('\n')
 print('You are currently in room', player)



 decide =int(input("Would you like to move or shoot? Enter 1 for move; Enter 2 for shoot :"))#asking the user for his choice
 if decide == 1:#if the player wants to move
    print('The tunnels lead to the following rooms')
    print(*displaychoice, sep=" ")  # printing the list of displaychoice in a format that is easy for the user to understand
    move = int(input('Which tunnel would you like to take?'))#if he wants to move
    displaychoices()#checking again just in case


    if move in displaychoice:#if player has entered a option which is displaychoice which is the rooms to which he can move
        player = move#player will be moved to that room
        print('You are now in the room', player)
        surekill()#if the player moved in the same room as wumpus......DEAD!!
    else:
        print('There are no tunnels that lead to room',move )#if the user entered a not connected room





    bpitkill() #if the player moves to a location with b pit, DEAD
    if player in bats:
        #He will be transported to a different room
        player = random.randint(1,20)#random rrom
        print('You foolishly walked into a room with a superbat, mere mortal')
        print('The bat carried you to another room')
        print('You are now in room', player)
        bpitkill()#checking again
        surekill()#and again


 if decide == 2 :#if the player wants to shoot
    hmany = int(input('How many rooms would you like to shoot through?'))
    numberofarrows -= 1
    #using hmany to identify how many rooms the user wants to shoot through and the moving forward accordingly
    if hmany == 1:
        p1 = int(input("Enter path1: "))
        if p1 not in displaychoice :
            print("Wrong choice, the rooms are not connected!!!")
            print("Generating Random Path For The Arrow")
            p1 = random.choice(displaychoice)#random choice out of the rooms suuronding players because only one room hence it would be the same as player's rooms
            print("The path generated is", p1)
            print("SHOOT GOES THE ARROWW......!!!")
            randomkill(p1)  # calling a function to check if the wumpus was in that room if he was , you won
        else:
            print("SHOOT GOES THE ARROWW......!!!")
            wumpuskill(p1)#if the path the user entered was correct and checking the normal kill

    elif hmany == 2:
        p1 = int(input("Enter path1: "))
        p2 = int(input("Enter path2: "))
        # checking if the 2nd path entered by user is connected to the entered first room This same method will be used for all the 5 rooms
        p2check = arrowdisplaychoices(p1)
        #if any one of the rooms is not connected, random path will be generated and the required functions will be called
        if p1 not in displaychoice or p2 not in p2check:
            print("Wrong choice, the rooms are not connected!!!")
            print("Generating Random Path For The Arrow of connected rooms")
            p1 = random.choice(displaychoice)
            arrowdisplaychoices(p1)
            p2 = random.choice(arrowdisplaychoice)
            randomkill(p1, p2)
            print("SHOOT GOES THE ARROWW......!!!")
            print("The path generated is", p1, p2)

        else:
            print("SHOOT GOES THE ARROWW......!!!")
            wumpuskill(p1,p2)
            randomkill(p1,p2)#checking just in case if the player shot himself xd
    #using same concept from hmany=1 and hmany=2 upto 5 paths which is the max a user can shoot through
    elif hmany == 3:
        p1 = int(input("Enter path1: "))
        p2 = int(input("Enter path2: "))
        p2check = arrowdisplaychoices(p1)
        p3 = int(input("Enter path3: "))
        p3check = arrowdisplaychoices(p2)
        if p1 not in displaychoice or p2 not in p2check or p3 not in p3check:
            print("Wrong choice, the rooms are not connected!!!")
            print("Generating Random Path For The Arrow of connected rooms")
            p1 = random.choice(displaychoice)
            arrowdisplaychoices(p1)
            p2 = random.choice(arrowdisplaychoice)
            arrowdisplaychoices(p2)
            p3 =  random.choice(arrowdisplaychoice)
            print("The path generated is", p1,p2,p3)
            print("SHOOT GOES THE ARROWW......!!!")
            randomkill(p1, p2, p3)
        else:
            print("SHOOT GOES THE ARROWW......!!!")
            wumpuskill(p1, p2,p3)
            randomkill(p1, p2,p3)
    elif hmany == 4:
        p1 = int(input("Enter path1: "))
        p2 = int(input("Enter path2: "))
        p2check = arrowdisplaychoices(p1)
        p3 = int(input("Enter path3: "))
        p3check = arrowdisplaychoices(p2)
        p4 = int(input("Enter path4: "))
        p4check = arrowdisplaychoices(p3)
        if p1 not in displaychoice or p2 not in p2check or p3 not in p3check or p4 not in p4check:
            print("Wrong choice, the rooms are not connected!!!")
            print("Generating Random Path For The Arrow of connected rooms")
            p1 = random.choice(displaychoice)
            arrowdisplaychoices(p1)
            p2 = random.choice(arrowdisplaychoice)
            arrowdisplaychoices(p2)
            p3 =  random.choice(arrowdisplaychoice)
            arrowdisplaychoices(p3)
            p4 = random.choice(arrowdisplaychoice)
            print("The path generated is", p1, p2, p3, p4)
            print("SHOOT GOES THE ARROWW......!!!")
            randomkill(p1, p2, p3, p4)

        else:
            print("SHOOT GOES THE ARROWW......!!!")
            wumpuskill(p1, p2, p3,p4)
            randomkill(p1, p2, p3, p4)
    elif hmany == 5:
        p1 = int(input("Enter path1: "))
        p2 = int(input("Enter path2: "))
        p2check = arrowdisplaychoices(p1)
        p3 = int(input("Enter path3: "))
        p3check = arrowdisplaychoices(p2)
        p4 = int(input("Enter path4: "))
        p4check = arrowdisplaychoices(p3)
        p5 = int(input("Enter path5: "))
        p5check = arrowdisplaychoices(p4)
        if p1 not in displaychoice or p2 not in p2check or p3 not in p3check or p4 not in p4check or p5 not in p5check:
            print("Wrong choice, the rooms are not connected!!!")
            print("Generating Random Path For The Arrow of connected rooms")
            p1 = random.choice(displaychoice)
            arrowdisplaychoices(p1)
            p2 = random.choice(arrowdisplaychoice)
            arrowdisplaychoices(p2)
            p3 =  random.choice(arrowdisplaychoice)
            arrowdisplaychoices(p3)
            p4 = random.choice(arrowdisplaychoice)
            arrowdisplaychoices(p4)
            p5 = random.choice(arrowdisplaychoice)
            print("The path generated is", p1, p2, p3, p4, p5)
            print("SHOOT GOES THE ARROWW......!!!")
            randomkill(p1, p2, p3, p4, p5)
        else:
            print("SHOOT GOES THE ARROWW......!!!")
            wumpuskill(p1, p2, p3, p4, p5)
            randomkill(p1, p2, p3, p4, p5)
    elif hmany > 5:#user cannot shoot through more than 5 rooms
        print("You can't shoot more than 5 connected rooms")
    if nextturn < 1:#if the user is alive, the code will check for the probability of the movement of wumpus and again check if the user is in the same room as wumpus
        print("Your arrow woke the Wumpus up!!")
        wumpusmove()
        surekill()
    if numberofarrows == 0 and nextturn<1:#The player will lose if he is out of arrows and if the wumpus is still alive
        nextturn = 1
        print("You should have used that brain of yours to keep a track of the number of arrows")
        print("You have run out of arrows")
        print("YOU LOSE!!!")
        turtle.color('maroon')
        style = ('goudy stout', 30, 'bold')
        turtle.write('GAME OVER!!!!', font=style, align='center')
        turtle.getscreen().mainloop()



#################


































