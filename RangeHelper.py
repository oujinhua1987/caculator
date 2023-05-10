import json

jsonPath = "preflop_equity.json"


class RangeHelper:
    eqiltMap = map;
    allHandList = list;

    def __init__(self, ):
        global allHandList
        global eqiltMap
        with open("preflop_equity.json", "r") as jsonPath:
            eqiltMap = json.load(jsonPath)

        allHandList = list(eqiltMap.keys())
        # for i in range(0, len(allHandList)):
        i=0
        while(i< len(allHandList)):


            hand = allHandList[i]

            if "O" in hand:

                for j in range(0, 15):
                    allHandList.insert(i + 1, hand);

                i = i + 16




            elif "S" in hand:

                for j in range(0, 3):
                    allHandList.insert(i + 1, hand);

                i = i + 4
            # pocket pair
            else:
                for j in range(0, 5):
                    allHandList.insert(i + 1, hand);

                i = i + 6



        i=i+1


        # print(allHandList)


    def getCombByRange(self, percentage):
        global eqiltMap
        # allcombsArray = eqiltMap.keys()
        combsCount = len(allHandList) * percentage
        # print(allHandList)
        print(int(combsCount))
        combsArray = allHandList[-int(combsCount):]
        print(combsArray)
        return combsArray


ra = RangeHelper()
ra.getCombByRange(0.23)
