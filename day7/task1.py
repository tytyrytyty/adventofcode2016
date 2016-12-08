import re, sys

abbaSeqLen = 4

def isAbbaSeq(abbaSeq):
    assert(len(abbaSeq) == abbaSeqLen)
    if (abbaSeq[0] != abbaSeq[1] and abbaSeq[0] == abbaSeq[3] and abbaSeq[1] == abbaSeq[2]):
        return True
    else:
        return False

data = open('input', 'r')
supportsTLS = 0

for line in data:
    line = line.strip()
    groups = re.split('[\[\]]', line)
    hasTLS = False
    for i in range(0,len(groups), 2):
        for j in range(0, len(groups[i])-3):
            if isAbbaSeq(groups[i][j:j+4]):
                hasTLS = True
                break;
        if hasTLS:
            break

    if hasTLS:
        for i in range(1,len(groups), 2):
            for j in range(0, len(groups[i])-3):
                if isAbbaSeq(groups[i][j:j+4]):
                    hasTLS = False
                    break;

            if not hasTLS:
                break


    if hasTLS:
        supportsTLS += 1

print supportsTLS

