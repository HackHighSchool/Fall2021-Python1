'''
Properties ref: https://en.wikibooks.org/wiki/Monopoly/Properties_reference
Cards reference: https://www.monopolyland.com/list-monopoly-chance-community-chest-cards/
Rules and Instructions reference: hasbro.com/common/instruct/00009.pdf

Objective
    - become the wealthiest player
    - become last standing player w/ money and properties

Board
    - array

Banker - computer
Bank - database of each player's earnings, unlimited


Players (class)
    -- instances - player name required parameter
    -- start with a set amount of money
    -- keep track of spot on the board
    -- roll function - generate random roll, adjust player's spot within the board(list?)
    -- alert player when they land on next spot
        - with its desc/any actions
    -- allow player to view current holdings
    - manually type "pass" or something similar if turn is over
    (not automatic pass, allow time to view holdings)

Properties 
    - attributes: owner, rent, number of houses/hotels
    - if someone lands on a property, function to check if the property is owned
    - if owned, player has to pay rent, else dialogue asks if player wants to buy the property
        - display player's current money, underneath display attributes of property
        - if player types yes and they don't have enough, tell them they cannot make the purchase
    - if player doesn't have enough to pay rent, either accumulate to debt and ask if they want to mortgage property
        or that player loses and cannot continue playing the game
        every time a player loses, their name is put into a list
        at the end, the winners list is output as string:
            "First place:{}
            Second place:{}
            Third place:{}
            Fourth place:{}
            .format(player4,player3,player2,player1)"

Houses
    - player can buy houses if all sites of a color group owned
    - if all properties have house, allow players to purchase 2nd house, and so on
    - increase rent on properties with houses
Hotels
    - call if player wants to exchange for hotel
    - if bought, -4 houses

Cards (dictionaries?)
    - randomize card that is chosen
    - updating list with cards that have been chosen
    - if card pulled is in chosen list, choose another
    - if all cards have been chosen, empty chosen list

(Classes?)
Chance cards
    - if player lands on chance, pick random card from chance dictionary:
    chance = ("chance1":"do something", "chance2":"do something else"... "chance16")

Community Chest cards
    - if player lands on community chest, pick random card from comchest dictionary:
    chest = ("chest1":"action1", "chest2":"action2" ... "chest16":"action16")

Free Parking/ Visiting Jail
    - alert players but no other dialogue
'''
#show board and instructions
#trade feature
#players can view their assets at any time

import random

# S T A R T I N G   V A R I A B L E S
num_players = 0
players = []
gameover = False
current = 0
winners_list = []

# C L A S S E S

def endGame():
    print("Would You like to Cancel?")
    confirm = input("YES or NO? ")
    print("===========================")
    if(confirm == "y" or confirm == "yes"):
        gameover = True
        print("Game Ended")
        exit()
    pass
  

class Player:
    def __init__(self, name):
        self.name = name
        self.money = 1500
        self.space = 0
        self.properties = []
        self.roll = 0

    def get_pos(self):
        return "{} is currently on {}.".format(self.name,board[self.space])

    def get_money(self):
        return self.money

    def get_properties(self):
        if len(self.properties) == 0:
            return "You currently have no properties."
        else:
            for i in range(len(self.properties)):
                print("[" + self.properties[i] + "]")
            #Have to add this return statement, otherwise returns None. Fix?
            return "Your properties are listed above."

    def turn(self):
        roll1 = random.randrange(1, 6)
        roll2 = random.randrange(1, 6)
        totalroll = roll1 + roll2
        # self.roll = totalroll
        #move player back to first space, then add remaining spaces
        if (len(board) - self.space) <= totalroll:
            self.space = -1
            self.space += (totalroll-(len(board) - self.space))
        else:
            self.space += (totalroll)
        return (" Rolled {} and {} \n Total {}\n{} moves to {}.\n".format(roll1, roll2, totalroll, self.name,board[self.space].name))
        
    #def pass(self):
        #current_player += 1
        #ask player if they want to take their turn, then call turn funct


#This section is before some classes but after player class 
#because we want to use current_player in some functions in later classes
#but first we have to define Player to create the list of player objects

# S T A R T   G A M E

print("")
print("Welcome to Monopoly!")
print("1 : Rules and Instructions")
print("2 : Start Game")
print("                               *****")
print("If, at any point during the game, you want to stop the game enter END")
print("                               *****")
start = input("Enter 1 or 2 to continue: ")
print("===========================")

