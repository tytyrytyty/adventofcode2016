import re, sys

abbaSeqLen = 3

def isAbaSeq(abbaSeq):
    assert(len(abbaSeq) == abbaSeqLen)
    if (abbaSeq[0] != abbaSeq[1] and abbaSeq[0] == abbaSeq[2]):
        return True
    else:
        return False

data = open('input', 'r')
supportsSSL = 0

for line in data:
    line = line.strip()
    groups = re.split('[\[\]]', line)
    isInBrackets = False
    inSeqs = []
    outSeqs = []
    for i in range(1,len(groups), 2):
        for j in range(0, len(groups[i])-2):
            if isAbaSeq(groups[i][j:j+3]):
                inSeqs.append(groups[i][j+1] + groups[i][j])

    if len(inSeqs):
        for i in range(0,len(groups), 2):
            for j in range(0, len(groups[i])-2):
                if isAbaSeq(groups[i][j:j+3]):
                    outSeqs.append(groups[i][j] + groups[i][j+1])


    if len(set(inSeqs).intersection(outSeqs)):
        supportsSSL+=1


print supportsSSL

