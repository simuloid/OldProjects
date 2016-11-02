# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 09:50:42 2016

@author: Steve


Poker hands
Problem 54
In the card game poker, a hand consists of five cards and 
are ranked, from lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank 
made up of the highest value wins; for example, a pair of 
eights beats a pair of fives (see example 1 below). But if 
two ranks tie, for example, both players have a pair of 
queens, then highest cards in each hand are compared (see 
example 4 below); if the highest cards tie then the next 
highest cards are compared, and so on.

Consider the following five hands dealt to two players:

Hand	 	Player 1           Player 2         Winner
1	 	5H 5C 6S 7S KD     2C 3S 8S 8D TD      Player 2
       Pair of Fives      Pair of Eights
 	
2	 	5D 8C 9S JS AC    2C 5C 7D 8S QH       Player 1
       Highest card Ace Highest card Queen
 	 	
3	 	2D 9C AS AH AC    3D 6D 7D TD QD       Player 2
       Three Aces       Flush with Diamonds
 	
4	 	4D 6S 9H QH QC    3D 6D 7H QD QS       Player 1
  Pair of Queens (9 high) (pair Q 7 high)

5	 	2H 2D 4C 4D 4S    3C 3D 3S 9S 9D       Player 1
       Full House of 4s  Full House of 3s

The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?
"""

ranks = '23456789TJQKA'
suits = 'CDHS'

def rank(c):
    return 2+ranks.index(c[0])
    
def suit(c):
    return suits.index(c[1])

def high_card(hand, n=0):
    return rank(hand[n])

def is_flush(hand):
    for c in hand:
        if suit(c) != suit(hand[0]):
            return False
    return True

def is_straight(hand):
    for p in range(0, len(hand)):
        if rank(hand[p]) != rank(hand[0])-p:
            return False
    return True
    
def is_straight_flush(hand):
    return is_straight(hand) and is_flush(hand)
           
def is_royal_flush(hand):
    return high_card(hand) == rank('AH') and \
    is_straight_flush(hand)

def is_n_of_a_kind(hand, n):
    for i in range(len(hand)-n+1):
        if rank(hand[i]) == rank(hand[i+n-1]):
            return rank(hand[i])
            
    return None

def is_four_of_a_kind(hand):
    return is_n_of_a_kind(hand, 4)
           
def is_three_of_a_kind(hand):
    return is_n_of_a_kind(hand, 3)

def is_pair(hand):
    return is_n_of_a_kind(hand, 2)
    
def remove_all(v, L):
    return [i for i in L if rank(i) != v]
    
def is_full_house(hand):
    f = is_n_of_a_kind(hand, 3)
    if f != None:
        h = remove_all(f, hand)
        p = is_n_of_a_kind(h, 2)
        if p != None:
            return (f, p)
    return None
           
def is_two_pairs(hand):
    f = is_n_of_a_kind(hand, 2)
    if f != None:
        h = remove_all(f, hand)
        p = is_n_of_a_kind(h, 2)
        if p != None:
            return (max([f, p]), min([f, p]))
    return None
           
predicates = [ is_royal_flush, \
               is_straight_flush, \
               is_four_of_a_kind, \
               is_full_house, \
               is_flush, \
               is_straight, \
               is_three_of_a_kind, \
               is_two_pairs, \
               is_pair \
             ]
             
pred_names = [ "royal_flush", \
               "straight_flush", \
               "four_of_a_kind", \
               "full_house", \
               "flush", \
               "straight", \
               "three_of_a_kind", \
               "two_pairs", \
               "pair", \
               "high_card" \
             ]

def hand_type(hand):
    for i, p in enumerate(predicates):
        tb = p(hand)
        if tb:
            return i
    return len(predicates)
            
    
def report(hand):
    t, tb = hand_type(hand)
    if t < 9:
        print hand, pred_names[t], 'tb=', tb
            
def compare_first_nonmatching(h1, h2):
    for c1, c2 in zip(h1, h2):
        if rank(c1) != rank(c2):
            return rank(c2) - rank(c1)
    return 0

# Returns a numeric comparison of h1 and h2.
# Negative numbers imply h1 is stronger than h2
# Positive numbers imply h2 is stronger than h1
# 0 is a tie
def compare(h1, h2):
    r1 = hand_type(h1)
    r2 = hand_type(h2)
    relevant = 5

    if r1 < relevant or r2 < relevant:
        print
        print h1, h2
        print pred_names[r1],pred_names[r2]
        
    if r1 != r2:
        return r1 - r2
    # Same hand type.  Break tie based on type.
    type_name = pred_names[r1]
    if type_name == "high_card":
        return compare_first_nonmatching(h1, h2)
    elif type_name == "pair":
        r1 = is_n_of_a_kind(h1, 2)
        r2 = is_n_of_a_kind(h2, 2)
        if r1 != r2:
            return r2 - r1
        q1 = remove_all(r1, h1)
        q2 = remove_all(r2, h2)
        return compare_first_nonmatching(q1, q2)
    elif type_name == "two_pairs":
        tb1 = is_two_pairs(h1)
        tb2 = is_two_pairs(h2)
        if tb1[0] != tb2[0]:
            return tb2[0] - tb1[0]
        elif tb1[1] != tb2[1]:
            return tb2[1] - tb1[1]

        q1 = remove_all(tb1[0], h1)
        q1 = remove_all(tb1[1], q1)
        q2 = remove_all(tb2[0], h2)
        q2 = remove_all(tb2[1], q2)
        return compare_first_nonmatching(q1, q2)
    elif type_name == "three_of_a_kind":
        r1 = is_n_of_a_kind(h1, 3)
        r2 = is_n_of_a_kind(h2, 3)
        if r1 != r2:
            return r2 - r1
        q1 = remove_all(r1, h1)
        q2 = remove_all(r2, h2)
        return compare_first_nonmatching(q1, q2)
    elif type_name == "straight":
        return compare_first_nonmatching(h1, h2)
    elif type_name == "flush":
        return compare_first_nonmatching(h1, h2)
    elif type_name == "full_house":
        tb1 = is_full_house(h1)
        tb2 = is_full_house(h2)
        if tb1[0] != tb2[0]:
            return tb2[0] - tb1[0]
        elif tb1[1] != tb2[1]:
            return tb2[1] - tb1[1]
        return 0
    elif type_name == "four_of_a_kind":
        r1 = is_n_of_a_kind(h1, 4)
        r2 = is_n_of_a_kind(h2, 4)
        if r1 != r2:
            return r2 - r1
        q1 = remove_all(r1, h1)
        q2 = remove_all(r2, h2)
        return compare_first_nonmatching(q1, q2)    
    elif type_name == "straight_flush":
        return compare_first_nonmatching(h1, h2)
    elif type_name == "royal_flush":
        # All royal flushes tie
        return 0
    else:
        raise "Unknown hand type: " + type_name
    
    return 0
    
if __name__ == '__main__':
    f = open('p054_poker.txt')
    a = 0
    for line in f:
        cards = line.split()
        p1 = cards[:5]
        p1.sort(key=rank, reverse=True)
        p2 = cards[5:]
        p2.sort(key=rank, reverse=True)
        c = compare(p1, p2)
        # print c
        if c < 0:
            a += 1
    f.close()
    print a
    
