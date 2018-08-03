def firstDuplicate(a):
    dictFirst = {}
    dictSecondIdx = {}

    for idx, c in enumerate(a):
        if c not in dictFirst:
            dictFirst[c] = idx  # never heard of c - add to our KB
        else:  # not the first occurence
            if c not in dictSecondIdx:  # only add idx of first duplicate
                dictSecondIdx[c] = idx
            else:
                pass

    # analyze index of second entries
    if len(dictSecondIdx) == 0:
        return -1
    else:
        # find the minimum
        result = min(dictSecondIdx.keys(), key=(lambda k: dictSecondIdx[k]))
        return result

a = [2, 1, 3, 5, 3, 2]
b = [2, 1, 3]
c = [8, 4, 6, 2, 6, 4, 7, 9, 5, 8]
print(firstDuplicate(a))
print(firstDuplicate(b))
print(firstDuplicate(c))