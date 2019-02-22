#!/bin/python3

import math
import os
import random
import re
import sys

#should use dict comprehension but too tired to think
def create_tally(votes):
        tally = {}#why dont I use a default dict xD derp
        for person in votes:
            if person not in tally:
                tally[person] = 1
            else:
                prev_votes = tally[person] + 1
                tally.update({person:prev_votes}) #not correct way to update entry, fix this
    return tally

def default_candidate(tally):
    current = 0
    defacto = ''
    for candidate, votes in tally.items():
        if votes > current:
            defacto = candidate
            break
    return defacto

def choose_winner(tally):
    current_winner = default_candidate(tally)
    potential_winners = []

    for person, votes in tally.items():#this doesnt consider case when we find a new highest count and forget to empty list

        if votes > tally[current_winner]:
            potential_winners.remove(current_winner)
            current_winner = person

        if votes == tally[current_winner]:
            #add them to a list for later sorting
            if person not in potential_winners:
                potential_winners.append(person)

    winners = potential_winners.copy()#deep copy, dont ever mod an item directly
    winners.sort(reverse=True)

    return winners[0]#improper way of returning cause doesnt consider an empty list

# Complete the electionWinner function below.
def electionWinner(votes):
    tally = create_tally(votes)
    winner = choose_winner(tally)
    return winner

if __name__ == '__main__':
    pass