if start == "1":
    print("")
    print("Rules and Instructions")
    print("======================")
    print("Objective: The player's goal is to become the wealthiest player through buying, renting and selling property. Bankruptcy results in elimination from the game. The last player remaining on the board is the winner.")
    print("")
    print("Play: Each player will always start at Go at the beginning of the game. The person going first will roll and recieve the number of spaces they are moving. After moving the delegated spaces, play will move on to the next player. According to the card the player lands on, the player will be entitled to buy real estate or other properties - or pay rent, pay taxes, draw a chance or community card, 'Go to Jail', etc.")
    print("")
    print("'Go' : Each time a player passes the Go card at the beginnning of the game, they will recieve $200. This includes receiving ")
    print("")
    print('Properties: Players have the option to buy properties when landing on them if they do not alredy belong to someone. Owning a property allows you to collect rent from them whenever somebody lands on it.')
    print("")
    print('Rent: Each property has a set rent that players must pay if they land on a property that is owned')
    print()
    print('Monopoly: A monopoly is when a player owns all the properties of a certain color. This allows the player to collect double the amount of rent on said properties and gives them the option of buying houses or hotels.')
    print("")
    print('Houses and Hotels: Players can buy houses or hotels for their properties to raise the rent on their proporties. Players must have a house on all properties in the monopoly to add another house. A hotel is the equivalent of 5 houses.')
    print("")
    print('Trades: When it is the players turn Players have the option to make a trade instead of rolling. Players can trade proporties for other proporties and or money with other plyaers.')
    print("")
    print('Jail: When a player gets told to go to jail they are stuck there until their next turn where they can either pay 50 to get out, roll the same number on both dice, or stay in jail')
    print("")
elif start == "2":
    print("")
else:
    endGame()

intro = input("Enter Y or YES to start the game: ")
if(intro.lower()!= "y" and intro.lower()!= "yes"):
    endGame()

num_players = int(input("Enter the number of players: "))

current = random.randint(0, num_players)

for i in range(num_players):
    #don't use players += to add to list. separates all characters of the entered string : ("a", "b", "c"...)
    check = input("player {}?: ".format(i + 1))
    if(check.lower() == "end"):
        i = i -1
        endGame()
    else:
        players.append(Player(check))

current_player = players[current]
print("%s Goes First"%(current_player.name))


#C L A S S E S

class Space:
    classify = "space"
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return "You passed {}.".format(self.name)

#Properties: Companies, Stations, Sites
class Property:
    classify = "property"
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

class Company(Property):
    classify = "company"
    #multipliers for rent
        #if one owned, rent = roll*4
        #if both owned, rent = roll*10
    mult1 = 4
    mult2 = 10
    def __init__(self, name, cost):
        Property.__init__(self, name, cost)
        self.rent = current_player.roll*4
        #if company1 and company2 in current_player.properties:
            #self.rent = player's roll*10
        
class Station(Property):
    classify = "station"
    def __init__(self, name, cost):
        Property.__init__(self, name, cost)
        self.rent = 25
        #if len({player}.properties) = 2:
            #self.rent = 50
        #if len({player}.properties) = 3:
            #self.rent = 100
        #if len({player}.properties) = 4:
            #self.rent = 200
        #every time # of stations increases, double rent

class Site:
    classify = "site"
    def __init__(self, name, cost, color, rent, r1, r2, r3, r4, r5):
        Property.__init__(self, name, cost)
        self.color = color
        self.rent = rent
        #rent1, rent2, rent3... increases with the more houses owned
        self.r1 = r1
        self.r2 = r2
        self.r3 = r3
        self.r4 = r4
        #rent with hotel
        self.r5 = r5
        self.owner = None
    def buy(self):
        if self.cost <= current_player.money:
            current_player.money -= self.cost
            self.owner = current_player
            return "Your updated balance is ${}. The new owner of {} is {}.".format(current_player.money, current_space.name,current_player.name)
        else:
            return "You don't have enough to buy this property."
    def pay(self):
        if self.rent <= current_player.money:
            current_player.money -= self.rent
            self.owner = current_player
            return "You paid rent to {}. Your new balance is ${}".format(board[current_player.space].owner.name, current_player.money)
        elif self.cost > current_player.money and len(current_player.properties > 0):
            sellProperty = input("Would you like to sell a property? Y/N")
            endGame(sellProperty)
            return sellProperty
            
        else: #if cost is higher than player savings and they have no properties to sell:
            return "{}, is bankrupt. You are out of the game!".format(current_player.name)

#Cards use same class, call specific functions to perform each card's tasks
class Card:
    classify = "card"
    def __init__(self, string):
        self.string = string
    def __str__(self):
        return self.string

