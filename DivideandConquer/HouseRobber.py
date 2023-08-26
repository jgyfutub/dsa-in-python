def HouseRobber(houses,currentIndex):
    if currentIndex>=len(houses):
        return 0
    else:
        stealFirstHouse=houses[currentIndex]+HouseRobber(houses,currentIndex+2)
        skipFirstHouse=HouseRobber(houses,currentIndex+1)
        return max(stealFirstHouse,skipFirstHouse)