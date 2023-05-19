import random

dayCharacters = ""
temp = random.randint(1,31)
if temp in range(1,9):
    dayCharacters = "0" + str(temp)
else:
    dayCharacters = temp

monthCharacters = ""
temp = random.randint(1,12)
if temp in range(1,9):
    monthCharacters = "0" + str(temp)
else:
    monthCharacters = temp


print(dayCharacters)