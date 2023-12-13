from pathlib import Path

p = Path(__file__).with_name('input-part2.txt')

# let's take some example sequences of possible ways to race for time 7 and 8
# 1*6, 2*5, 3*4, 4*3, 5*2, 6*1
# 1*7, 2*6, 3*5, 4*4, 5*3, 6*2, 1*7
# there are (times - 1) ways to race
# we remove elements from both ends of the sequence until we find the first element that is greater than the high score distance


times, distances = list(map(lambda x: list(map(int, x.split(":")[1].split())), p.open('r').read().split("\n")))
response = 1
for i, time in enumerate(times):
    dist = distances[i]
    speed = 1
    # find the first speed that allows us to have a higher score
    while speed * (time - speed) <= dist:
        speed += 1
    # use this speed to calculate the reamining ways to win the race
    possibleWays = time - 1 - (2 * (speed - 1))
    response *= possibleWays
print(response)
