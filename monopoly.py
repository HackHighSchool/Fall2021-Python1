'''
Properties ref: https://en.wikibooks.org/wiki/Monopoly/Properties_reference
Cards reference: https://www.monopolyland.com/list-monopoly-chance-community-chest-cards/

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

import random

class Player:
    money = 1500
    space = 0
    properties = []
    def __init__(self, name):
        self.name = name
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
        total = roll1 + roll2
        self.space += (total)
        return ("Roll: {}, {}. Total: {}. {} moves to {}.".format(roll1, roll2, total, self.name,board[self.space].name))
    #def pass(self):
        #current_player += 1
        #ask player if they want to take their turn, then call turn funct

class Space:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return "You passed {}.".format(self.name)

#Properties: Companies, Stations, Sites
class Property:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

class Company(Property):
    #multipliers for rent
        #if one company owned, rent = roll*4
        #if both comapanies owned, rent = roll*10
    mult1 = 4
    mult2 = 10
    def __init__(self, name, cost):
        Property.__init__(self, name, cost)
        
class Station(Property):
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
    def __init__(self, name, cost, color, rent, r1, r2, r3, r4, r5):
        Property.__init__(self, name, cost)
        self.color = color
        self.rent = rent
        #rent1, rent2, rent3... increases with the more houses you Have
        self.r1 = r1
        self.r2 = r2
        self.r3 = r3
        self.r4 = r4
        #rent with hotel
        self.r5 = r5

#Cards use same class, call specific functions to perform each card's tasks
class Card:
    def __init__(self, string):
        self.string = string
    def __str__(self):
        return self.string

#Chance Cards
#Have player enter ok statement to do action on card to give them time to read
c1 = Card("Advance to Go (Collect $200)")
c2 = Card("Advance to Trafalgar Square. If you pass Go, collect $200")
c3 = Card("Advance to Mayfair")
c4 = Card("Advance to Pall Mall. If you pass Go, collect $200")
c5 = Card("Advance to the nearest Station. If unowned, you may buy it from the Bank. If owned, pay wonder twice the rental to which they are otherwise entitled")
c6 = Card("Advance to the nearest Station. If unowned, you may buy it from the Bank. If owned, pay wonder twice the rental to which they are otherwise entitled") 
c7 = Card("Advance to nearest Utility. If unowned, you may buy it from the Bank. If owned, throw dice and pay owner a total ten times amount thrown.")
c8 = Card("Bank pays you dividend of $50")
c9 = Card("Get Out of Jail Free")
c10 = Card("Go Back 3 Spaces")
c11 = Card("Go to Jail.") #Go directly to jail - update player.space to one corresponding to Jail
c12 = Card("Make general repairs on all your property. For each house pay $25. For each hotel pay $100")
c13 = Card("Speeding fine $15")
c14 = Card("Take a trip to Kings Cross Station. If you pass Go, collect $200")
c15 = Card("You have been elected Chairman of the Board. Pay each player $50")
c16 = Card("Your building loan matures. Collect $150")

#Community Chest Cards
cc1 = Card("Advance to Go (Collect $200)")
cc2 = Card("Bank error in your favour. Collect $200")
cc3 = Card("Doctor’s fee. Pay $50")
cc4 = Card("From sale of stock you get $50")
cc5 = Card("Get Out of Jail Free")
cc6 = Card("Go to Jail.") 
cc7 = Card("Holiday fund matures. Receive $100")
cc8 = Card("Income tax refund. Collect $20")
cc9 = Card("It is your birthday. Collect $10 from every player")
cc10 = Card("Life insurance matures. Collect $100")
cc11 = Card("Pay hospital fees of $100")
cc12 = Card("Pay school fees of $50")
cc13 = Card("Receive $25 consultancy fee")
cc14 = Card("You are assessed for street repairs. $40 per house. $115 per hotel")
cc15 = Card("You have won second prize in a beauty contest. Collect $10")
cc16 = Card("You inherit $100")
   
#Community Chest and Chance cards to pull from
com_chest = (cc1, cc2, cc3, cc4, cc5, cc6, cc7, cc8, cc9, cc10, cc11, cc12, cc13, cc14, cc15, cc16)
chance = (c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16)

#Spaces on board
s1 = Space("In progress") #Go
s2 = Site("Old Kent Road", 60, "Brown", 2, 10, 30, 90, 160, 250) #//Old Kent Road
s3 = Space("In Progress")#Community chest 
s4 = Site("Whitechapel Road", 60, "Brown", 4, 20, 60, 180, 320, 450) #//Whitechapel Road
s5 = Space("In Progress") #Income Tax
s6 = Station("King's Cross Station", 200) #//King's Cross
s7 = Site("The Angel, Islington", 100, "Cyan", 6, 30, 90, 270, 400, 550) #//The Angel, Islington
s8 = Space("In Progress")#Chance
s9 = Site("Euston Road", 100, "Cyan", 6, 30, 90, 270, 400, 550) #//Euston Road
s10 = Site("Pentonville Road", 120, "Cyan", 8, 40, 100, 300, 450, 600) #//Pentonville Road
s11 = Space("Just Visiting Jail") #just visiting
s12 = Site("Pall Mall", 140, "Purple", 10, 50, 150, 450, 625, 750) #//Pall Mall
s13 = Company("Electric Company", 150)#Electric Company
s14 = Site("Whitehall", 140, "Purple", 10, 50, 150, 450, 625, 750) #//Whitehall
s15 = Site("Northumberland Avenue", 160, "Purple", 12, 60, 180, 500, 700, 900) #//Northumrld Ave
s16 = Station("Marylebone Station", 200) #//Marylebone Station
s17 = Site("Bow Street", 180, "Orange", 14, 70, 200, 550, 750, 950) #//Bow Str
s18 = Space("In Progress")#Community Chest
s19 = Site("Marlborough Street", 180, "Orange", 14, 70, 200, 550, 750, 950) #//Marlborough Str
s20 = Site("Vine Street", 200, "Orange", 16, 80, 220, 600, 800, 1000) #//Vine Street
s21 = Space("Free Parking") #Free Parking
s22 = Site("The Strand", 220, "Red", 18, 90, 250, 700, 875, 1050) #//The Strand
s23 = Space("In Progress")#Chance
s24 = Site("Fleet Street", 220, "Red", 18, 90, 250, 700, 875, 1050)#//Fleet Street
s25 = Site("Trafalgar Square", 240, "Red", 20, 100, 300, 750, 925, 1100)#//Trafalgar Square
s26 = Station("King's Cross Station", 200)#Fenchurch St. Station
s27 = Site("Leicester Square", 260, "Yellow", 22, 110, 330, 800, 975, 1150)#//Leicester Square
s28 = Site("Coventry Street", 260, "Yellow", 22, 110, 330, 800, 975, 1150)#//Coventry Street
s29 = Company("Water Works", 150) #Water Works
s30 = Site("Piccadilly", 260, "Yellow", 22, 110, 330, 850, 1025, 1200)#//Piccadilly
s31 = Space("Go to Jail")#Go to Jail
s32 = Site("Regent Street", 300, "Green", 26, 130, 390, 900, 1100, 1275)#//Regent Street
s33 = Site("Oxford Street", 300, "Green", 26, 130, 390, 900, 1100, 1275)#//Oxford Street
s34 = Space("In Progress")#Community Chest
s35 = Site("Bond Street", 320, "Green", 28, 150, 450, 1000, 1200, 1400)#//Bond Street
s36 = Station("King's Cross Station", 200)#//Liverpool St. Station
s37 = Space("In Progress")#Chance
s38 = Site("Park Lane", 350, "Blue", 35, 175, 500, 1100, 1300, 1500)#//Park Lane
s39 = Space("In Progress")#Super Tax
s40 = Site("Mayfair", 400, "Blue", 50, 200, 600, 1400, 1700, 2000)#//Mayfair

#Board - 40 spaces
board = (s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16, s17, s18, s19, s20,
s21, s22, s23, s24, s25, s26, s27, s28, s29, s30, s31, s32, s33, s34, s35, s36, s37, s38, s39, s40)

#Gameplay:
#Ask how many players
#Get player names - "Enter player one's name: [input]", "Enter player two..."
#Create player instance with that name, then append to "players" list
p1 = Player("Alex")
p2 = Player("Anny")
p3 = Player("Ashley")
players = [p1, p2, p3] #add to list when users input players
current_player = 0
#Keep moving to the next person's turn when there are still players in the game
#while len(players) > 0:
print(players[0].turn())
current_player += 1


#Tests
p2 = Company("Water Works", 15)
print (p2.cost)

