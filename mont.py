import numpy
import random 
import seaborn


random.seed(3)
doors = [1,0,0]

nbsim = 1000
repreat = 1000

repreatsim = []
for i in range(repreat):
    win = []
    for i in range(nbsim):
        gamedoors = random.sample(doors,3)
        pickdoor = random.sample([0,1,2],1)

        tmpop = []
        for i in range(3):
            if numpy.sum(pickdoor) != i:
                if gamedoors[i] == 0:
                    tmpop.append(i)
        opendoor = numpy.sum(random.sample(tmpop,1))

        tmpnewc = []
        for i in range(3):
            if i not in [numpy.sum(pickdoor),opendoor]:
                tmpnewc.append(i)
        win.append(gamedoors[numpy.sum(tmpnewc)])
    repreatsim.append(numpy.sum(win)/nbsim)

p = seaborn.distplot(repreatsim,kde=False,rug=True).get_figure()
p.savefig('distofmonty.png')
