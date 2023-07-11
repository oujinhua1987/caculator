import json

jsonPath = "preflop_equity.json"


class RangeHelper:
    eqiltMap = map;
    allHandList = list;
    colorList=list
    def __init__(self, ):

        global allHandList
        global eqiltMap
        global colorList
        colorList=['h', 'c', 'd', 's']

        thisHandList = []

        with open("preflop_equity.json", "r") as jsonPath:
            eqiltMap = json.load(jsonPath)

        allHandList = list(eqiltMap.keys())
        # for i in range(0, len(allHandList)):
        i=0
        while(i< len(allHandList)):


            hand = allHandList[i]

            thisHandList.clear()
            handOneBase = hand[0]
            handTwoBase = hand[1]

            if "O" in hand:



                for j in range(0,len(colorList)):
                    handOne=handOneBase+colorList[j]

                    for z in range(0,len(colorList)):
                        if colorList[j]==colorList[z]:continue

                        actualHand=handOne+handTwoBase+colorList[z]
                        thisHandList.append(actualHand)


                for j in range(0,len(thisHandList)):
                    allHandList.insert(i + 1, thisHandList[j]);

                allHandList.remove(hand)
                i = i + len(thisHandList)


            elif "S" in hand:

                for j in range(0, len(colorList)):
                    handOne = handOneBase + colorList[j]

                    for z in range(0, len(colorList)):
                        if colorList[j] != colorList[z]: continue

                        actualHand = handOne + handTwoBase + colorList[z]
                        thisHandList.append(actualHand)

                for j in range(0, len(thisHandList)):
                    allHandList.insert(i + 1, thisHandList[j]);

                allHandList.remove(hand)
                i = i + len(thisHandList)
            # pocket pair
            else:
                for j in range(0, len(colorList)):
                    handOne = handOneBase + colorList[j]

                    for z in range(0, len(colorList)):
                        if colorList[j] == colorList[z]: continue
                        handTwo= handTwoBase + colorList[z]
                        actualHand = handOne + handTwo
                        samehand=handTwo+handOne

                        if actualHand not in thisHandList and samehand not in thisHandList:
                           thisHandList.append(actualHand)

                for j in range(0, len(thisHandList)):
                    allHandList.insert(i + 1, thisHandList[j]);

                allHandList.remove(hand)
                i = i + len(thisHandList)


        i=i+1


        # print(allHandList)


    def getCombosByRange(self, percentage):
        # global eqiltMap
        global allHandList
        # allcombsArray = eqiltMap.keys()
        combsCount = len(allHandList) * percentage
        # print(allHandList)
        print(int(combsCount))
        combsArray = allHandList[-int(combsCount):]
        # print(combsArray)
        return combsArray


# ra = RangeHelper()
# by_range = ra.getCombosByRange(0.23)
# print(by_range)
