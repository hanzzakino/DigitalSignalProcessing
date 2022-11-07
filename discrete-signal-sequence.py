from typing import Callable

def getSequence(func:Callable, scale = 1, shift = 0):

    neg_range = []
    count0 = 0
    i = -1
    while(True):
        n = x((scale*i))
        if(n == 0):
            count0 += 1
        else:
            count0 = 0
        if count0>10000:
            break
        neg_range.insert(0,n)
        i -= 1
    neg_range = neg_range[count0-2:]

    pos_range = []
    count0 = 0
    i = 0
    while(True):
        n = x((scale*i))
        if(n == 0):
            count0 += 1
        else:
            count0 = 0
        if count0>10000:
            break
        pos_range.append(n)
        i += 1
    pos_range = pos_range[:len(pos_range)-(count0-2)]
    sequence = neg_range + pos_range

    mid_index = len(neg_range)

    if mid_index+shift < 0:
        for i in range(abs(mid_index+shift)+1):
            sequence.insert(0,0)
        mid_index = 1
    elif mid_index+shift > len(sequence)-1:
        for i in range(abs(mid_index+shift)-len(sequence)+2):
            sequence.append(0)
        mid_index = len(sequence)-2
    else:
        mid_index += shift

    return {"sequence":sequence,"mid":mid_index}

def printSequence(seq):
    seqString = '{...'
    for i,n in enumerate(seq["sequence"]):
        if i == seq["mid"]:
            seqString += ' <'+str(n)+'> ,' 
        elif i == len(seq["sequence"])-1:
            seqString += ' '+str(n)+' '
        else:
            seqString += ' '+str(n)+' ,'
    seqString += '...}'
    print(seqString)


def x(n):
    if -5<=n<=-1:
        return 4-n
    elif 0<=n<=4:
        return 4
    else:
        return 0

printSequence(getSequence(x, scale = -1, shift = 0))