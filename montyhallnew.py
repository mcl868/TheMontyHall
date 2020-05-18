import numpy
import pandas
import random 


random.seed(3)
doors = [["car"],["goat"],["goat"]]
doornb = [1,2,3]

nbsim = 1000

nbgameshow = []
choice = []
opdoor = []
newdoor = []
win = []


nbgameshow = []
DoorPos1 = []
DoorPos2 = []
DoorPos3 = []
choice = []
choiceMonty = []
newdoor = []
win = []
for i in range(nbsim):

    list1 = [0,1,2]

    gamedoors = random.sample(doors,3)
    pickdoor = random.sample(list1,1)

    DoorPos1.append(gamedoors[0])
    DoorPos2.append(gamedoors[1])
    DoorPos3.append(gamedoors[2])

    nbgameshow.append(i+1)

    for ele in list1:
        if [ele] == pickdoor:
            list1.remove(ele) 

    pickmontydoor = random.sample(list1,1)

    choice.append(doornb[numpy.sum(pickdoor)])
    choiceMonty.append(doornb[numpy.sum(pickmontydoor)])

    if gamedoors[numpy.sum(pickmontydoor)] == ["goat"]:
        for ele in list1:
            if [ele] == pickmontydoor:
                list1.remove(ele)
    elif gamedoors[numpy.sum(pickmontydoor)] == ["car"]:
        list1 = pickmontydoor


    newdoor.append(doornb[numpy.sum(list1)])
    win.append(gamedoors[numpy.sum(list1)])



montyhall = {"Gameshow":nbgameshow,
             "DoorPos.1": DoorPos1,
             "DoorPos.2": DoorPos2,
             "DoorPos.3": DoorPos3,
             "Chioce": choice,
             "choiceMonty": choiceMonty,
             "DoorNew": newdoor,
             "Win": win}

dfmontyhall = pandas.DataFrame(montyhall,
                               columns = ["Gameshow",
                                          "DoorPos.1","DoorPos.2","DoorPos.3",
                                          "Chioce","choiceMonty","DoorNew",
                                          "Win"])

print("     _     _  ___  __    _ _______ _     _ _    _     __     _      _      ")
print("    | \  /  |/ _ \|   \ | |__   __| \   / | |  | |   /  \   | |    | |     ")
print("    |  \/   | / \ | |\ \| |  | |   \ \_/ /| |__| |  / /\ \  | |    | |     ")
print("    | |\_/| ||   || | \ | |  | |    \   / |  __  | / /__\ \ | |    | |     ")
print("    | |   | | \_/ | |  \  |  | |     | |  | |  | |/ ______ \| |____| |____ ")
print("    |_|   |_|\___/|_|   \_|  |_|     |_|  |_|  |_|_/      \_|______|______|")
print("                                  SIMULATION                               ")



print("")
print(dfmontyhall[dfmontyhall["Gameshow"] <= 10])
print("")
print("The door that has been chosen at first")
print(dfmontyhall["Chioce"].value_counts()/nbsim)
print("")
print("")
print("The door that was open")
print(dfmontyhall["choiceMonty"].value_counts()/nbsim)
print("")
print("")
print("The door that was chosen afterwards")
print(dfmontyhall["DoorNew"].value_counts()/nbsim)
print("")
print("")
print("The probability for win either the car or the goat")
print(dfmontyhall["Win"].value_counts()/nbsim)



