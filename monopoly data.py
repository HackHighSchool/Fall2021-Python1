'''
Objective
    - become the wealthiest player
    - become last standing player w/ money and properties

Board
    - array

Banker - computer
Bank - database of each player's earnings, unlimited


Players (class)
    - instances - player name required parameter
    - start with a set amount of money
    - keep track of spot on the board
    - roll function - generate random roll, adjust player's spot within the board(list?)
    - alert player when they land on a new square w name
    - allow player to view current holdings
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

Chance cards
    - if player lands on chance, pick random card from chance dictionary:
    chance = ("chance1":"do something", "chance2":"do something else"... "chance16")

Community Chest cards
    - if player lands on community chest, pick random card from comchest dictionary:
    chest = ("chest1":"action1", "chest2":"action2" ... "chest16":"action16")

Free Parking/ Vising Jail
    - alert players but no other dialogue
'''