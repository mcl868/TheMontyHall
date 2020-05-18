import numpy
import pandas
import random 


random.seed(3)
doors = [["car"],["goat"],["goat"]]
doornb = [1,2,3]

nbsim = 1000

nbgameshow = []
DoorPos1 = []
DoorPos2 = []
DoorPos3 = []
choice = []
opdoor = []
newdoor = []
win = []
for i in range(nbsim):
    gamedoors = random.sample(doors,3)
    pickdoor = random.sample([0,1,2],1)

    DoorPos1.append(gamedoors[0])
    DoorPos2.append(gamedoors[1])
    DoorPos3.append(gamedoors[2])

    nbgameshow.append(i+1)
    
    choice.append(doornb[numpy.sum(pickdoor)])

    tmpop = []
    for i in range(3):
        if numpy.sum(pickdoor) != i:
            if gamedoors[i] == ["goat"]:
                tmpop.append(i)
    opendoor = numpy.sum(random.sample(tmpop,1))
    opdoor.append(doornb[opendoor])

    tmpnewc = []
    for i in range(3):
        if i not in [numpy.sum(pickdoor),opendoor]:
            tmpnewc.append(i)
    newdoor.append(doornb[numpy.sum(tmpnewc)])
    win.append(gamedoors[numpy.sum(tmpnewc)])

montyhall = {"Gameshow":nbgameshow,
             "DoorPos.1": DoorPos1,
             "DoorPos.2": DoorPos2,
             "DoorPos.3": DoorPos3,
             "Chioce": choice,
             "DoorOpen": opdoor,
             "DoorNew": newdoor,
             "Win": win}

dfmontyhall = pandas.DataFrame(montyhall,
                               columns = ["Gameshow",
                                          "DoorPos.1","DoorPos.2","DoorPos.3",
                                          "Chioce","DoorOpen","DoorNew","Win"])

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
print(dfmontyhall["DoorOpen"].value_counts()/nbsim)
print("")
print("")
print("The door that was chosen afterwards")
print(dfmontyhall["DoorNew"].value_counts()/nbsim)
print("")
print("")
print("The probability for win either the car or the goat")
print(dfmontyhall["Win"].value_counts()/nbsim)





