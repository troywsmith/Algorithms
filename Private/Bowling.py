POINTS_FOR_STRIKE = 10
import numpy as np
import pandas as pd

# class BowlingPlayer(object):
#     def __init__(self, name, overall=0):
#         self.name = name
#         self.total_points = overall

#     def frames(self):
#         shot_one = int(input('how many pins on first shot:'))
#         if shot_one == POINTS_FOR_STRIKE:  # this is a strike
#             shot_two_after_strike = int(input('how many pins on shot after strike:'))
#             self.total_points += shot_two_after_strike + shot_one

#             if shot_two_after_strike == POINTS_FOR_STRIKE:  # you got another strike. continue the frame!
#                 shot_three_after_strike = int(input('how many pins on shot after two strikes:'))
#                 self.total_points += shot_three_after_strike
#         elif shot_one < POINTS_FOR_STRIKE:
#             shot_two = int(input('how many pins on second shot:'))
#             shots = shot_one + shot_two
#             self.total_points += shots

#             if shots == POINTS_FOR_STRIKE:  # this is a spare
#                 shot_three_after_spare = int(input('how many pins on shot after spare'))
#                 self.total_points += shot_three_after_spare
#         return self.total_points


# if __name__ == '__main__':
#     craig = BowlingPlayer('craig')
#     print(craig.frames())

player1 = input('Player 1 Name: ')
scores = {
    player1: [0 for x in range(1, 12)]
}


def calculate_score(score):
    pass


def bowl(player):
    for x in range(1, 11):
        score = input('Frame ' + str(x) + ' Score: ')

        calculate_score(score)

        scores[player][x] = score

        data = np.array([[' ', 'Player', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'], [' ', player1, scores[player1][1], scores[player1][2], scores[player1]
                                                                                              [3], scores[player1][4], scores[player1][5], scores[player1][6], scores[player1][7], scores[player1][8], scores[player1][9], scores[player1][10]]])
        print(x, data)


bowl(player1)