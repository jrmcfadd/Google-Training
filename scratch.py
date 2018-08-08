def isogram(word):
    before = len(word)
    after = len(set(word))

    if before == after:
        return True
    else:
        return False


def isogramNew(word):
    seen = {}

    for letter in word:
        if letter in seen:
            return False
        else:
            seen[letter] = 1
    return True


def removeDup(word):
    seen = {}
    newWord = ''
    if word:
        for letter in word:
            if letter in seen:
                pass
            else:
                seen[letter] = 1
                newWord = newWord + letter
    return newWord


def anagram(word1, word2):
    if len(word1) >  len(word2):
        return False

    test = len(word2)
    for letter in word1:
        if letter in word2:
            test = True
        else:
            return False
    return True

def cstyle(word):
    print(word)
    print(word[::-1])


def space_replace(phrase):
    return phrase.replace(" ", "%20")


answer = space_replace('hello world')
print(answer)