def printMaxActivites(activties):
    activties.sprt(key=lambda x:x[2])
    i=0
    firstA=activties[i][0]
    print(firstA)
    for j in range(len(activties)):
        if activties[j][1]>activties[i][2]:
            print(activties[j][0])
            i=j