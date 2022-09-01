# -*- coding: utf-8 -*-

class TennisGame:
    def __init__(self, player1_name: str, player2_name: str):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1_points = 0
        self.p2_points = 0

    def won_point(self, player_name: str):
        if player_name == self.player1_name:
            self.p1_points += 1
        else:
            self.p2_points += 1


class TennisGame1(TennisGame):
    def score(self) -> str:
        result = ""
        temp_score = 0
        if self.p1_points == self.p2_points:
            result = {
                0: "Love-All",
                1: "Fifteen-All",
                2: "Thirty-All",
            }.get(self.p1_points, "Deuce")
        elif self.p1_points >= 4 or self.p2_points >= 4:
            minus_result = self.p1_points - self.p2_points
            if minus_result == 1:
                result = "Advantage " + self.player1_name
            elif minus_result == -1:
                result = "Advantage " + self.player2_name
            elif minus_result >= 2:
                result = "Win for " + self.player1_name
            else:
                result = "Win for " + self.player2_name
        else:
            for i in range(1, 3):
                if i == 1:
                    temp_score = self.p1_points
                else:
                    result += "-"
                    temp_score = self.p2_points
                result += {
                    0: "Love",
                    1: "Fifteen",
                    2: "Thirty",
                    3: "Forty",
                }[temp_score]
        return result


class TennisGame2(TennisGame):
    def score(self) -> str:
        result = ""
        p1_result = ""
        p2_result = ""

        if self.p1_points == self.p2_points and self.p1_points < 3:
            if self.p1_points == 0:
                result = "Love"
            elif self.p1_points == 1:
                result = "Fifteen"
            elif self.p1_points == 2:
                result = "Thirty"
            result += "-All"
        if self.p1_points == self.p2_points and self.p1_points > 2:
            result = "Deuce"
        if self.p1_points > 0 and self.p2_points == 0:
            if self.p1_points == 1:
                p1_result = "Fifteen"
            elif self.p1_points == 2:
                p1_result = "Thirty"
            elif self.p1_points == 3:
                p1_result = "Forty"
            p2_result = "Love"
            result = p1_result + "-" + p2_result
        if self.p2_points > 0 and self.p1_points == 0:
            if self.p2_points == 1:
                p2_result = "Fifteen"
            elif self.p2_points == 2:
                p2_result = "Thirty"
            elif self.p2_points == 3:
                p2_result = "Forty"
            p1_result = "Love"
            result = p1_result + "-" + p2_result
        if self.p2_points < self.p1_points < 4:
            if self.p1_points == 2:
                p1_result = "Thirty"
            elif self.p1_points == 3:
                p1_result = "Forty"
            if self.p2_points == 1:
                p2_result = "Fifteen"
            elif self.p2_points == 2:
                p2_result = "Thirty"
            result = p1_result + "-" + p2_result
        if self.p1_points < self.p2_points < 4:
            if self.p2_points == 2:
                p2_result = "Thirty"
            elif self.p2_points == 3:
                p2_result = "Forty"
            if self.p1_points == 1:
                p1_result = "Fifteen"
            elif self.p1_points == 2:
                p1_result = "Thirty"
            result = p1_result + "-" + p2_result
        if self.p1_points > self.p2_points >= 3:
            result = "Advantage " + self.player1_name
        if self.p2_points > self.p1_points >= 3:
            result = "Advantage " + self.player2_name
        if self.p1_points >= 4 and self.p2_points >= 0 and (self.p1_points - self.p2_points) >= 2:
            result = "Win for " + self.player1_name
        if self.p2_points >= 4 and self.p1_points >= 0 and (self.p2_points - self.p1_points) >= 2:
            result = "Win for " + self.player2_name
        return result

    def set_p1_score(self, points: int):
        self.p1_points += points

    def set_p2_score(self, points: int):
        self.p2_points += points


class TennisGame3(TennisGame):
    def score(self) -> str:
        if (self.p1_points < 4 and self.p2_points < 4) and (self.p1_points + self.p2_points < 6):
            p = ["Love", "Fifteen", "Thirty", "Forty"]
            s = p[self.p1_points]
            return s + "-All" if (self.p1_points == self.p2_points) else s + "-" + p[self.p2_points]
        else:
            if self.p1_points == self.p2_points:
                return "Deuce"
            s = self.player1_name if self.p1_points > self.p2_points else self.player2_name
            return "Advantage " + s if (
                    (self.p1_points - self.p2_points) * (self.p1_points - self.p2_points) == 1) else "Win for " + s
