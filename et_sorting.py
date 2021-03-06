#!/usr/bin/python3
import random
import itertools
# sorting players into teams based on prw and k/d
# TODO:
# add more players for testing
# add usefulness factor for campers

# sorting algorithm is fair right now but to make it even better we could add
# usefulness factor  (for campers only) => rating = rating* 0.7
# this will make sure that useless ppl like smithay are rated fair, while
# others are not affected.

playersList = {1: ['Freak', 1.9, 0.9, 0.9],2: ['Macka', 3.4, 0.8, 0.8], \
 3: ['GreatDanton', 1.69, 0.67, 0.67], 4: ['Smithay', 3.9, 0.45, 0.45], \
 5: ['Frog', 2.9, 0.83, 0.83], 6: ['Randal', 1.05, 0.35, 0.35], \
 7: ['Elph', 2.0, 0.48, 0.48], 8: ['Venom', 2.0, 0.74, 0.74], 
 9: ['Gaunt', 1.4, 0.649, 0.649], 10: ['Breh', 2.3, 0.745, 0.745], \
 11: ['Gargoyles', 2.086, 0.385, 0.385], 12: ['zyklonn', 1.949, 0.588, 0.588], \
 13: ['Etplayer', 1.855, 0.468, 0.468,], 14: ['klokk', 1.840, 0.692, 0.692], \
 15: ['death', 2.275, 0.564, 0.564], 16: ['Noxious', 2.916, 0.638, 0.638], \
 17: ['Greenfire', 3.385, 0.652, 0.652], 18: ['Noix', 1.204, 0.689, 0.689], \
 18: ['Ak/47', 1.350, 0.499, 0.499], 19: ['Stumpel', 0.692, 0.441, 0.441], \
 20: ['kdshp', 0.415, 0.333, 0.333]}

# greedy_sorting algorithm
def greedy_sorting(sortedList):
# sorting players into teams using greedy sorting
    axis = []
    allies = []
    max_players_per_team = len(sortedList) // 2
    axis_score = 0
    allies_score = 0

    for player in sortedList:
        if axis_score <= allies_score:
            if len(axis) < max_players_per_team:
                axis.append(player)
                axis_score += float(player[3])
            else:
                allies.append(player)
                allies_score += float(player[3])
        else:
            allies.append(player)
            allies_score += float(player[3])

# printing teams score
    print("")
    print("{:15}{:<6.3f}".format("axis score:", axis_score))
    print("{:15}{:<6.3f}".format("allies score:", allies_score))
    print("{:14}{:<6}".format("difference:", str(axis_score-allies_score) + " for axis"))
    print("")

# since the output of the shuffle with same players is always the same
# this switches teams so that the first player (ex. Freak) doesn't always end up in axis
    swap_int = random.randint(1, 10)
    if swap_int > 5:
        temp = axis
        axis = allies
        allies = temp
        print("Axis: " + "(" + str(len(axis)) + ")" )
        for player in axis:
            print("{:15}{:<6.3f}".format(player[0], player[3]))
        print("")
        print("Allies: " + "(" + str(len(allies)) + ")" )
        for player in allies:
            print("{:15}{:<6.3f}".format(player[0], player[3]))
    else:
        print("Axis: " + "(" + str(len(axis)) + ")" ) 
        for player in axis:
            print("{:15}{:<6.3f}".format(player[0], player[3]))
        print("")
        print("Allies: " + "(" + str(len(allies)) + ")" )
        for player in allies:
            print("{:15}{:<6.3f}".format(player[0], player[3]))

    greedy_sorting.axis = axis
    greedy_sorting.allies = allies
    greedy_sorting.axis_rating = axis_score
    greedy_sorting.allies_rating = allies_score 

# sorting all players:
def sort(players):
    sortedList = []

    for player in players:
# calculating rating of the player
        rating = players[player][1]*0.05+players[player][2]*0.95
        players[player][3] = float("%.4f" % rating)
        sortedList.append(players[player])
# printing descending list of players and their stats
    sortedList = sorted(sortedList, key=lambda x: x[3], reverse=True)
    print("")
    print("Ratings: ")

    for player in sortedList:
# prints players name and rating
        print("{:15}{:<5}".format(player[0]+": ", player[3]))
# greedy sorting
    greedy_sorting(sortedList)


# randomly picks players from the playersList, sort it and split into teams
def test(players):
    sortedList = []
    numbers_list = []

    number_of_players = random.randint(6, len(playersList)) 

# randomly picks random amount of players from the playersList
    for i in range(number_of_players):
        player = random.randint(1, len(playersList))
        while True:
            player = random.randint(1, len(playersList))
            if player not in numbers_list:
                numbers_list.append(player)
                break
        sortedList.append(playersList[player])
    print(len(sortedList))

