from pathlib import Path
import numpy as np

p = Path(__file__).with_name("input.txt")

instructions, rulesBlock = p.open("r").read().split("\n\n")
ruleLines = rulesBlock.split("\n")
rules = {line.split(" = ")[0]: line.split("(")[1].split(")")[0].split(", ") for line in ruleLines}

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
    
