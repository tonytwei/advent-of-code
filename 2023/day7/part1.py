f = open("input.txt", "r")
#f = open("test.txt", "r")
lines = f.readlines()

from functools import cmp_to_key
from collections import defaultdict 

def findHandStrength(hand):
    map = defaultdict(int)
    for card in hand:
        map[card] += 1
    
    # Five of a kind
    for key, count in map.items():
        if count == 5:
            return 0

    # Four of a kind
    for key, count in map.items():
        if count == 4:
            return 1

    # Full house
    countThree = False
    countTwo = False
    for key, count in map.items():
        if count == 3:
            countThree = True
        if count == 2:
            countTwo = True
    if countTwo and countThree:
        return 2

    # Three of a kind
    for key, count in map.items():
        if count == 3:
            return 3
    
    # Two pair
    countTwo = False
    for key, count in map.items():
        if count == 2 and countTwo:
            return 4
        elif count == 2:
            countTwo = True
    
    # One Pair
    countTwo = False
    for key, count in map.items():
        if count == 2:
            return 5

    # High Card
    return 6

handsMap = defaultdict(list)
for line in lines:
    hand, bet = line.split()
    handStrength = findHandStrength(hand)
    handsMap[handStrength].append((hand, bet))
handsMap = dict(sorted(handsMap.items()))

cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

def compare(hand1, hand2):
    card1 = hand1[0]
    card2 = hand2[0]
    for i in range(len(card1)):
        index1 = cards.index(card1[i])
        index2 = cards.index(card2[i])
        if index1 == index2:
            continue
        elif index1 < index2:
            return -1
        elif index1 > index2:
            return 1
    return 0

concatHandBetList = []
for handStrength, handList in handsMap.items():
    concatHandBetList.extend(sorted(handList, key=cmp_to_key(compare)))

rank = len(lines)
res = 0

for hand, bet in concatHandBetList:
    res += int(bet) * rank
    rank -= 1
print(res)