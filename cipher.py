#!/usr/bin/python 
import random
import string


def insertion(initial, counter):
    x = counter
    choices = string.printable
    elem = random.SystemRandom().choice(choices)
    initial.insert(x, elem)
    return initial


def answer(encode):
    for x in range(len(encode)):
        encode[x] = chr(encode[x])
    final = ''.join(str(x) for x in encode)
    print("\nYour encoded string is:" + final)


def scatterAscii(aList):
    for x in range(len(aList)):
        aList[x] = ((aList[x] * 17) - 32)
    for x in range(len(aList)):
        while aList[x] > 126:
            aList[x] = aList[x] - 126
        if aList[x] < 40: aList[x] = aList[x] + 40
    answer(aList)


def advancedAsciiEncryption(initial):
    encodedOriginal = []
    for x in initial:
        encodedOriginal.append(ord(x))
    encodedOriginal = scatterAscii(encodedOriginal)


def insertionEncryption(initial):
    x = 1
    choices = string.printable
    initial = insertion(initial, 0)
    while x < len(initial):
        if x % 4 != 0:
            insertion(initial, x)
        x += 1
    initial.pop(0)
    halfWay = advancedAsciiEncryption(initial)


def decideEncryption(initial):
    randomizer = random.SystemRandom().randint(0, 1)
    if randomizer == 0:
        originalEncrypted = advancedAsciiEncryption(initial)
    elif randomizer == 1:
        originalEncrypted = insertionEncryption(initial)


print("Please provide a block of text that you want encoded.")
original = list(input())
decideEncryption(original)
print("\nWould you like to know which version of encryption was used?(Y/N)")
versionRequest = input()
if versionRequest == 'Y' or 'y':
    print("Please enter username and password:\n")
else:
    quit()
