
with open('list.txt', 'r') as file:
    list1 = file.read().translate(str.maketrans({'\n':'   '})).split("   ")

total = 0
FirVal = 0
SecVal = 0
ListFirstLine = list1[::2]
ListSecondLine = list1[1::2]
ListFirstLine.sort()
ListSecondLine.sort()
ListFirstLine = ListFirstLine[1:]
for i in range(len(ListFirstLine)):
    ListFirstLine[i] = int(ListFirstLine[i])
for i in range(len(ListSecondLine)):
    ListSecondLine[i] = int(ListSecondLine[i])

for i in range(len(ListFirstLine)):
    FirVal = abs(ListSecondline[i] - ListFirstLine[i])
    total = total + FirVal


total = str(total)
print('Differenz insgesamt ' +  total)
