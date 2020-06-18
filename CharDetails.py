import time
#Class, Race, Name, Alignment, Age, Gender, Weight, Height



def classes_overview():
    #Details about every playable class
    while True:
        Class = input("Please indicate which class you would like to take a look at with the according number attached. When you are finished, Press 0.")
        Class = int(Class)
        file = open("classes.txt","r")
        f = file.readlines()
        if Class == 0:
            return
        elif Class == 1:
            print("===BARBARIAN===")
            barblist = []
            for line in f:
                barblist.append(line.strip())
            count = 0
            while count < 6:
                print(barblist[count])
                count += 1    
            file.close()  
        elif Class == 2:
            print("===BARD===")
            bardlist = []
            for line in f:
                bardlist.append(line.strip())
            count = 6
            while count < 12:
                print(bardlist[count])
                count += 1    
            file.close()
        elif Class == 3:
            print("===CLERIC===")
            clericlist = []
            for line in f:
                clericlist.append(line.strip())
            count = 12
            while count < 18:
                print(clericlist[count])
                count += 1    
            file.close()
        elif Class == 4:
            print("===DRUID===")
            druidlist = []
            for line in f:
                druidlist.append(line.strip())
            count = 18
            while count < 24:
                print(druidlist[count])
                count += 1    
            file.close()
        elif Class == 5:
            print("===FIGHTER===")
            fighterlist = []
            for line in f:
                fighterlist.append(line.strip())
            count = 24
            while count < 30:
                print(fighterlist[count])
                count += 1    
            file.close()
        elif Class == 6:
            print("===MONK===")
            monklist = []
            for line in f:
                monklist.append(line.strip())
            count = 30
            while count < 36:
                print(monklist[count])
                count += 1    
            file.close()
        elif Class == 7:
            print("===PALADIN===")
            paladinlist = []
            for line in f:
                paladinlist.append(line.strip())
            count = 36
            while count < 42:
                print(paladinlist[count])
                count += 1    
            file.close()            
        elif Class == 8:
            print("===RANGER===")
            rangerlist = []
            for line in f:
                rangerlist.append(line.strip())
            count = 42
            while count < 48:
                print(rangerlist[count])
                count += 1    
            file.close()
        elif Class == 9:
            print("===ROGUE===")
            rougelist = []
            for line in f:
                rougelist.append(line.strip())
            count = 48
            while count < 54:
                print(rougelist[count])
                count += 1    
            file.close() 
        elif Class == 10:
            print("===SORCERER===")
            sorclist = []
            for line in f:
                sorclist.append(line.strip())
            count = 54
            while count < 60:
                print(sorclist[count])
                count += 1    
            file.close() 
        elif Class == 11:
            print("===WARLOCK===")
            warlocklist = []
            for line in f:
                warlocklist.append(line.strip())
            count = 60
            while count < 66:
                print(warlocklist[count])
                count += 1    
            file.close() 
        elif Class == 12:
            print("===WIZARD===")
            wizardlist = []
            for line in f:
                wizardlist.append(line.strip())
            count = 66
            while count < 72:
                print(wizardlist[count])
                count += 1    
            file.close()

def classes_select():
    #Selection of specific class to create

def chardetails_overview():
    #Creating Name, age, height, weight, gender
    
def race_overview():
    #Details about all the playable races for the character

def race_selection():
    #Selection of race for character


selection = classes_select
start = input(" Welcome to the DnD 5e character generator. Would you like to continue?(Yes or No)")
while start.lower() == "yes":
    print("Perfect! Now lets start with your class, all available classes listed in the handbook are below:")
    print("1. Barbarian")
    print("2. Bard")
    print("3. Cleric")
    print("4. Druid")
    print("5. Fighter")
    print("6. Monk")
    print("7. Paladin")
    print("8. Ranger")
    print("9. Rogue")
    print("10. Sorcerer")
    print("11. Warlock")
    print("12. Wizard")

    classes_overview()
    classes_select()