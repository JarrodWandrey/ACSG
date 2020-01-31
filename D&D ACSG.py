import random

def Stat_roll():
    # This does a loop six times, and the number
    # that the loop is on is stored in `i`.
    for i in range(6):
        # This puts 4 random numbers (chosen 1-6) in a new list called rolls.
        rolls = [random.randint(1, 6) for i in range(4)]

        # This removes the minimum number in the `rolls` list.
        # Even if there is more than one min number, it will only
        # remove one.
        rolls.remove(min(rolls))

        x = sum(rolls)
        #Checking each roll and assigning a modifier depending on what is rolled.
        if (x<=3):
            print(x, "Stat has been granted modifier of -4")
        elif (x>=4 and x<=5):
            print(x, "Stat has been granted modifier of -3")
        elif (x>=6 and x<=7):
            print(x, "Stat has been granted modifier of -2")
        elif (x>=8 and x<=9):
            print(x, "Stat has been granted modifier of -1")
        elif (x>=10 and x<=11):
            print(x, "Stat has been granted modifier of +0")
        elif (x>=12 and x<=13):
            print(x, "Stat has been granted modifier of +1")
        elif (x>=14 and x<=15):
            print(x, "Stat has been granted modifier of +2")
        elif (x>=16 and x<=17):
            print(x, "Stat has been granted modifier of +3")
        else:
            print(x, "Stat has been granted modifier of +4")


Stat_roll()

#Modifiers:
# 1-2       -5
# 2-3       -4
# 4-5       -3
# 6-7       -2
# 8-9       -1
# 10-11     +0
# 12-13     +1
# 14-15     +2
# 16-17     +3
# 18–19     +4
# 20–21     +5
# 22-23     +6