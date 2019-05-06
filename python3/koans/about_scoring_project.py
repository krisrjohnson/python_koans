#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

# Greed is a dice game where you roll up to five dice to accumulate
# points.  The following "score" function will be used calculate the
# score of a single roll of the dice.
#
# A greed roll is scored as follows:
#
# * A set of three ones is 1000 points
#
# * A set of three numbers (other than ones) is worth 100 times the
#   number. (e.g. three fives is 500 points).
#
# * A one (that is not part of a set of three) is worth 100 points.
#
# * A five (that is not part of a set of three) is worth 50 points.
#
# * Everything else is worth 0 points.
#
#
# Examples:
#
# score([1,1,1,5,1]) => 1150 points
# score([2,3,4,6,2]) => 0 points
# score([3,4,5,3,3]) => 350 points
# score([1,5,1,2,4]) => 250 points
#
# More scoring examples are given in the tests below:
#
# Your goal is to write the score method.

def score(dice):
    score = 0
    if (dice==[]): return score
    #TODO: do all the 3-of-a-kind in one step, 
    # possibly using a dict of value awarded (aka times 1000 for 1's, 100 for 2-6)
    # additionally do the extra 1 and 5's in one step, dict w/ {1:100, 2:0, 3:0, 4:0, 5:50, 6:0}

    # create a list that'll be the counts of each die face, 
    # aka die_counts[5] is how many 6's were rolled
    die_counts = list(0 for i in range(6))
    for i in dice:
        die_counts[i-1] += 1

    if (die_counts[0] >= 3): 
        score += 1000
        die_counts[0] += -3

    #now that the special 1's case is handled, do the #*100 case for any other faces and update
    score += sum((i+1) * 100 for i in range(6) if die_counts[i] >= 3)
    for i in range(len(die_counts)):
        if (die_counts[i] >= 3):
            die_counts[i] += -3

    score += die_counts[0] * 100
    score += die_counts[4] * 50

    return score
    

class AboutScoringProject(Koan):
    def test_score_of_an_empty_list_is_zero(self):
        self.assertEqual(0, score([]))

    def test_score_of_a_single_roll_of_5_is_50(self):
        self.assertEqual(50, score([5]))

    def test_score_of_a_single_roll_of_1_is_100(self):
        self.assertEqual(100, score([1]))

    def test_score_of_multiple_1s_and_5s_is_the_sum_of_individual_scores(self):
        self.assertEqual(300, score([1,5,5,1]))

    def test_score_of_single_2s_3s_4s_and_6s_are_zero(self):
        self.assertEqual(0, score([2,3,4,6]))

    def test_score_of_a_triple_1_is_1000(self):
        self.assertEqual(1000, score([1,1,1]))

    def test_score_of_other_triples_is_100x(self):
        self.assertEqual(200, score([2,2,2]))
        self.assertEqual(300, score([3,3,3]))
        self.assertEqual(400, score([4,4,4]))
        self.assertEqual(500, score([5,5,5]))
        self.assertEqual(600, score([6,6,6]))

    def test_score_of_mixed_is_sum(self):
        self.assertEqual(250, score([2,5,2,2,3]))
        self.assertEqual(550, score([5,5,5,5]))
        self.assertEqual(1150, score([1,1,1,5,1]))

    def test_ones_not_left_out(self):
        self.assertEqual(300, score([1,2,2,2]))
        self.assertEqual(350, score([1,5,2,2,2]))