# add rating to each player 
    for player in sortedList:
        rating = player[1]*0.05+player[2]*0.95
        player[3] = rating

    sortedList = sorted(sortedList, key=lambda x: x[3], reverse=True)
# greedy sorting:
    greedy_sorting(sortedList)

def kd_sort(players):
    sortedList = []
    print("")
    print("")
    print("K/D sort: ")
    for player in players:
        rating = players[player][1]
        players[player][3] = float("%.4f" % rating)
        sortedList.append(players[player])

    sortedList = sorted(sortedList, key=lambda x: x[3], reverse=True)
    greedy_sorting(sortedList)

def balance(players):
    print("")
    print("TEST OUTPUT: ")
    print("")
    test(players)
    axis = greedy_sorting.axis
    allies = greedy_sorting.allies
    axis_rating = greedy_sorting.axis_rating
    allies_rating = greedy_sorting.allies_rating
    random_players = []
    print("")
    removed_axis = []
# Make unbalanced teams
# choose number of the random player in axis to be moved
    while len(random_players) < random.randint(2, 4):
        random_number = random.randint(0,len(axis)-1)
        if random_number not in random_players:
            random_players.append(random_number)
    print(random_players)
    for player in random_players:
        allies.append(axis[player])
        allies_rating += axis[player][3]
        axis_rating -= axis[player][3]
        removed_axis.append(axis[player])

# remove chosen players from axis to make teams uneven
    axis = [player for player in axis if player not in removed_axis]

# pretty output
    print("")
    print("UNBALANCED TEAMS")
    print("")

    print("Axis: " + "(" + str(len(axis)) + ")")
    for player in axis:
        print("{:15}{:<6.3f}".format(player[0], player[3]))
    print("")
    print("Allies: " + "(" + str(len(allies)) + ")")
    for player in allies:
        print("{:15}{:<6.3f}".format(player[0], player[3]))
    
    print("") 
    print("Difference: " + str(axis_rating-allies_rating) + " for axis")

# permutations
    number_of_moved_players = abs(len(axis) - len(allies)) // 2
    print("Move this amount to axis: " + str(number_of_moved_players))

    if number_of_moved_players > 0:
        if len(axis) > len(allies):
            stronger_team = axis
            weaker_team = allies
            stronger_team_rating = axis_rating
            weaker_team_rating = allies_rating
            team = 'a' 
        else:
            stronger_team = allies
            weaker_team = axis
            stronger_team_rating = allies_rating
            weaker_team_rating = axis_rating
            team = 'b'

        all_possibilities = list(itertools.permutations(stronger_team, number_of_moved_players))
        turn = -1
        differences = []
        for possibility in all_possibilities:
            turn = turn + 1
            temp_weaker_team_rating = 0
            temp_stronger_team_rating = 0
            for i in range(len(possibility)):
                temp_weaker_team_rating += (possibility[i][3])
                temp_stronger_team_rating -= (possibility[i][3])
            
            difference = abs((stronger_team_rating + temp_stronger_team_rating) - (weaker_team_rating + temp_weaker_team_rating))
            differences.append([difference, possibility, turn])

# get the smallest difference between the teams
        min_value = float(abs(differences[0][0]))
        iteration = differences[0]
        iteration_turn = differences[0][2]
        for value in differences:
            first_value = value[0]
            if abs(first_value) <= min_value:
                min_value = first_value
                iteration = value
                iteration_turn = iteration[2]
        print("")

# append / remove players into right team
        for player in differences[iteration_turn][1]:
            weaker_team.append(player)
            stronger_team.remove(player)

        weaker_team = sorted(weaker_team, key=lambda x: x[3], reverse=True)
        stronger_team = sorted(stronger_team, key=lambda x: x[3], reverse=True)
        weaker_score = 0
        stronger_score = 0
        for player in weaker_team:
            weaker_score += player[3]
        for player in stronger_team:
            stronger_score +=player[3]
        print("ACTUAL SCORE COMPARE IT WITH THE SCORE BELOW: " + str(stronger_score-weaker_score))
 # pretty output
    if team == 'a':
        axis = stronger_team
        allies = weaker_team
        axis_rating = stronger_score
        allies_rating = weaker_score
    else:
        axis = weaker_team
        allies = stronger_team
        axis_rating = stronger_score
        allies_rating = weaker_score
        
    print("")
    print("")

    print("BALANCED TEAMS")
    print("")

    print("Axis: " + "(" + str(len(axis)) + ")")
    for player in axis:
        print("{:15}{:<6.3f}".format(player[0], player[3]))
    print("")
    print("Allies: " + "(" + str(len(allies)) + ")")
    for player in allies:
        print("{:15}{:<6.3f}".format(player[0], player[3]))
    
    print("") 
    print("Difference: " + str(differences[iteration_turn][0]) + " for axis")

    print("")
    print(100*"#")


# run

#kd_sort(playersList)
#test(playersList)
balance(playersList)
#sort(playersList)

