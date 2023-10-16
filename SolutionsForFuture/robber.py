def houseRobberTD(houses,currentIndex,tempDict):
   if currentIndex>=len(houses):
       return 0
   else:
       if currentIndex not in tempDict:
           stealFirstHouse=houses[currentIndex]+houseRobberTD(houses,currentIndex+2,tempDict)
           skipFirstHouse=houseRobberTD(houses,currentIndex+1,tempDict)
           tempDict[currentIndex]=max(stealFirstHouse,skipFirstHouse)
       return tempDict[currentIndex]
