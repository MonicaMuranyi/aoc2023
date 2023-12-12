from pathlib import Path

p = Path(__file__).with_name('input.txt')
seedsInput, *categories = p.open('r').read().split("\n\n")

seedsInputValues = list(map(int, seedsInput.split(":")[1].split()))

# the seeds will be a list of (start, end) tuples
inputRanges = []
for i in range(0, len(seedsInputValues), 2):
    inputRanges.append((seedsInputValues[i], seedsInputValues[i] + seedsInputValues[i + 1]))

for category in categories:
    # holds all translated ranges from the previous category
    outputRanges = []

    # holds all range mapping lines for the current category
    mappings = []
    lines = category.splitlines()[1:]
    for line in lines:
        mappings.append(list(map(int, line.split())))


    # while we still have input ranges to map
    while len(inputRanges) > 0:
        seedStart, seedEnd = inputRanges.pop()
        for dest, source, length in mappings:
            # get the intersection of the mapping range and the input range
            outputRangeStart = max(source, seedStart)
            outputRangeEnd = min(source + length, seedEnd)
            if outputRangeStart < outputRangeEnd:
                # new translated range
                outputRanges.append((outputRangeStart + dest - source, outputRangeEnd + dest - source))
                # what if the input range wasn't completely mapped
                if outputRangeStart > seedStart:
                    # add the unmapped left range to the inputRanges list
                    inputRanges.append((seedStart, outputRangeStart))
                if outputRangeEnd > seedEnd:
                    # add the unmapped right range to the inputRanges list
                    inputRanges.append((seedStart, outputRangeStart))
                break
        else:
            # didn't get mapped at all so the range is the same for the next category
            outputRanges.append((seedStart, seedEnd))
    inputRanges = outputRanges
# print the minimum location range start
print(min(inputRanges)[0])
            