#Spaces on board
s1 = Space("In progress") #Go
s2 = Site("Mediterranean Avenue", 60, "Brown", 2, 10, 30, 90, 160, 250) #//Old Kent Road
s3 = Space("In Progress")#Community chest 
s4 = Site("Baltic Avenue", 60, "Brown", 4, 20, 60, 180, 320, 450) #//Whitechapel Road
s5 = Space("In Progress") #Income Tax
s6 = Station("Reading Railroad", 200) #//King's Cross
s7 = Site("Oriental Avenue", 100, "Cyan", 6, 30, 90, 270, 400, 550) #//The Angel, Islington
s8 = Space("In Progress")#Chance
s9 = Site("Vermont Avenue", 100, "Cyan", 6, 30, 90, 270, 400, 550) #//Euston Road
s10 = Site("Connecticut Avenue", 120, "Cyan", 8, 40, 100, 300, 450, 600) #//Pentonville Road
s11 = Space("Just Visiting Jail") #just visiting
s12 = Site("St. Charles Place", 140, "Purple", 10, 50, 150, 450, 625, 750) #//Pall Mall
s13 = Company("Electric Company", 150)#Electric Company
s14 = Site("States Avenue", 140, "Purple", 10, 50, 150, 450, 625, 750) #//Whitehall
s15 = Site("Virginia Avenue", 160, "Purple", 12, 60, 180, 500, 700, 900) #//Northumrld Ave
s16 = Station("Pennsylvania Railroad", 200) #//Marylebone Station
s17 = Site("St. James Place", 180, "Orange", 14, 70, 200, 550, 750, 950) #//Bow Str
s18 = Space("In Progress")#Community Chest
s19 = Site("Tennessee Avenue", 180, "Orange", 14, 70, 200, 550, 750, 950) #//Marlborough Str
s20 = Site("New York Avenue", 200, "Orange", 16, 80, 220, 600, 800, 1000) #//Vine Street
s21 = Space("Free Parking") #Free Parking
s22 = Site("Kentucky Avenue", 220, "Red", 18, 90, 250, 700, 875, 1050) #//The Strand
s23 = Space("In Progress")#Chance
s24 = Site("Indiana Avenue", 220, "Red", 18, 90, 250, 700, 875, 1050)#//Fleet Street
s25 = Site("Illinois Avenue", 240, "Red", 20, 100, 300, 750, 925, 1100)#//Trafalgar Square
s26 = Station("B&O Railroad", 200)#Fenchurch St. Station
s27 = Site("Atlantic Avenue", 260, "Yellow", 22, 110, 330, 800, 975, 1150)#//Leicester Square
s28 = Site("Ventnor Avenue", 260, "Yellow", 22, 110, 330, 800, 975, 1150)#//Coventry Street
s29 = Company("Water Works", 150) #Water Works
s30 = Site("Marvin Gardens", 260, "Yellow", 22, 110, 330, 850, 1025, 1200)#//Piccadilly
s31 = Space("Go to Jail")#Go to Jail
s32 = Site("Pacific Avenue", 300, "Green", 26, 130, 390, 900, 1100, 1275)#//Regent Street
s33 = Site("North Carolina Avenue", 300, "Green", 26, 130, 390, 900, 1100, 1275)#//Oxford Street
s34 = Space("In Progress")#Community Chest
s35 = Site("Pennsylvania Avenue", 320, "Green", 28, 150, 450, 1000, 1200, 1400)#//Bond Street
s36 = Station("Short Line", 200)#//Liverpool St. Station
s37 = Space("In Progress")#Chance
s38 = Site("Park Place", 350, "Blue", 35, 175, 500, 1100, 1300, 1500)#//Park Lane
s39 = Space("In Progress")#Super Tax
s40 = Site("Boardwalk", 400, "Blue", 50, 200, 600, 1400, 1700, 2000)#//Mayfair

#Board - 40 spaces
board = (s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16, s17, s18, s19, s20,
s21, s22, s23, s24, s25, s26, s27, s28, s29, s30, s31, s32, s33, s34, s35, s36, s37, s38, s39, s40)

# G A M E
while gameover == False:
    current_player = players[current]
    print("%s's Turn"%(current_player.name))
    print(current_player.turn())
    current_space = board[current_player.space]
    
    if current_space.classify == "space":
        #look for functions that need to be called, call them, then pass on.
        pass
    elif current_space.classify == "site" and current_space.owner == None:
        buy_opt = input("Your current balance is $%d. Would you like to purchase %s for $%d? Y/N "%(current_player.money,current_space.name, current_space.cost))
        if buy_opt.lower() == "y" or buy_opt.lower() == "yes":
            print(current_space.buy())
        elif buy_opt.lower() == "y" or buy_opt.lower() == "no":
            pass
        else:
            endGame()
    elif current_space.classify == "site" and current_space.owner != None:
        print(current_space.pay())
    
    #Ask if player wants to view properties of space or finish their turn
    next_step = input("Enter p or properties to view properties of current space OR enter f or finished to pass turn to the next player.\n")
    if(next_step.lower()!= "p" or next_step.lower() != "properties" or next_step.lower()!= "f" or next_step.lower()!= "finished"):
        endGame()
    else:
        pass
    #if lower(next_step) == 'p' or lower(next_step) == 'properties':
        #call properties function
    if current < num_players-1:
        current += 1
    else:
        current = 0

print("Game Over. Current Winner: ")
#if len(players) == 1: #end game if only one player left--> return the
    #if player is out, move obj into another list, 
    #gameover == True
    #print("Game over! The winner is {}. Congratulations!".format(players[0].name))
    #return the only person left in the players list, then return (in opposite order) the players who lost
