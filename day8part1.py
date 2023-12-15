from pathlib import Path

p = Path(__file__).with_name("input.txt")

instructions, rulesBlock = p.open("r").read().split("\n\n")
ruleLines = rulesBlock.split("\n")
rules = {line.split(" = ")[0]: line.split("(")[1].split(")")[0].split(", ") for line in ruleLines}

node = "AAA"
instructionIdx = 0
steps = 0
while node != "ZZZ":
    # replace the current node with the one that the current instruction points to
    node = rules[node][0 if instructions[instructionIdx] == "L" else 1]
    print(node)
    instructionIdx = instructionIdx + 1 if instructionIdx < len(instructions) - 1 else 0
    steps += 1
print(steps)
    
