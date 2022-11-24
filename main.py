debug = []
debug2 = []


def compress(n: int):
    returnBinVar = ""

    while n != 1:
        if (n % 2) == 0:
            n /= 2
            returnBinVar += "0"
            debug.append(n)
        elif (n % 2) != 0:
            n -= 1
            n /= 2
            returnBinVar += "1"
            debug.append(n)

    number2 = str(returnBinVar)
    oneStreak = 0
    zeroStreak = 0

    finalStr = ""

    for i in range(0, len(number2)):
        if i == 0:
            if number2[i] == "0":
                zeroStreak += 1
            else:
                finalStr += str(oneStreak)
        if number2[i] == "0":
            zeroStreak += 1
            if oneStreak != 0:
                finalStr += str(oneStreak)
            oneStreak = 0
        elif number2[i] == "1":
            oneStreak += 1
            if zeroStreak != 0:
                finalStr += str(zeroStreak)
            zeroStreak = 0
        if i == len(number2) - 1:
            if oneStreak != 0:
                finalStr += str(oneStreak)
            elif zeroStreak != 0:
                finalStr += str(zeroStreak)

    print("1.", finalStr)

    return returnBinVar


def decompress(n: str):
    number = 1
    binstr = n

    while len(binstr) != 0:
        if binstr[-1] == "1":
            number *= 2
            number += 1
            binstr = binstr[:(len(binstr) - 1)]
            debug2.append(number)
        elif binstr[-1] == "0":
            number *= 2
            binstr = binstr[:(len(binstr) - 1)]
            debug2.append(number)

    print("4.", number)  # debug

    return number


x = 200000000000069  # max  is 227227227227227
n2 = compress(x)
print("2.", int(n2, 2))  # base
print("3. ", n2)
decompress(n2)
