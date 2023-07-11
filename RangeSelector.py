from RangeHelper import RangeHelper


class RangSelector:




    def selectPreFlopRange(self,position):
        # BTN:0 CO:1 MP:2 EP:3 UTG+1:4 UTG:5 BB:6 SB:7
        #defaultRange BTN:37.71% CO:32% MP:28 EP:23% UTG+1:20% UTG:18% BB: SB:7
        if position== 0:
            percentage=0.3771
            btnCombosList = RangeHelper().getCombosByRange(percentage)

            return btnCombosList;
rs=RangSelector()
combos =rs.selectPreFlopRange(0)
print(combos)
