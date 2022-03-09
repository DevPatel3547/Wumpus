# Wumpus
Wumpus, Final project for ENGR 102 lab(2021)

Wumpus was a text-based game created for computers in 1973 by
Gregory Yob, and was originally written in BASIC (the real original
BASIC, not visual Basic.) This is a replication of the game in Python.


RULES

How to Play:
The Wumpus lives in a cave of twenty rooms. Each room has three
tunnels leading to other rooms. You want to shoot the Wumpus
before it eats you, or you die from falling in a Bottomless Pit or from
shooting yourself with a Crooked Arrow.
Play is turn-based. At the start of each turn, the program tells you
what room you are in, and what the three neighboring rooms are.
On a given turn, the player can either a) move to a neighboring
room, or b) shoot a crooked arrow.

Moving:
If you choose to move, you will be asked which number room you
want to move to. If you try to move to room which is not neighbor-
ing, the program will tell you the move is not possible.


Shooting an arrow:
When you shoot an arrow, it can travel through 1 to 5 rooms – you
have to tell the computer which rooms you want the arrow to go
through. The rooms must be connected – if you enter non-connected
rooms the program will 1) tell you the arrow path is not valid, and 2)
generate a random path (of the same number of rooms) for the arrow
to travel. If the arrow goes through the room where the Wumpus is,
the Wumpus is hit and the player wins! If the arrow (somehow) goes
through your room, you have shot yourself, and you lose!
As described below, whenever you shoot an arrow, the Wumpus
wakes up.
You start off with 5 arrows. When you run out of arrows, you lose!

Hazards:
There are two hazards in the cave network – Bottomless Pits and
Superbats.

Bottomless Pits:
Two of the twenty rooms have bottomless pits. If you enter either of
these rooms, you will fall into the pit and die, and you lose!

Superbats:
Two of the twenty rooms have Superbats living in them. If you enter
a room with Superbats, a bat will pick you up and drop you off in
some other random room. This can be a problem – if the bat drops
you off in a room with a bottomless pit, you fall in and die. If the bat
drops you off in the room where the Wumpus is, you will have to
deal with the Wumpus – it will wake up, and either leave the room
or eat you.


Initializing:
The rooms in which the pits and bats are placed are randomly chosen
at the start of the game. The initial room for the Wumpus is also
randomly chosen at the start of the game. But at the start of the game
none of these five items are in the same room.

The Wumpus:
The Wumpus is not bothered by bats or pits. Unlike you, the Wum-
pus may move into a room with a pit or bats during the game, but
nothing happens; it is too heavy for the bats to pick up, and has suckers 
on its feet, so it won’t fall in pits. Usually the Wumpus is asleep,
but two things will wake it up: if you enter its room, or if you shoot
an arrow. If the Wumpus wakes up, there is a 75% chance it will sim-
ply move to another neighboring room. There is a 25% chance it will
stay put. If you are in the same room as the Wumpus after it moves
or stays put, it will eat you, and you lose!

Warnings:
You have a magic earbud which will give you warnings if you are
one room away from the Wumpus or a hazard. If you are one room
away from the Wumpus, it will say “I smell a Wumpus.” If you are
one room away from a bottomless pit, it will say “I feel a draft”, and
if you are one room away from the bats, it will say “Bats nearby.”
