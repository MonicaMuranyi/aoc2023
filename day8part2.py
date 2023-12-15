from pathlib import Path
import numpy as np

p = Path(__file__).with_name("input.txt")

instructions, rulesBlock = p.open("r").read().split("\n\n")
ruleLines = rulesBlock.split("\n")
rules = {line.split(" = ")[0]: line.split("(")[1].split(")")[0].split(", ") for line in ruleLines}

# Solving this via bruteforce (i.e. simulating all steps until all destinations meet) takes too much time
# Suppose for a starting node we reach the destination in X steps, then we also reach it in 2*X steps, 3*X steps and so on
# That means we reach all destinations at the same time after N steps
# where N is the least common multiple of the number of steps to reach each destionation

def getStepsForStartNode(node):
    instructionIdx = 0
    steps = 0
    while node[2] != "Z":
        node = rules[node][0 if instructions[instructionIdx] == "L" else 1]
        instructionIdx = instructionIdx + 1 if instructionIdx < len(instructions) - 1 else 0
        steps += 1
    return steps

currentNodes = [line.split(" = ")[0] for line in ruleLines if line.split(" = ")[0][2] == "A"]
stepsPerNode = [getStepsForStartNode(node) for node in currentNodes]

print(stepsPerNode)
print(np.lcm.reduce(stepsPerNode))
