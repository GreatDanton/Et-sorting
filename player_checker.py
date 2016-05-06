#!usr/bin/python3

# Author: GreatDanton

# compares player names on tb and sl

import urllib.request
from bs4 import BeautifulSoup
import re

# get html code from urls below 
tb_url = "http://et.trackbase.net/clan/83/" 
sl_url = "http://et.splatterladder.com/?mod=claninfo&idx=119505"

# players array
trackbase_players = []
splatterladder_players = []

# parse html from the url function
def parse_html(url):
    try:
        connection = urllib.request.urlopen(url)

        html = str(connection.read())

        connection.close()

        return html
    except urrlib.request.URLError:
        print('Cannot download html, check your internet connection')


# get player names from data and push them to array 
def get_players(data, arr):
    if arr == 'tb': 
        table_start = data.find('<div class="ci-content-content ci-members-table">')
        table_end = data.find('</table>', table_start)

        html = data[table_start:table_end]
        soup = BeautifulSoup(html, 'html.parser')
        html = soup.get_text()

        starting_pos = 0
        while True:
                starting_pos = html.find('<=TM', starting_pos)

                if starting_pos == -1:
                    return False
                else:
                    ending_pos = html.find(' ', starting_pos)
                    player = html[starting_pos:ending_pos]

# make spaces and ' (apostrophe) pretty
                    player = re.sub(r'\xa0', ' ', player)
                    player = re.sub(r"\\'", "'", player)
# append to array
                    trackbase_players.append(player)
                    starting_pos += 1
    else: 
# getting names from splatterladder data
        table_start = data.rfind('id="head"')
        table_end = data.rfind('</table') 

        html = data[table_start:table_end]
        soup = BeautifulSoup(html, 'html.parser')
        html = soup.get_text()

        starting_pos = 0 
# deletes all new lines characters       
        html = re.sub(r'\s', html, ' ')        
# get player names
        while True:
            starting_pos = html.find('<=TM=>', starting_pos)
            if starting_pos == -1:
                return False
            else:
                end_pos = html.find('\n', starting_pos)

                player = html[starting_pos:end_pos]
                if '→' in player:
                    s = player.find('→') 
                    player = player[:s]
                elif '(Trial)' in player:
                    s = player.find('(Trial)')
                    player = player[:s]
                elif '(Inactive)' in player:
                    s = player.find('(Inactive)')
                    player = player[:s]
# make spaces and apostrophes pretty
                player = re.sub(r"\\'", "'", player)
                player = re.sub(r'\xa0', ' ', player)
# append to sl array
                splatterladder_players.append(player)
                starting_pos += 1


# parse html from tb and sl
tb_html = parse_html(tb_url)
sl_html = parse_html(sl_url)
# append player names to tb and sl array
get_players(tb_html, 'tb')
get_players(sl_html, 'sl')

# prints every name in array => for test only

#get_players(tb_html, 'tb')
#print("Trackbase players: ")
#print(trackbase_players)

#print("")
#print("Splatterladder players: ")
#print(splatterladder_players)


print("")
print("Players from TB not in SL")
print("=========================================")
for player in trackbase_players:
    if player not in splatterladder_players:
        print(player)

print("")
print("")
print("Players from SL not in TB")
print("==========================================")
for player in splatterladder_players:
    if player not in trackbase_players:
        print(player)
