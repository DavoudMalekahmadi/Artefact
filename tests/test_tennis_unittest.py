# -*- coding: utf-8 -*-

import unittest

from service import play_game
from tennis import TennisGame1, TennisGame2, TennisGame3
from tests.mock_data import test_cases


class TestTennis(unittest.TestCase):
    def test_Score_Game1(self):
        for testcase in test_cases:
            (p1Points, p2Points, score, p1Name, p2Name) = testcase
            game = play_game(TennisGame1, p1Points, p2Points, p1Name, p2Name)
            self.assertEqual(score, game.score())

    def test_Score_Game2(self):
        for testcase in test_cases:
            (p1Points, p2Points, score, p1Name, p2Name) = testcase
            game = play_game(TennisGame2, p1Points, p2Points, p1Name, p2Name)
            self.assertEqual(score, game.score())

    def test_Score_Game3(self):
        for testcase in test_cases:
            (p1Points, p2Points, score, p1Name, p2Name) = testcase
            game = play_game(TennisGame3, p1Points, p2Points, p1Name, p2Name)
            self.assertEqual(score, game.score())


if __name__ == "__main__":
    unittest.main()
