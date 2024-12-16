# THERE IS TYPICAL MISTAKE
# f = open('24-1.txt', 'r').readline()
# maxOnlyEvenDigitsNum = -1
# numString = ''
# for elem in f:
#     if elem in '2468':
#         numString += elem
#         if int(numString) > maxOnlyEvenDigitsNum:
#             maxOnlyEvenDigitsNum = int(numString)
#     else:
#         numString = ''
# print(maxOnlyEvenDigitsNum)

def isStringEvenDigitsOnly(string):
    flag = True
    for digit in string:
        if int(digit) % 2 == 1:
            flag = False
    return flag


f = open('24-1.txt', 'r').readline()
maxOnlyEvenDigitsNum = -1
numString = ''
for elem in f:
    if '0' <= elem <= '9':
        numString += elem
    else:
        if len(numString) != 0:
            if isStringEvenDigitsOnly(numString):
                maxOnlyEvenDigitsNum = max(maxOnlyEvenDigitsNum,
                                           int(numString))
        numString = ''
print(maxOnlyEvenDigitsNum)
