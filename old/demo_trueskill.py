# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 19:09:42 2017

@author: Stephan Porz
"""

# http://trueskill.org/

import trueskill

# rating objects for players
player1 = trueskill.Rating()
player2 = trueskill.Rating()
player3 = trueskill.Rating()
player4 = trueskill.Rating()

print player1

# change player rating based on game results
player1, player2 = trueskill.rate_1vs1(
    player1, player2)

print player1
print player2


player1, player2 = trueskill.rate_1vs1(
    player1, player2, drawn=True)

print player1
print player2


teams = [
    [player1, player2], 
    [player3, player4]
]
results = [
    1, 
    2
]

[
    [player1, player2], 
    [player3, player4]
] = (
    trueskill.rate(teams, ranks = results))

print player1
print player2
print player3
print player4


# player has a minimum skill of [95% confidence]
print player1.mu - 2.575829303549 * player1.sigma


# matchmaking
# quality returns draw probability
trueskill.quality([[player1], [player2]])


