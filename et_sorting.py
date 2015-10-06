#!/usr/bin/python3
import random

# sorting players into teams based on prw and k/d
# TODO:
# add more players for testing

players = {1: ['Freak', 1.9, 0.9, 0.9],2: ['Macka', 3.4, 0.8, 0.8], \
 3: ['GreatDanton', 1.69, 0.67, 0.67], 4: ['Smithay', 3.9, 0.45, 0.45], \
 5: ['Frog', 2.9, 0.83, 0.83], 6: ['Randal', 1.05, 0.35, 0.35], \
 7: ['Elph', 2.0, 0.48, 0.48], 8: ['Venom', 2.0, 0.74, 0.74], 
 9: ['Gaunt', 1.4, 0.649, 0.649], 10: ['Breh', 2.3, 0.745, 0.745], \
 11: ['Gargoyles', 2.086, 0.385, 0,385], 12: ['zyklonn', 1.949, 0.588, 0.588], \
 13: ['Etplayer', 1.855, 0.468, 0.468,], 14: ['klokk', 1.840, 0.692, 0.692], \
 15: ['death', 2.275, 0.564, 0.564], 16: ['Noxious', 2.916, 0.638, 0.638], \
 17: ['Greenfire', 3.385, 0.652, 0.652], 18: ['Noix', 1.204, 0.689, 0.689], \
 18: ['Ak/47', 1.350, 0.499, 0.499], 19: ['Stumpel', 0.692, 0.441, 0.441], \
 19: ['kdshp', 0.415, 0.333, 0.333]}
sortedList = []

for player in players:
# calculating rating of the player
    rating = players[player][1]*0.05+players[player][2]*0.95

    players[player][3] = float("%.4f" % rating)
    sortedList.append(players[player])

# printing descending list of players and their stats
sortedList = sorted(sortedList, key=lambda x: x[3], reverse=True)
for player in sortedList:
# prints players name and rating
    print("{:15}{:<5}".format(player[0]+": ", player[3]))

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
print("difference: " + str(axis_score-allies_score) + " for axis")
print("")

# since the output of the shuffle with same players is always the same
# this switches teams so that the first player (ex. Freak) doesn't always end up in axis
swap_int = random.randint(1, 10)
if swap_int > 5:
    temp = axis
    axis = allies
    allies = temp
    print("Axis: ")
    for player in axis:
        print("{:15}{:<6}".format(player[0], player[3]))
    print("")
    print("Allies: ")
    for player in allies:
        print("{:15}{:<6}".format(player[0], player[3]))
else:
    print("Axis: ")
    for player in axis:
        print("{:15}{:<6}".format(player[0], player[3]))
    print("")
    print("Allies: ")
    for player in axis:
        print("{:15}{:<6}".format(player[0], player[3]))

