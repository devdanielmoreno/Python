import random

def tr():
    return random.choice("1X2")

for i in range(15):
    #print("%5"% (random.choice("1X2")))
    #print("%5"% (random.choice(['1','X','2'])))
    print("%s %s %s %s %s"%(tr(),tr(),tr(),tr(),tr()))
    print(i)