def firstDuplicate(a):
    index = len(a)+1
    pos = 0
    count = 0
    dup = 0

    for num in a:
        #print(num)
        skip = a.index(num)
        while count < len(a):
            if num == a[count]:
                if count == skip:
                    count += 1
                else:
                    tindex = count
                    if tindex <= index:
                        cindex = tindex
                        index = cindex
                    count += 1
            else:
                count += 1
        count = 0
    if index != len(a)+1:
        return a[index]
    else:
        return -1

a = [2, 1, 3, 5, 3, 2]
b = [2, 1, 3]
c = [8, 4, 6, 2, 6, 4, 7, 9, 5, 8]
print(firstDuplicate(a))
print(firstDuplicate(b))
print(firstDuplicate(c))