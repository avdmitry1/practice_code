# Our football team finished the championship. The result of each match look like "x:y". Results of all matches are recorded in the collection.
#
# For example: ["3:1", "2:2", "0:1", ...]
#
# Write a function that takes such collection and counts the points of our team in the championship. Rules for counting points for each match:
#
# if x > y: 3 points
# if x < y: 0 point
# if x = y: 1 point
# Notes:
#
# there are 10 matches in the championship
# 0 <= x <= 4
# 0 <= y <= 4
def points(games):
    x = 0
    games = ':'.join(games)
    games = games.replace(':', "")
    score1 = list(games[0::2])
    score2 = list(games[1::2])
    for i in range(len(score1)):
        if score1[i] > score2[i]:
            x += 3
        elif score1[i] == score2[i]:
            x += 1
        else:
            x += 0
    return x


print(points(["3:1", "2:2", "0:1"]))
